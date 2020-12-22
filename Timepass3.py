from pyclick import HumanClicker as h
from pynput.mouse import Controller as c , Button as b
from pynput.keyboard import Controller as kc , Key as ke
from time import sleep
import numpy as np
import pandas as pd
import random as r
import Sel7_1 as sel
import os
import pyautogui
c=c()
hc=h()
def tab(ch):
    al=np.random.randint(0,30)                          #Tab Changing Modules
    tab1=np.random.randint(0,220)
    tab2=np.random.randint(250,460)
    tab3=np.random.randint(490,700)
    tab4=np.random.randint(730,940)
    if ch==1:
        return [tab1,al]
    elif ch==2:
        return [tab2,al]
    elif ch==3:
        return [tab3,al]
    else:
        return [tab4,al]

def wtab(ch,s):                             #Function for Tab Clicking
    a=tab(ch)
    hc.move(a,s)
    hc.click()

def decomposition(i):                   #Time Splitting Function (Randomly Generates)
        while i > 0: 
            n = r.randint(1, i)
            yield n
            i -= n

def yeld(i,m):                          #Checking the Right Number of Splitters   
    a=[]
    while len(a)!=m:
        a=list(decomposition(i))
    return a
def pr(i,m):
    print(list(yeld(i,m)))              #Prints the yeld function


def yeld2(i,m):                          #Checking the Right Number of Splitters 2   
    a=[]
    per=i/m
    for ij in range(m):
        ak=r.uniform(per*0.86666,per*1.13333)
        a.append(ak)
    return a
def num(sec):
    seq=[]                              #Psuedo Random Generator
    ul=[]
    ab=yeld(sec,4)
    for i in range(4):
        ak=r.randint(1,4)
        seq.append(ak)
    print("Total No of Sec:",ab)
    print("Sequence:",seq)
    for i in range(4):
        au=yeld2(ab[i],seq[i])
        ul.append(au)
    print(ul)
    return ul

def svytwy(aj):
    opd,dpd=[],[]
    for i in aj:
        op=i*0.25
        dp=i*0.75
        opd.append(op)              #Splitting the Time into 25 % and 75 % Split
        dpd.append(dp)
    return opd,dpd

def sidespace(ss,s):
    ch1=r.randint(1,2)          # Side Space or Free Space Scroller 
    sel.mover(ss[ch1-1],s)
    if ch1==1:
        c.click(b.right)    
    elif ch1==2:
        c.click(b.left)

def scrlr(scrl,i,opd,dpd):         #Scroller >> Up or Down Randomly generates with svytwy(fxn)
    sel.mover(scrl,opd[i])
    c.press(b.left)
    sel.mover(scrl,dpd[i])
    c.release(b.left)

def seqq(ul):
    eq=[]
    for i in range(len(ul)):
        for j in range(len(ul[i])):     
            eq.append(i)
    r.shuffle(eq)
    return eq

def tabchgr(s):                     # Swift Tab Changer
    ch=r.randint(1,4)
    return wtab(ch,s)
def equalizer(eq):
    tl,ii=len(eq)//4,1
    for i in range(tl):
        eq.insert((i*-3)-ii,4)
        ii+=1
    return eq
lio=[]

    
def setme(ul,eq,cm5,lis,lio,name):
    s1,s3,s4=ul[0],ul[2],ul[3]
    opd,dpd=svytwy(ul[1])
    cm1,cm2,cm3,cm4=0,0,0,0
    for ch in eq:
        if ch==0:
            sidespace(ss,s1[cm1])
            cm1+=1
        elif ch==1:
            scrlr(scrl,cm2,opd,dpd)
            cm2+=1
        elif ch==2:
            sleep(s3[cm3])
            cm3+=1
        elif ch==3:
            tabchgr(s4[cm4])
            cm4+=1
        elif ch==4:
            sel.scubn()
            word=lis[cm5]
            sel.click(lio,word,name,cm5)
            cm5+=1
        else:
            print("Enter a Right Choice")

    return cm5
def opener():
    name =input("Enter the Name")
    os.chdir('C:\\Users\\hp\\Desktop\\my builderall\\Data\\'+name)
    oj=os.listdir()
    return oj


def knowitall(lio,ik,count,ikr):
    oj=opener()
    name=oj[2]
    f=open(oj[2],"r")
    lis=f.read().split("\n")
    pyautogui.FAILSAFE= False
    ao=ik
    while count<ikr:
        ok=r.randint(15,180)
        ul=num(ok)
        
        opd,dpd=svytwy(ul[1])
        eq=equalizer(seqq(ul))
        if ik==0:
            ao=setme(ul,eq,0,lis,lio,name)
            ik=ao
            count+=1
        else:
            ao=setme(ul,eq,ao,lis,lio,name)
            ik=ao
            count+=1
    return ik,count
    
# ------- The Main Results ---------------------------------------------------


ok=r.randint(15,70)
ul=num(ok)
opd,dpd=svytwy(ul[1])
eq=equalizer(seqq(ul))
ss=[[4,[0,174,180,718]],[4,[840,1340,180,718]]]
scrl=[4,[1350,1365,125,691]]
lio=[]
#setme(ul,eq)
