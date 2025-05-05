import random
secret = random.randit(1, 10)
guess =int(input("guess a number: "))

if guess == secret:
    print("correct")
else:
    print("not correct")

