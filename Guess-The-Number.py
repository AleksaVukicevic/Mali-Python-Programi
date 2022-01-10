import random as random

def run():
    print("\n")
    print("Guess the number 0-100")
    br = random.randint(0,100)
    inp = int(input("What about "))

    while inp != br:
        if(br > inp):
            print("Larger")
        else:
            print("Smaller")
        inp = int(input("What about "))

    print("Correct")

    if input("Play again?(y/n) ") == "y":
       run()
    else:
        quit()  

run()
