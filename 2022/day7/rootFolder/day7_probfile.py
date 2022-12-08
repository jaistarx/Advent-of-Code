import os

def get_size(start_path = '.'):
    total_size = 0
    k=[]
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in dirnames:
            fp = os.path.join(dirpath, f)
            fsize=get_all_size(fp)
            k.append(fsize)
    return k

def get_all_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return (total_size)//1024


def part1():
    total_size=0
    size_arr=get_size()
    for j in size_arr:
        if(j<=100000):
            total_size+=j
    print(total_size)
# part1()

def part2():
    fullsize=get_all_size()

    available= 70000000
    needed   = 30000000

    unused=available-fullsize

    l=get_size()
    gg=[]
    for s in sorted(l):
        if(unused+s>=needed):
            gg.append(s)
    print(min(gg))
# part2()