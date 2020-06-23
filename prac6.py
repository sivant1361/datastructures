graph={
    "A":["B","C"],
    "B":["A","D","E"],
    "C":["A","F"],
    "D":["B"],
    "E":["B","F"],
    "F":["C","E"]
}


visited=[]

def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

print("Depth First Search: ",end=" ")
dfs(visited,graph,"F")