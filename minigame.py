import random
option = range(1, 10)
while True:
    secret = random.choice(option)
    guess = int(input("guess a number(1, 10): "))
    
    if guess not in option:
        print("not in range. try again")
        continue
    if guess == secret:
        print("you win!")
        retry = input("do you wanna play again? ")
        if retry != "yes":
            print("thanx for playing!")
            break
    else:
        print("you lose! the number was", secret)
        retry = input("do you wanna play again? ")
        if retry != "yes":
            print("thanx for playing!")
            break







