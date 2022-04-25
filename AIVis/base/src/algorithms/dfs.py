def dfs(adj_list, start, path=[]):
	if start not in path:
		path.append(start)
	for child in adj_list.get(start, []):
		dfs(adj_list, child, path)

	return path