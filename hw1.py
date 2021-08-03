import random

def printb(state):
    board= state[0]
    for x in range(9):
        print(board[x], end=' ')
        if((x+1)%3==0):
            print("")
    print("")


def printStr(s):
    # s = "[1, 2, 3...]" <- string
    b = ((s.replace(' ',''))[1:-1]).split(",")
    # b = ['1','2','3',...] <- array of strings
    printb([b,0,0])
  

def findZero(state):
    board = state[0]
    for i in range(9):
        if(board[i]==0):
            return i


def up(state):
    z = findZero(state)
    if(z>2):
        b = state[0]
        b[z], b[z-3] = b[z-3],b[z]


def down(state):
    z = findZero(state)
    if(z<6):
        b = state[0]
        b[z], b[z+3] = b[z+3],b[z]


def left(state):
    z = findZero(state)
    if(((z+1) % 3) != 1):
        b = state[0]
        b[z], b[z-1] = b[z-1],b[z]


def right(state):
    z = findZero(state)
    if( ((z+1) % 3) != 0):
        b = state[0]
        b[z], b[z+1] = b[z+1],b[z]


def hval(st):
    diff = 0
    for x in range(9):
        acc=0
        if(st[x]!=0):
            acc = abs((st[x]-1)%3 - x%3) + abs((st[x]-1)//3 - x//3)
        diff=diff+acc
    return diff


def shuffle(state):
    for _ in range(10000):
        move = random.randint(1, 4)
        if(move == 1):
            up(state)
        if(move == 2):
            down(state)
        if(move == 3):
            left(state)
        if(move == 4):
            right(state)


def copy(state):
    b=state[0]
    temp = []
    for x in range(9):
        temp.append(b[x])
    return [temp, state[1], state[2]]


def children(state):
    result = []
    
    var1 = copy(state)
    up(var1)
    if(var1[0] != state[0]):
        result.append(var1[0])
    
    var2 = copy(state)
    down(var2)
    if(var2[0] != state[0]):
        result.append(var2[0])

    var3 = copy(state)
    left(var3)
    if(var3[0] != state[0]):
        result.append(var3[0])

    var4 = copy(state)
    right(var4)
    if(var4[0] != state[0]):
        result.append(var4[0])
    
    return result


##########################################################
def solve(state):
    # 'parent' is a {string:string} dictionary that 
    # pairs each child with its parent. It is used to
    # determine wheter a node was closed or not and
    # helps to print out the solution at the end.
    parent = {}
    open = []
    open.append(state)

    while True:
        tmp = open[0]
        
        if(hval(tmp[0])==0):
            printStr("[1,2,3,4,5,6,7,8,0]")
            i=str(tmp[0])
            for _ in range(tmp[2]):
                printStr(parent[i])
                i=parent[i]

            print("Solved in", tmp[2], "steps.")
            return True

        for i in children(tmp):
            if(str(i) not in parent):
                open.append([i,hval(i),tmp[2]+1])
                parent[str(i)]=str(tmp[0])

        del open[0]

        # Sort frontier by f-value
        open.sort(key = lambda x:x[2]+x[1])    
##########################################################


def validate(state):
    inversions = 1
    arr=state[0]

    for i in range(9): 
        for j in range(i + 1, 9): 
            if (arr[i] > arr[j]): 
                inversions += 1
    
    print(inversions)
    return (inversions%2)==0
        

#########################| Main |#########################
def main():
    # INPUT:
    doShuffle = True
    start = [1,2,3,4,5,6,7,8,0]
    
    # state - [board], h-value, g-value
    state = [start, 0, 0]

    if(doShuffle):
        shuffle(state)
        solve(state)
        return 0

    if(validate(state)):
        state[1] = hval(state[0])
        solve(state)
    
    else:
        print("No solution.")
##########################################################

main()
