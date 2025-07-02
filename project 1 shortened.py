import random

computer=random.choice([-1,0,1])
youstr=input("enter your choice snake ,water ,Gun:")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:" Water",0:"Gun"}

you=youDict[youstr]

if(computer==you):
    print("it's a drow!")

else:
    if((computer-you)==-1 or (computer-you)==2):
        print("you Lose!")
    else:
        print("you win!")