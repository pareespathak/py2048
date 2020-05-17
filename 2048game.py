from numpy import *
from random import *
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--p", type=int,help="enter board size")
parser.add_argument("--w", type=int,help="enter winvalue")
args = parser.parse_args()
# ===============================================initial stage ===================================================
n=args.p
w=args.w
if args.p == None or args.p ==0:
    n=5
if args.w==None or args.w ==1:
    w=2048
t=math.log(w,2)
if t-int(t) ==0:
    winvalue=w
else:
    winvalue=2048
board=zeros((n,n))
#==========================================inserting tile==================================================
def inserting_tile():
    b=randint(0,n-1)
    a=randint(0,n-1)
    if board[a][b]==0:
        board[a][b]=2
    else :
        inserting_tile()
#==== =============================================leftmove function===================================================
def leftmove():
    def left(i,j):
        while i<n and j<n-1:
            if board[i][j]==0:
                board[i][j]=board[i][j+1]
                board[i][j+1]=0
                left(i,j+1)
            else:
                left(i,j+1)
            i=i+1
    def addleft():
        for i in range(0,n):
            for j in range(0,n-1):
                if board[i][j]==board[i][j+1]:
                    board[i][j]=board[i][j+1]+board[i][j]
                    board[i][j+1]=0
    for i in range(0,n):
        left(0,0)
    addleft()
    for i in range(0,n):
        left(0,0)
# ====================================================rightmove function=============================================
def rightmove():
    def right(i,j):
        while j>0 and i<n:
            if board[i][j]==0:
                board[i][j]=board[i][j-1]
                board[i][j-1]=0
                right(i,j-1)
            else:
                right(i,j-1)
            i=i+1

    def addright(i,j):
        while j>0 and i<n:
            if board[i][j]==board[i][j-1]:
                temp=board[i][j]+board[i][j-1]
                board[i][j]=temp
                board[i][j-1]=0
                addright(i,j-2)
            else:
                addright(i,j-1)
            i=i+1
    for i in range(0,n):
        right(0,n-1)
    addright(0,n-1)
    for i in range(0,n):
        right(0,n-1)
# =================================================moveup function=================================================
def moveup():
    def up(i,j):
        while i<n-1 and j<n:
            if board[i][j]==0:
                board[i][j]=board[i+1][j]
                board[i+1][j]=0
                up(i+1,j)
            else:
                up(i+1,j)
            j=j+1
    for i in range(0,n):
        up(0,0)            
    for row in range(0,n-1):
        for col in range(0,n):
            if board[row][col]==board[row+1][col]:
                temp=board[row][col]+board[row+1][col]
                board[row][col]=temp
                board[row+1][col]=0
    for i in range(0,n):
        up(0,0)
# ================================================movedown function==================================================
def movedown():
    def down(i,j):
        while i>0 and j<n:
            if board[i][j]==0:
                board[i][j]=board[i-1][j]
                board[i-1][j]=0
                down(i-1,j)
            else:
                down(i-1,j)
            j=j+1

    def adddown(i,j):
        while i>0 and j<n:
            if board[i][j]==board[i-1][j]:
                temp=board[i][j]+board[i-1][j]
                board[i][j]=temp
                board[i-1][j]=0
                adddown(i,j+1)
            else:
                adddown(i,j+1)
            i=i-1
    for i in range(0,n):
        down(n-1,0) 
    adddown(n-1,0)
    for i in range(0,n):
        down(n-1,0)
#===============================================play_move()===========================
def play_move():
    key=input("enter move w/s/d/a \n")
    if key=='w' or key=='W':
        moveup()
    elif key=='a' or key=='A':
        leftmove()
    elif key=='d' or key=='D':
        rightmove()
    elif key=='s' or key=='S':
        movedown() 
    else:
        print("invalid move","\n play again")
        play_move()
#===============================printing board=============================
def printing():
    for i in range(0,n):
            for j in range(0,n):
                print(int(board[i][j]),end=" ")
            print("")
#============================================clear screen======================================
def clear():
    if os.name=='nt':
        _=os.system('cls')
    else:
        _=os.system('clear')
#===============================================main code=======================================
inserting_tile()
status=True
while status==True:
    status=False
    for i in range(0,n):
        for j in range(0,n-1):
            if board[i][j]==board[i][j+1]:
                status=True
    for i in range(0,n-1):
        for j in range(0,n):
            if board[i][j]==board[i+1][j]:
                status=True
    if board.all()==False:
        status=True
    if status==False:
        clear()
        if n==1 and winvalue==2:
            print("u won the game")
            printing()
        else:
            printing()
            print("game over,u lost")
            print("winvalue was =",winvalue)
            break
    for i in range(0,n):
        for j in range(0,n):
            if board[i][j]==winvalue:
                status=False
                clear()
                printing()
                print("you won","\n new game")
                break
    if status==True:
        a=board.copy()
        clear()
        print("play game")
        print("winvalue=",winvalue)
        print("to quit game press clt+c")
        printing()
        play_move()
        b=board
        c=a-b
        if c.any()==True:
            inserting_tile()
