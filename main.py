import random

p=random.randint(1,100)
print(p)
choice=input("enter level:easy or hard")
t=0
if(choice=="easy"):
    t=10
elif(choice=="hard"):
    t=5

i=1
l=0
j=0
while(i<=t):
    n=input("enter a number to guess")
    if(int(n)==p):
        l=1
        print("right guess")
        break
    elif(int(n)<p):
        print("too low")
    else:
        print("too high")
    j=t-i
    if j!=0:
        print("you have",j,"guesses left")

    i+=1
if l==0:
    print("you have run out of guesses")