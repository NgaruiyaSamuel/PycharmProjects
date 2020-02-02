import random
number = random.randint(1, 10)
tries = 1

uname = input("Hello, what is your username?")
print("Hello", uname + ",",)

question = input("would you like to play a game? [Y/N]")
if question == "n":
    print("oh..okey")
    if question == "y":
        print("i'm thinking of a number btn 1 and 10")
        guess = int(input("Have a guess:"))
        if guess > number:
            print("Guess lower")
            if guess < number:
                print("Guess higher")
                while guess != number:
                    tries += 1
                    guess = int(input("Try again "))
                    if guess < number:
                        print("Guess higher")
                        if guess == number:
                            print("You are right! You WIN! The number was", number, \
                                  "and it only", tries, "tries!"
                            )
