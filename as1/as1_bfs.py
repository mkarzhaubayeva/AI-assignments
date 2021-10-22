#Author: Dinh-Mao Bui, Anh-Tu Nguyen
#Rule of traversing: Alphabetical ordered, then left to right, 
#Points: 2
def traverse(tree, init):    	
	queue = [init]
	traversed = []
	while queue:
		node = queue.pop(0)
		if traversed.count(node) != 0:
			continue
		traversed.append(node)
		leaves = tree[node]
		leaves.sort()
		for leaf in leaves:
			queue.append(leaf)
	return traversed

#Points: 3
def pathfinder(tree, init, goal):
	traversed = []
	queue = [[init]]
	if init == goal:
		return "No kidding, pls"
	while queue:
		path = queue.pop(0)
		node = path[-1]
		if traversed.count(node) == 0:
			leaves = tree[node]
			leaves.sort()
			for leaf in leaves:
				new_path = list(path)
				new_path.append(leaf)
				queue.append(new_path)
				if leaf == goal:
					traversed.append(leaf)
					return new_path
			traversed.append(node)
	return "No such path exists"