import random as random

print("\n")
print("Rock = r\nPaper = p\nScissors = s")

while True:
    print("\n")
    
    inp = input("Rock, paper, scissors, SHOOT ")
    if(inp == "exit"):
        exit()
    
    comp = random.choice(["r","p","s"])
    print(f"Computer {comp}")
      
    if(inp == comp ):
        print("draw")
        continue

    if(inp == "r" and comp == "s" or
            inp == "p" and comp == "r" or
            inp == "s" and comp == "p"):
        print("you win")
        continue
    else:
        print("you lose")
        continue

