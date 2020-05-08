import time
moveCount = 0

A = []   
B = []
C = []

def showP(): #show pegs
    print("A: ",*A, sep = " ")
    print("B: ",*B, sep = " ")
    print("C: ",*C, sep = " ") 
    print("----------------------------")
    time.sleep(0.5)
    
def move(f,t): #move from f to t
    global moveCount
    t.append(f[-1])
    f.pop(-1)
    moveCount += 1
    showP()

def move1(): # move disk 1 across the "board"
    if 1 in A:
        move(A,B)
        move(B,C)
    else:
        move(C,B)
        move(B,A)    

def hanoi(n): # main function
    global A
    for x in range(n,0,-1):
        A.append(x)
        
    showP()
    
    while len(C) != n:
        move1()
        
        if A: 
            a = A[-1]
        else:
            a = n+1 # if the array for the peg is empty set its "top value" to be 1 greater than n, thus any disk can move to it.
            
        if B: 
            b = B[-1]
        else: b = n+1
        
        if C: 
            c = C[-1]
        else: c = n+1
        
        if a < b and a != 1: # not 1 as disk 1 is only moved in method move1()
            move(A,B)
        elif b < c and b != 1:
            move(B,C)
        elif c < b and c != 1:
            move(C,B)
        elif b < a and b != 1:
            move(B,A)
            
             
    print("Done in : " + str(moveCount) + " moves")

i = int(input("n = "))    
hanoi(i)
