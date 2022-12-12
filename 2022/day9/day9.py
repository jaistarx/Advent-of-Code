file = open('input.txt', 'r')
content = file.read()
lines=content.splitlines()

col_path={'L':0,'U':-1,'R':0,'D':1}
row_path={'L':-1,'U':0,'R':1,'D':0}


def find_tail(H,T):
    col=(H[0]-T[0])
    row=(H[1]-T[1])
    if abs(row)<=1 and abs(col)<=1:
        pass
    elif abs(row)>=2 and abs(col)>=2:
        if T[0]<H[0]:
            if T[1]<H[1]:
                T=(H[0]-1,H[1]-1)
            else:
                T=(H[0]-1,H[1]+1)
        else:
            if T[1]<H[1]:
                T=(H[0]+1,H[1]-1)
            else:
                T=(H[0]+1,H[1]+1)
    elif abs(col)>=2:
        if T[0]<H[0]:
            T=(H[0]-1,H[1])
        else:
            T=(H[0]+1,H[1])
    elif abs(row)>=2:
       if T[1]<H[1]:
            T=(H[0],H[1]-1)
       else:
            T=(H[0],H[1]+1)
    return T

def part1():
    H=(0,0)
    T=(0,0)
    traversed=set()
    for line in lines:
        i1,i2=line.split(' ')
        i2=int(i2)
        for k in range(i2):
            traversed.add(T)
            H=(H[0]+col_path[i1],H[1]+row_path[i1])
            T=find_tail(H,T)
            traversed.add(T)
    print(len(traversed))
# part1()

def part2():
    H=(0,0)
    T=[(0,0) for i in range(9)]
    traversed=set()
    for line in lines:
        i1,i2=line.split(' ')
        i2=int(i2)
        for k in range(i2):
            traversed.add(T[8])
            H=(H[0]+col_path[i1],H[1]+row_path[i1])
            T[0]=find_tail(H,T[0])
            for j in range(1,9):
                T[j]=find_tail(T[j-1],T[j])
            traversed.add(T[8])
    print(len(traversed))
# part2()