file = open('input.txt', 'r')
content = file.read()
arr=content.splitlines()


def part1():
    count=0
    for i in arr:
        sarr=i.split(",")
        s1arr=sarr[0].split("-")
        s2arr=sarr[1].split("-")
        if((int(s1arr[0])<=int(s2arr[0])) and (int(s1arr[1])>=int(s2arr[1])) or (int(s2arr[0])<=int(s1arr[0])) and (int(s2arr[1])>=int(s1arr[1]))):
            count+=1
    print(count)
# part1()


def part2():
    count=0
    for i in arr:
        sarr=i.split(",")
        s1arr=sarr[0].split("-")
        s2arr=sarr[1].split("-")
        if not (int(s1arr[1])<int(s2arr[0]) or int(s2arr[1])<int(s1arr[0])):
            count+=1
    print(count)
# part2()