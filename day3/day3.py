file = open('input.txt', 'r')
content = file.read()
arr=content.splitlines()

res_arr=[]
final=[]

def part1():
    for i in arr:
        l=len(i)
        first = i[0:l//2]
        second=i[l//2:]
        for j in first:
            if j in second:
                res_arr.append(j)
                break
    for k in res_arr:
        if(ord(k)>=97 and ord(k)<=122):
            final.append(ord(k)-96)
        else:
            final.append(ord(k)-38)
    print(sum(final))
# part1()


def part2():
    for i in range(0,len(arr),3):
        output_set = set(arr[i]) & set(arr[i+1]) & set(arr[i+2])
        res_arr.append(output_set)
    for k in res_arr:
        if(ord(str(k)[2])>=97 and ord(str(k)[2])<=122):
            final.append(ord(str(k)[2])-96)
        else:
            final.append(ord(str(k)[2])-38)
    print(sum(final))
# part2()
