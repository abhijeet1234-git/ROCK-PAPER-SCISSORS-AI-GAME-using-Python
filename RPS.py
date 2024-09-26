# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 13:41:09 2020

@author: user
"""
import random as r 
import sys as s 
import pyttsx3 as pt 
import datetime as dt 
speech_engine=pt.init("sapi5") # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty("rate",200) 

#class RPSgame: 
def Menu(): 
    year=(dt.datetime.now().year) 
    month=(dt.datetime.now().month) 
    date=(dt.datetime.now().day) 
    Time=dt.datetime.now().strftime("%I-%M-%S") 
    print("\n                    DATE : ",end="") 
    print(date,month,year,sep="/",end="               ") 
    print("TIME : "+Time) 
    print("                    ############################################## ") 
    print("                    #    WELCOME TO ROCK-PAPER-SCISSORS GAME     # ") 
    print("                    ############################################## ") 
    print("                    #  R:ROCK , P:PAPER , S:SCISSORS cheat code  # ") 
    print("                    ############################################## ") 
    print("                    #                   MENU                     # ") 
    print("                    ############################################## ") 
    print("                    # OPTIONS :                                  # ") 
    print("                    #  1) 2 PLAYERS                              # ") 
    print("                    #  2) HUMAN VS COMPUTER                      # ") 
    print("                    #  3) EXIT                                   # ") 
    print("                    ############################################## ") 
Menu() 

def Speak(text): 
    speech_engine.say(text) 
    speech_engine.runAndWait() 
    
def Choice(): 
    ch=int(input("Enter your choice(1-3) : ")) 
    return(ch) 

c=Choice() 
def score_board(P,s1,s2): 
    if(P!=""): 
        print("Winner is {} ".format(P)) 
        print("SCORE : {0} - {1} ".format(s1,s2)) 
        Speak("Winner is {}".format(P)) 
        Speak("SCORE  {0} to {1} ".format(s1,s2)) 
    else: 
        print("Winner is COMPUTER ") 
        print("SCORE : {0} - {1} ".format(s2,s1)) 
        Speak("Winner is computer ") 
        Speak("SCORE  {0} to {1} ".format(s2,s1)) 

def score(p1,p2,s1,s2): 
    if((s1>s2) and (p1!="")): 
            score_board(p1,s1,s2) 
    elif((s1<s2) and (p2!="")): 
            score_board(p2,s2,s1) 
    elif((s1==s2) and (p1!="" or p2!="")): 
            print("\nTIE ") 
            print("SCORE : {0} - {1} ".format(s1,s2)) 
            Speak("SCORE  {0} to {1} ".format(s2,s1)) 
            Speak("It's draw ") 
    else: 
            score_board(p2,s2,s1) 

def opt(ch): 
    d={} 
    d["R"],d["P"],d["S"]="ROCK","PAPER","SCISSORS" 
    d1,d2={},{} 
    if(ch==1): 
        P1=input("Player 1 enter your name : ") 
        P2=input("Player 2 enter your name : ") 
        print("\nPlayer 1 enter the secret code(cheat code) : ") 
        d1[1]=input("1st code : ") 
        d1[2]=input("2nd code : ") 
        d1[3]=input("3rd code : ") 
        i,count=0,3 
        print("\nPlayer 2 enter the secret code(cheat code) : ") 
        d2[1]=input("1st code : ") 
        d2[2]=input("2nd code : ") 
        d2[3]=input("3rd code : ") 
        s1,s2=0,0 
        print("---------------------------------------------") 
        while(count!=0): 
                print("\nRound {} ".format(i+1)) 
                ch1=int(input("Player1 enter the code : ")) 
                ch2=int(input("Player2 enter the code : ")) 
                p1=d1[ch1] 
                q1=d2[ch2] 
                if((d1[ch1]==d2[ch2]=="R") or (d1[ch1]==d2[ch2]=="P") or (d1[ch1]==d2[ch2]=="S")): 
                    print("Draw\n ") 
                    print("{0}=={1} ".format(d[p1],d[q1])) 
                else: 
                    if(((d1[ch1]=="R") and (d2[ch2]=="S")) or ((d1[ch1]=="S") and (d2[ch2]=="P")) or ((d1[ch1]=="P") and (d2[ch2]=="R"))): 
                        print("Player1 Won\n ") 
                        print("{0}>>{1} ".format(d[p1],d[q1])) 
                        s1+=1 
                    else: 
                        print("Player2 won\n ") 
                        print("{0}<<{1} ".format(d[p1],d[q1])) 
                        s2+=1 
                print("--------------------------------------------") 
                count-=1 
                i+=1 
        score(P1,P2,s1,s2)    
    elif(ch==2): 
        P1,P2=input("Player 1 enter your name : "),"" 
        print("\nPlayer 1 enter the secret code(cheat code) : ") 
        d1[1]=input("1st code : ") 
        d1[2]=input("2nd code : ") 
        d1[3]=input("3rd code : ") 
        i,count=0,3 
        d2[1]="R" 
        d2[2]="P" 
        d2[3]="S" 
        s1,s2=0,0  
        print("--------------------------------------------- ") 
        while(count!=0): 
            print("\nRound {} ".format(i+1)) 
            ch1=int(input("Player1 enter the code : ")) 
            ch2=r.choice([1,2,3]) 
            print("Player2 enter the code : {} ".format(ch2)) 
            p2=d1[ch1] 
            q2=d2[ch2] 
            if((d1[ch1]==d2[ch2]=="R") or (d1[ch1]==d2[ch2]=="P") or (d1[ch1]==d2[ch2]=="S")): 
                print("Draw\n ") 
                print("{0}=={1} ".format(d[p2],d[q2])) 
            else: 
                if(((d1[ch1]=="R") and (d2[ch2]=="S")) or ((d1[ch1]=="S") and (d2[ch2]=="P")) or ((d1[ch1]=="P") and (d2[ch2]=="R"))): 
                    print("Player1 Won\n ") 
                    print("{0}>>{1} ".format(d[p2],d[q2])) 
                    s1+=1 
                else: 
                    print("Computer won\n ") 
                    print("{0}<<{1} ".format(d[p2],d[q2])) 
                    s2+=1 
            print("-------------------------------------------- ") 
            count-=1 
            i+=1 
        score(P1,P2,s1,s2) 
    elif(ch==3): 
        print("EXITED THE GAME ") 
        s.exit() 
    else: 
        print("Wrong choice!!!! ") 
opt(c) 
while(True): 
    p=input("Do U want anymore (Press Y to continue or N to stop)? : ") 
    if((p=="y") or (p=="Y")): 
        n=int(input("Enter your choice again(1-3) : ")) 
        opt(n) 
    elif((p=="n") or (p=="N")): 
        Speak("Thank you for playing ") 
        break 
    else: 
        print("\nPlease try to enter Y/N correctly : ") 
print("\n<--                                    THANK YOU                                              --> ") 
#RPSgame() 
