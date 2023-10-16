import random
l=["rock","paper","scissors"]
c=random.choice(l)
u=input("enter your choice")
print(c)
if c=="paper" and u=="rock":
    print ("you win")
elif c=="rock" and u=="paper":
    print ("computer is the winner")
elif c=="scissors" and u=="paper":
    print ("computer is the winner")
elif c=="paper" and u=="scissors":
    print ("you win")
elif c=="scissors" and u=="rock":
    print ("you win")
elif c=="rock"and u=="scissors":
    print ("computer is the winner")
else:
    print("invalid input")