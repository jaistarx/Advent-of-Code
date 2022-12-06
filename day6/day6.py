file = open('input.txt', 'r')
content = file.read()
arr=content.splitlines()

arr=arr[0]

from collections import Counter

def part1():
    i=0
    j=4
    while(j<len(arr)):
        r=arr[i:j]
        freq = Counter(r)
        if(len(freq) == 4):
            break
        i+=1
        j+=1
    print(j)
# part1()




def part2():
    i=0
    j=14
    while(j<len(arr)):
        r=arr[i:j]
        freq = Counter(r)
        if(len(freq) == 14):
            break
        i+=1
        j+=1
    print(j)
# part2()