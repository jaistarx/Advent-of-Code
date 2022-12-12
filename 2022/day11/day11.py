file = open('input.txt', 'r')
content = file.read()
arr=content.split("\n")
d={}

newarr=[]
s=[]
for i in range(len(arr)):
    if(arr[i]==''):
        newarr.append(s)
    elif(arr[i][0:3]=="new"):
        s.append(arr[i])
    elif(arr[i].isnumeric()):
        arr[i]=int(arr[i])
        s.append(arr[i])
    else:
        n=arr[i].split(",")
        for j in range(len(n)):
            n[j]=int(n[j])
        s.append(n)
arr=[]
for i in range(0,len(newarr[0]),6):
    arr.append(newarr[0][i:i+6])

d={}

for i in range(len(arr)):
    d[arr[i][0]]=arr[i][1:]

def part1():
    for i in range(20):
        for j in range(len(d)):
            # for k in range(len(d[j][0])):
                print(d[j][0])
part1()