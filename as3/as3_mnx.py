#Assignment 3
from as3_tree import Tree
class Result:
	def __init__(self, sol=[], val=-1000):
			self.solution = sol
			self.value = val
			
class MNX:
	def __init__(self, data_list):
		self.tree = Tree()	
		self.tree.init_tree(data_list)
		self.root = self.tree.root
		self.currentNode = None
		self.successors = []		
		return
        
	def terminalTest(self, node):
		assert node is not None
		return len(node.children) == 0

	def utilityChecking(self, node):
		assert node is not None
		return node.value

	def getChildren(self, node):
		assert node is not None
		return node.children

	def minimax(self):		
		terminal_val = self.max_v(self.root)
		successors = self.getChildren(self.root)
		traversed = self.traverse(self.root, terminal_val); #example of solution_array
		res = Result();


#################  Return the solution here  #################
		res.value=terminal_val #you put the best terminal value for root node here
		res.solution=traversed #you put the solution_array here
#################  Return the solution here  #################



		return res

	def traverse(self, begin, end):
		queue = []
		queue.append(begin)
		current = begin

		while queue:
			node = queue.pop(0)
			deeper_layer = self.getChildren(node)
			for deeper_node in deeper_layer:
				if self.terminalTest(deeper_node) and self.utilityChecking(deeper_node) == end:
					current = deeper_node
					break
				elif not self.terminalTest(deeper_node):
					queue.append(deeper_node)
		
		traversed = []
		traversed.append(current.Name)
		while(current.parent):
			traversed.insert(0, current.parent.Name)
			current = current.parent
		return traversed

	def max_v(self, node):		
		if self.terminalTest(node):
			return self.utilityChecking(node)		
		max_v = -1000 #we use 1000 as the initial_maximum value
		deeper_layer = self.getChildren(node)
		for deeper_node in deeper_layer:
			max_v = max(max_v, self.min_v(deeper_node))
		return max_v

	def min_v(self, node):		
		if self.terminalTest(node):
			return self.utilityChecking(node)
		min_v = 1000 #we use -1000 as the initial_minimum value
		deeper_layer = self.getChildren(node)
		for deeper_node in deeper_layer:
			min_v = min(min_v, self.max_v(deeper_node))
		return min_v