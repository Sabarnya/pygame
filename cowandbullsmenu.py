from cowandbulls import *
from mainmenu import *

def cowsandbullsmenu():
    print("1.Play\n2.Rules\n3.Return to Main menu")
    ch = int(input("Enter your choice number:"))
    if ch == 1:
        cowsandbulls()
    elif ch == 2:
        cowsandbullsrules()
    elif ch == 3:
        mainmenu()
    else:
        print("Invalid choice!")
        cowsandbullsmenu()