class MiniMax:
    def __init__(self, board_tree):
        self.board_tree
        self.currentNode = None
        self.next_nodes = []
        return

    def minimax(self, node):
        fit_val = self.max_value

    def max_value(self, node):
        # print "Max: Visited Node::  "+node.Name
        if self.is_end(node):
            return self.getUtil(node)
        inf = float('inf')
        max_value = -inf

        previous_nodes = self.previous_nodes(node)
        for state in previous_nodes:
            max_val = max(max_val, self.min_value())

    def is_end(self, node):
        assert node is not None
        return len(node.value) == 0

    def getUtil(self, node):
        assert node is not None
        return node.value

    def previous_node(self, node):
        assert node is not None
        return node.value
