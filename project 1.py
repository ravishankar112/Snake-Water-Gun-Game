# We all have played snake ,water gun game in our childhood .
# if you haven 't,google the rules of this game and 
# write a python program capable of playing this game with the user


# 1 for snake 
# -1 for water
# 0 for gun

import random


computer=random.choice([-1,0,1])
youstr=input("enter your choice snake ,water ,Gun:")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:" Water",0:"Gun"}

you=youDict[youstr]

# By now we have 2 numbers (variables),you and computer

print(f"you chose {reverseDict[you]}\n computer chose {reverseDict[computer]}")

if(computer==you):
    print("its a drow!")
    
else:
    if(computer==-1 and you==1):
        print("you win!")
    
    elif(computer==-1 and you==0):
          print("you Lose!")
    
    elif(computer==1 and you==-1):
         print("you Lose!")

    elif(computer==1 and you==0):
         print("you Win!")

    elif(computer==0 and you==1):
        print("you Lose!")

    elif(computer==0 and you==-1):
        print("you win!")
     
    else:
        print("something is wrong !") 