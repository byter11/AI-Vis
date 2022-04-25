def bfs(adjList, start):
  path = []
  q = [start]

  while q:
    m = q.pop(0) 
    path.append(m)
    
    # if m == goal:
    #   return path
      
    for node in adjList.get(m, []):
      if node not in path:
        q.append(node)


  return path