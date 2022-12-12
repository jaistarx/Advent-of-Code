file = open('input.txt', 'r')
content = file.read()
arr=content.splitlines()


def part1():
    # X=0
    # step=0
    # i=0
    # cyclesum=0
    # while(i<len(arr)):
    #     if(arr[i]=="noop"):
    #         step+=1
    #         if(step in {20,60,100,140,180,220}):
    #             cyclesum+=X
    #     elif(arr[i][0:4]=="addx"):
    #         s1,s2=arr[i].split(" ")
    #         X+=int(s2)
    #         step+=1
    #         if(step in {20,60,100,140,180,220}):
    #             cyclesum+=X
    #         step+=1
    #         if(step in {20,60,100,140,180,220}):
    #             cyclesum+=X
    #     i+=1
    # print(cyclesum)
    ans=0
    x=1
    cycle=0
    for i in arr:
        w=i.split()
        if(w[0]=="noop"):
            cycle+=1
            if(cycle in {20,60,100,140,180,220}):
                ans+=x*cycle
        elif(w[0]=="addx"):
            cycle+=1
            if(cycle in {20,60,100,140,180,220}):
                ans+=x*cycle
            cycle+=1
            if(cycle in {20,60,100,140,180,220}):
                ans+=x*cycle
            x+=int(w[1])
    print(ans)
# part1()
 

def part2():
    crt=[]
    lst=[]
    for i in range(6):
        for j in range(40):
            lst.append(".")
        crt.append(lst)
        lst=[]
    sprite=["." for j in range(40)]
    # for i in crt:
    #     print(''.join(i))
    sprite[0]=sprite[1]=sprite[2]="#"
    # print(''.join(sprite))
    ans=0
    x=1
    cycle=0
    for i in arr:
        w=i.split()
        if(w[0]=="noop"):
            cycle+=1
            if(cycle in {20,60,100,140,180,220}):
                ans+=x*cycle
        elif(w[0]=="addx"):
            cycle+=1
            if(cycle in {20,60,100,140,180,220}):
                ans+=x*cycle
            cycle+=1
            if(cycle in {20,60,100,140,180,220}):
                ans+=x*cycle
            x+=int(w[1])
            k=0
            while(k<len(sprite)):
                if(k==x):
                    sprite[k]="#"
                    sprite[k-1]="#"
                    sprite[k+1]="#"
                    k+=1
                else:
                    sprite[k]="."
                k+=1
            print(''.join(sprite))   
# part2()