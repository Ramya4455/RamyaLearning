import random
nump = random.randint(1000,9999)
print(nump)

n= int(input("enter a 4 digut num  "))

while n!=10:
    num=nump
    cor=0
    while num%10:
        numc=num%10
        nc=n%10
        num=num//10
        n=n//10
        if numc==nc:
            cor = cor+1
    if cor ==4:
        print("Congrats")
        break
    else:
        print("% d digits wer guessed right" %cor)
        n= int(input("Enter 4 digit num  "))
else:
    print(' you quited the game')