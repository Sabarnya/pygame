#function to welcome the user in the gaming page
def welcome():
    #enter the first line of the welcome page with stars
    for i in range(0,15):
        print("*\t",end="")
    print()
    #loops to print first star and blank tabs
    for k in range(0,2):
        print("*",end="")
        for i in range(0,14):
            print("\t",end="")
        print("*\n",end="")
    print("*",end="")
    #type the welcome statement after some tabs
    for i in range(0,7):
        print("\t",end="")
    print("WELCOME",end="")
    for i in range(0,7):
        print("\t",end="")
    print("*")
    #printing the bottom part with star and tabs
    for k in range(0,2):
        print("*",end="")
        for i in range(0,14):
            print("\t",end="")
        print("*\n",end="")
    #printing the last line with stars
    for i in range(0,15):
        print("*\t",end="")
    print()
    input("Press any key to start:") 

#function call to print the welcome screen
print(welcome())
import os
import click
key = click.getchar()
if(key!=null):
    os.system('cls')