

graph = {
  'Start' : ['A','B','D'],
  'A' : ['C'],
  'B' : ['D'],
  'C' : ['Goal','D'],
  'D' : ['Goal'],

}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

#while loop for the queue for visiting the nodes and then remove the same node and print it as it is visited.
  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 
#for loop to check the not visited nodes and append the same from the visited and queue list.
    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, 'Start')    # function calling
