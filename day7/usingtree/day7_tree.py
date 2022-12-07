file = open('input.txt', 'r')
content = file.read()
arr=content.splitlines()

k=[]
class TreeNode:
    def __init__(self,data,size=0):
        self.data=data
        self.size=size
        self.children = []
        self.parent = None

    def add_child(self,child):
        self.child = child 
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0 
        p = self.parent
        while p :
            p = p.parent
            level += 1
        return level 

    def print_tree(self):
        print('  '*self.get_level() + '|--', end = '')
        print(self.data +" "+str(self.size))
        if self.children:
            for each in self.children:
                each.print_tree()

    def find_dir_sizes(self):
        if self.children:
            k.append([self.data,self.size])
            for each in self.children:
                each.find_dir_sizes()

root=TreeNode("/")
curr=root
for i in arr:
    item=i.split(" ")
    if(item[0]=="$"):
        if(item[1]=="cd"):
            if(item[2]==".."):
                curr=curr.parent
            else:
                for i in curr.children:
                    if(i.data==item[2]):
                        curr=i
        else:
            pass
    elif(item[0].isnumeric()):
        new=TreeNode(item[1],int(item[0]))
        curr.add_child(new)
        new.parent=curr
        temp=curr
        while(temp.data!="/"):
            temp.size+=int(item[0])
            temp=temp.parent
        temp.size+=int(item[0])
    elif(item[0]=="dir"):
        new=TreeNode(item[1])
        curr.add_child(new)
        new.parent=curr

def part1():
    root.print_tree()
    root.find_dir_sizes()
    total=0
    for j in k:
        if(j[1]<=100000):
            total+=j[1]
    print(total)
# part1()

def part2():
    root.print_tree()
    total_space=70000000
    required_space=30000000
    used_space=root.size
    unused_space=total_space-used_space
    root.find_dir_sizes()
    sk=sorted(k,key=lambda x:x[1])
    for j in sk:
        if(unused_space+j[1]>=required_space):
            final_space_required=j[1]
            break
    print(final_space_required)
# part2()
