import random
secret = random.randint(1, 10)
guess =int(input("guess a number: "))

if guess == secret:
    print("correct")
else:
    print("not correct")

