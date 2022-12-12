file = open('input.txt', 'r')
content = file.read()
arr=content.split("\n")

class Graph:
    
    graph_dict={}
    
    def addEdge(self,node,neighbour):  
        if node not in self.graph_dict:
            self.graph_dict[node]=[neighbour]
        else:
            self.graph_dict[node].append(neighbour)
            
    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print(node,"->",neighbour)
    
    def show_graph(self):
        return self.graph_dict


def BFS_SP(graph, start, goal):
    explored = []
     
    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]
     
    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return
     
    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
        # if(node not in graph.keys()):
        #     node=path[-2]
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            if node in graph.keys():
                neighbours = graph[node]
            else:
                neighbours = []
            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                 
                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    print("path",start,"->",goal)
                    return new_path
            explored.append(node)
 
    # Condition when the nodes
    # are not connected
    print("path doesn't exist",start,"->",goal)
    return
    

g= Graph()


for i in range(len(arr)):
    for j in range(len(arr[i])):
        if(arr[i][j]=="S"):
            start=(i,j,'a')
            arr[i]=arr[i].replace("S","a")
        elif(arr[i][j]=="E"):
            end=(i,j,'z')
            arr[i]=arr[i].replace("E","z")

for i in range(len(arr)):
    for j in range(len(arr[i])):
        item=(i,j,arr[i][j])
        if((i-1)>=0):
            if((ord(arr[i][j])+1) >= ord(arr[i-1][j])):
                top=(i-1,j,arr[i-1][j])
                g.addEdge(str(item),str(top))
        if((j-1)>=0):
            if((ord(arr[i][j])+1) >= ord(arr[i][j-1])):
                left=(i,j-1,arr[i][j-1])
                g.addEdge(str(item),str(left))
        if((i+1)<len(arr)):
            if((ord(arr[i][j])+1) >= ord(arr[i+1][j])):
                bottom=(i+1,j,arr[i+1][j])
                g.addEdge(str(item),str(bottom))
        if((j+1)<len(arr[i])):
            if((ord(arr[i][j])+1) >= ord(arr[i][j+1])):
                right=(i,j+1,arr[i][j+1])
                g.addEdge(str(item),str(right))



def part1():
    # g.show_edges()
    # print(arr)
    graph=g.show_graph()
    # print(graph)
    spath=BFS_SP(graph, str(start), str(end))
    print(len(spath)-1)
part1()

def part2():
    graph=g.show_graph()
    path_a=[]
    for i in graph.keys():
        if(i[-3]=="a"):
            spath=BFS_SP(graph, i, str(end))
            if(spath):
                path_a.append(len(spath)-1)
    print(min(path_a))
# part2()