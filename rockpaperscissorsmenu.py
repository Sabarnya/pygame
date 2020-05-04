from rockpaperscissor import *
from mainmenu import *

rockpaperscissorsmenu(){
    print("1.Play\n2.Rules\n3.Return to Main menu")
    ch = int(input("Enter your choice number:"))
    if ch == 1:
        rockpaperscissors()
    elif ch == 2:
        rockpaperscissorsrules()
    elif ch == 3:
        mainmenu()
    else:
        print("Invalid choice!")
        rockpaperscissorsmenu()}