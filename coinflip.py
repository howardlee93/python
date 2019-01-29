#lab3-1  
import random

def FlipCoin():
    #toss = random.randint(0,1)
    if random.randint(0,1) == 0:
        return "tails"
    return "heads"

def main(num):
    heads = 0
    for i in range(num):
        if FlipCoin() == "heads":
            heads += 1
    print("With %d flips, 'heads' came up %d times, or " % (num,heads),end="")
    print("%.f%% of the flips." % ((heads *100)/num))


if __name__ == "__main__":
    main(100)

    

