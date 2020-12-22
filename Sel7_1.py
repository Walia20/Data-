
# Sel 7.1 have difff saving mechanism than Sel 7
# Different location for Go Execution




from pynput.mouse import Button as b, Controller as c
from pynput.keyboard import Key as ke, Controller as kc
from pyclick import HumanClicker as h
from copypaste import paste
from time import sleep
import random as r
from pyp3rclip import paste as p
from keyboard import press_and_release as pr
import pandas as pd
import numpy as np
c=c()
k=kc()
hc=h()
lio=[]
sel=[[1,[160,175,242]],[1,[760,780,767]]]#Selector Range
ser=[[3,[180,720,130,160]],[3,[808,841,128,164]]] #Search Bar and Search Button
srup=[[1,[1350,1365,691]],[1,[1350,1360,125]]]

def rgen(i,ab):
    if i==1:                    #Left Random Gen
        pos1=r.randint(ab[0],ab[1])
        pos=(pos1,ab[-1])
    elif i==2:
        pos1=r.randint(ab[1],ab[2])  # Right Random  Gen
        pos=(ab[0],pos1)
    else:
        pos1=r.randint(ab[0],ab[1])         #Both Side Generator
        pos2=r.randint(ab[2],ab[3])
        pos=(pos1,pos2)

    return pos
def keygen():
    k.press(ke.ctrl)
    k.press("a")
    k.release(ke.ctrl)
    k.release("a")
def go(cm5):
    k.press(ke.ctrl)
    k.press("s")
    k.release("s")
    k.release(ke.ctrl)
  #  hc.move((382, 376),1)
    hc.move((564, 504),1)
    hc.click()
    keygen()
    k.type(str(cm5))
    #hc.click()
    #k.press(ke.backspace)
    #k.release(ke.backspace)
    
    #sleep(1)
   # hc.move((516, 452),1)
    hc.move((697, 574),1)
    hc.click()
def mover(selo,s):                          #Generates a Random Movement Phase
	i=selo[0]                           # Seach with [1,[fgnjfg,gngirjg,ifjggk]]  for left random  >>> Selo
	ab=selo[1]                          # s = Seconds
	aol=rgen(i,ab)
	hc.move(aol,s)
def click(lio,word,name,cm5):
    searcher(word)
    mover(sel[0],1)
    c.press(b.left)
    mover(sel[1],3)
    sleep(6)
    c.release(b.left)
    hc.move((1001, 479),1)
    c.click(b.right)
    sleep(1)
    c.move(10,10)
    c.click(b.left)
    lio.append(p())
    go(cm5)
    repeater(lio,name)
    go(str(cm5)+"b")
    
#click()
word="\"bussiness\""
def searcher(word):
    mover(ser[0],1)             #Moves and Seaches the Word in the Clicker
    hc.click()
    k.press(ke.ctrl)
    k.press("a")
    k.release(ke.ctrl)
    k.release("a")
    k.press(ke.backspace)
    k.release(ke.backspace)
    k.type(word)
    mover(ser[1],1)
    hc.click()
    
    
def scrup():
    mover(srup[0],1)
    c.press(b.left)
    mover(srup[1],2)            #Scroller to up (for last)
    sleep(0.5)
    c.release(b.left)
    
def scrdwn():
    mover(srup[1],1)
    c.press(b.left)
    mover(srup[0],2)            #Scroller to Down (for next new)
    c.release(b.left)

def pgchange(s):
    pgch=[4,[490,569,585,593]]
    mover(pgch,s)
    hc.click()

def repeater(lio,name):
    pgchange(0.5)
    mover(sel[0],1)
    c.press(b.left)
    mover(sel[1],3)
    sleep(6)
    c.release(b.left)
    hc.move((1001, 479),0.6)
    c.click(b.right)
    sleep(1)
    c.move(10,10)
    c.click(b.left)
    lio.append(p())
    saver(lio,name)
    
def creator(name):
    li=[]
    aj=pd.Series(li)
    aj.to_csv(str(name)+".csv")
    return aj
def saver(lio,name):
    lio.append(p())
    aj=creator(name)
    a=pd.Series(lio)
    
    a.to_csv(str(name)+".csv")
    return a
def scubn():
    hc.move((1356, 121),0.20)
    c.press(b.left)
    sleep(3)
    c.release(b.left)

