import random
from mainmenu import *

rockpaperscissors()
    print("WELCOME TO ROCK PAPER AND SCISSORS")
    print("You will be competing against the computer. The player that scores 5 points first, will be declared as the winner!")
    print("If your choice is Rock,please Enter 0")
    print("If your choice is Paper,please Enter 1")
    print("If your choice is Scissors,please Enter 2")
    print("If you wish to exit,please Enter -1")
    user=0
    comp=0
    cnt=0
    chc=["Rock","Paper","Scissors"]
    while(user<5 and comp<5 and cnt<25):
        cnt+=1
        u_ch=int(input("Enter your choice:"))
        if u_ch==-1:
            print("Thank you")
            return
        c_ch=random.choice([0,1,2])
        if u_ch==0 and c_ch==1:
            comp+=1
        elif u_ch==0 and c_ch==2:
            user+=1
        elif u_ch==1 and c_ch==0:
            user+=1
        elif u_ch==1 and c_ch==2:
            comp+=1
        elif u_ch==2 and c_ch==0:
            comp+=1
        elif u_ch==2 and c_ch==1:
            user+=1
        print("You:",chc[u_ch])
        print("Computer",chc[c_ch])
        print("Your score:",user,"\t Computer's Score:",comp)
    if(user>comp):
        print("Congragulations!You win!")
    elif(comp>user):
        print("Oops!Sorry you lose. Better luck next time!")
    else:
        print("Match Draw")
    mainmenu()

rockpaperscissorsrules()
    print("Although the game has a lot of complexity to it, the rules to play it are pretty simple.\n")
    print("The game is played where players deliver hand signals that will represent the elements of the game;\n rock, paper and scissors. The outcome of the game is determined by 3 simple rules:\n\n")
    print("Rock wins against scissors.\nScissors win against paper.\nPaper wins against rock.")
    mainmenu()