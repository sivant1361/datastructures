graph={
    "A":["B","C","E"],
    "B":["A","D"],
    "C":["A","D"],
    "D":["B","C","F"],
    "E":["A","F"],
    "F":["D","E"]
}

queue=[]
visited=[]

def bfs(graph,visited,node):
    queue.append(node)
    visited.append(node)
    while queue:
        s=queue.pop(0)
        if s==node:
            print("")
            print("=> ","@",s)
        elif s in graph[node]:
            print("*",s,end=" ")
        else:
            print("#",s,end=" ")
        for i in graph[s]:
            if i not in visited:
                queue.append(i)
                visited.append(i)

print("Mutual friends in connection:",end=" ")
bfs(graph,visited,"F")