'''1 for rock 
-1  for paper 
0 for scissors'''
import random


computer=random.choice([-1,0,1])

youstr =(input("enter your choice: "))
youdict={"r":1,"p":-1,"s":0}
reversedict={1:"rock",-1:"paper",0:"scissors"}
you =youdict[youstr]

print(f"you chose {reversedict[you]} \ncomputer chose {reversedict[computer]}")   # its a rock paper scissors game!!!


if(computer==you):
    print("its a draw game")
else:
    if(computer==1 and you==-1):
        print("you win ,congrasts")
    elif(computer==-1 and you==0):
        print("you win,congrats")
    elif(computer==0 and you==1):
        print("you win,congrats")
    elif(computer==-1 and you==1):
            print("you lose,try again next time")
    elif(computer==0 and you==-1):
            print("you lose,try again next time")
    elif(computer==1 and you==0):
            print("you lose,try again next time")
    else:
          ("something went wrong")
        
        