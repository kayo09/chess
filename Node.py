class Node:	 #takes in matrix and score such that with traversal, ideal iterations can be generated and taken
    def __init__(self, key, matrix, score):
            
        self.key = key
        self.child = []
        self.egg = matrix
        self.score - score

# Utility function to create a new tree node
def newNode(key):
	temp = Node(key)
	return temp