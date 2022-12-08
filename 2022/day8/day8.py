file = open('input.txt', 'r')
content = file.read()
arr=content.splitlines()

def part1():
    visible=0
    visited=[]
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[i])-1):
            item=int(arr[i][j])
            rw=arr[i]

            row=[]
            for z in rw:
                row.append(int(z))
            leftrow=row[0:j]
            leftrow=leftrow[::-1]
            rightrow=row[j+1:]

            if(item>max(leftrow) or item>max(rightrow)):
                if(str([i,j]) not in visited):
                    visible+=1
                    visited.append(str([i,j]))
            
            column=[]
            for c in range(len(arr)):
                column.append(int(arr[c][j]))
            topcolumn=column[0:i]
            bottomcolumn=column[i+1:]

            if(item>max(topcolumn) or item>max(bottomcolumn)):
                if(str([i,j]) not in visited):
                    visible+=1
                    visited.append(str([i,j]))
    border=392
    print(border+visible)
# part1()

def part2():
    leftscene=0
    rightscene=0
    topscene=0
    bottomscene=0
    scene=0
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[i])-1):
            item=int(arr[i][j])
            rw=arr[i]

            row=[]
            for r in rw:
                row.append(int(r))
            leftrow=row[0:j]
            leftrow=leftrow[::-1]
            rightrow=row[j+1:]

            for s in leftrow:
                if(s<item):
                    leftscene+=1
                else:
                    leftscene+=1
                    break
            for s in rightrow:
                if(s<item):
                    rightscene+=1
                else:
                    rightscene+=1
                    break

            column=[]
            for k in range(len(arr)):
                column.append(int(arr[k][j]))
            topcolumn=column[0:i]
            topcolumn=topcolumn[::-1]
            bottomcolumn=column[i+1:]

            for s in topcolumn:
                if(s<item):
                    topscene+=1
                else:
                    topscene+=1
                    break
            for s in bottomcolumn:
                if(s<item):
                    bottomscene+=1
                else:
                    bottomscene+=1
                    break
            scene_of_item=leftscene*rightscene*bottomscene*topscene
            if(scene_of_item>scene):
                scene=scene_of_item
            leftscene=0
            rightscene=0
            bottomscene=0
            topscene=0
    print(scene)
# part2()