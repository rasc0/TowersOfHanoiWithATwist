import time
moveCount = 0

A = []   
B = []
C = []

def showP():
    print("A: ",*A, sep = " ")
    print("B: ",*B, sep = " ")
    print("C: ",*C, sep = " ") 
    print("----------------------------")
    time.sleep(0.5)
    
def move(f,t):
    global moveCount
    t.append(f[-1])
    f.pop(-1)
    moveCount += 1
    showP()

def move1():
    if 1 in A:
        move(A,B)
        move(B,C)
    else:
        move(C,B)
        move(B,A)    

def hanoi(n): 
    global A
    for x in range(n,0,-1):
        A.append(x)
        
    showP()
    
    while len(C) != n:
        move1()
        
        if A: 
            a = A[-1]
        else:
            a = n+1
            
        if B: 
            b = B[-1]
        else: b = n+1
        
        if C: 
            c = C[-1]
        else: c = n+1
        
        if a < b and a != 1:
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
