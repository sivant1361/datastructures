graph={
    "A":["B","C"],
    "B":["D","E"],
    "C":["F"],
    "D":[],
    "E":["F"],
    "F":[]
}

visited=[]

def dfs(visited,graph,node):
    print(node,end=" ")
    visited.append(node)
    for neighbour in graph[node]:
        dfs(visited,graph,neighbour)
    

dfs(visited,graph,"B")