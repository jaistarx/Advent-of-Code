file = open('input.txt', 'r')
content = file.read()
arr=content.splitlines()

cfile = open('crate.txt', 'r')
ccontent = cfile.read()
stackarr=ccontent.splitlines()

movearr=[]
for i in arr:
    c=i.split(' ')
    movearr.append(c)

for j in movearr:
    j.pop(4)
    j.pop(2)
    j.pop(0)
    for k in range(len(j)):
        j[k]=int(j[k])


def part1():
    for i in movearr:
        beforearr=stackarr[(i[1]-1)]
        afterarr=stackarr[(i[2]-1)]
        movingnumber=i[0]
        for x in range(0,movingnumber):
            item=beforearr[-1]
            beforearr = beforearr[:-1]
            afterarr=afterarr+item
            stackarr[(i[1]-1)]=beforearr
            stackarr[(i[2]-1)]=afterarr
    print(stackarr)
# part1()


def part2():
    for i in movearr:
        beforearr=stackarr[(i[1]-1)]
        afterarr=stackarr[(i[2]-1)]
        movingnumber=i[0]
        item=beforearr[-movingnumber:]
        beforearr = beforearr[:-movingnumber]
        afterarr=afterarr+item
        stackarr[(i[1]-1)]=beforearr
        stackarr[(i[2]-1)]=afterarr
    print(stackarr)
# part2()