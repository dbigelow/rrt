from RRTMap import Graph
from RRTMap import Node

class RRT:
    def __init__(self, start_node, end_node, map):
        self.start_node = start_node
        self.end_node = end_node
        self.map = map
        self.Tree = Graph()
        self.Tree.addNode(start_node)
        self.Tree.addNode(end_node)




