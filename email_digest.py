import requests
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
CITY = os.getenv("CITY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={WEATHER_API_KEY}"
    data = requests.get(url).json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    return f"{city.title()}: {temp}°C, {desc}"

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=3&apiKey={NEWS_API_KEY}"
    data = requests.get(url).json()
    headlines = [f"- {article['title']}" for article in data["articles"]]
    return "\n".join(headlines)

def get_quote():
    url = "https://api.quotable.io/random"
    data = requests.get(url).json()
    return f'"{data["content"]}" – {data["author"]}'

def create_email_digest():
    weather = get_weather(CITY)
    news = get_news()
    quote = get_quote()

    content = f"""
    <h2>Your Daily Digest</h2>
    <h3>📍 Weather</h3>
    <p>{weather}</p>
    
    <h3>📰 News</h3>
    <pre>{news}</pre>
    
    <h3>💡 Quote of the Day</h3>
    <blockquote>{quote}</blockquote>
    """
    return content

def send_email(subject, body):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = RECIPIENT_EMAIL

    part = MIMEText(body, "html")
    msg.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

if __name__ == "__main__":
    digest = create_email_digest()
    send_email("📬 Your Daily Email Digest", digest)
    print("Email sent successfully!")
