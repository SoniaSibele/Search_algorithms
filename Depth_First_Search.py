# Using a Python dictionary to act as an adjacency list
#neighbour = 0
graph = {
  'Start' : ['A','B','D'],
  'A' : ['C'],
  'B' : ['D'],
  'C' : ['Goal','D'],
  'D' : ['Goal'],

}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited: #check whether any node of the graph is visited or not
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, 'Start')
