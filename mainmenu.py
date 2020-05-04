from rockpaperscissorsmenu import *
from cowandbullsmenu import *

def mainmenu():
    print("1.Rock Paper Scissors\n2.Cows and Bulls\n3.Exit")
    ch=int(input("Enter your choice number:"))
    if ch==1:
        rockpaperscissorsmenu()
    elif ch==2:
        cowsandbullsmenu()
    elif ch==3:
        exit()
    else:
        print("Invalid choice!")
        mainmenu()