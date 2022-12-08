import os

file = open('input.txt', 'r')
content = file.read()
arr=content.splitlines()

arr.pop(0)

for i in range(len(arr)):
    item=arr[i].split(" ")
    if(item[0]=="$" and item[1]=="ls"):
        arr[i]=""
    elif(item[0]=="$" and item[1]=="cd"):
        arr[i]=" ".join(item[1:])
    elif(item[0]=="dir"):
        item[0]="mkdir"
        arr[i]=" ".join(item)
    else:
        if(item[0].isnumeric()):
            temp=int(item[0])*1024
            item[0]="fsutil file createnew "+item[1]
            item[1]=str(temp)
            j=" ".join(item)
            arr[i]=j
os.makedirs("rootFolder")
with open('./rootFolder/modifiedfile.cmd', 'w') as f:
    for line in arr:
        if(line!=""):
            f.write(f"{line}\n")

