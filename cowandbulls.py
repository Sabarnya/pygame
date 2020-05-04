import random
from mainmenu import *

cowsandbulls()
    words=["rate","fail","cake","sore","tear","calm","rage","time","face","swan"]
    rand=random.randrange(0,10)
    word=words[rand]
    cnt=0
    while(cnt<15):
        s=input("Enter string:")
        if s=="-1":
            print("Thank you!")
            return
        cows=0
        bulls=0
        #time mite
        chars=0
        for c in s:
            if c in word:
                chars+=1 #chars=4
        for i in range(0,4):
            if s[i]==word[i]:
                bulls+=1 #bulls=2
        cows=chars-bulls
        print("Cows:",cows,"\tBulls:",bulls)
        if bulls==4:
            print("Congragulations!You win!")
            mainmenu()
        cnt+=1
    print("Oops!Maximum guess limit reached!")
    mainmenu()