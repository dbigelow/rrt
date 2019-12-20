from numpy import sqrt
from random import randint
from RRTMap import Graph
from RRTMap import MapDisplay
from RRTMap import Node
import sys

class RRT:
    def __init__(self, start_node, end_node, map):
        self.start_node = start_node
        self.end_node = end_node
        self.mapDisplay = map
        self.Tree = Graph()
        self.Tree.addNode(start_node)
        if self.checkMapEdges(end_node, start_node):
            self.Tree.addNode(end_node)
            self.Tree.addEdge(start_node, end_node)

    def getRandomNode(self) -> Node:
        randNode = Node(randint(0,self.mapDisplay.width - 1), randint(0,self.mapDisplay.height - 1))
        return randNode

    def findNearestNode(self, newNode) -> Node:
        minDistance = sqrt(self.mapDisplay.width ** 2 + self.mapDisplay.height ** 2)
        nearestNode = None
        for node in self.Tree.graph.keys():
            dist = newNode.nodeDistance(node)
            if dist < minDistance and self.checkMapEdges(newNode, node):
                minDistance = dist
                nearestNode = node
        return nearestNode

    def explore(self) -> bool:
        if self.end_node in self.Tree.graph.keys():
            return True
        randNode = self.getRandomNode()
        nearestNode = self.findNearestNode(randNode)
        while nearestNode is None:
            randNode = self.getRandomNode()
            nearestNode = self.findNearestNode(randNode)
        self.Tree.addNode(randNode)
        self.Tree.addEdge(nearestNode,randNode)
        if self.checkMapEdges(self.end_node, randNode):
            self.Tree.addNode(self.end_node)
            self.Tree.addEdge(randNode, self.end_node)
            return True
        return False

    '''Returns False if nodes cross a map line/edge'''
    def checkMapEdges(self, node1, node2) -> bool:
        for edge in self.mapDisplay.map:
            if self.doIntersect(edge[0], edge[1], node1, node2):
                return False
        return True

    def checkOrientation(self, p, q, r):
        #See https://www.geeksforgeeks.org/orientation-3-ordered-points/ for details of below formula.
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)   
        if val == 0:
           return 0 #colinear
        return 1 if val > 0 else 2 #clock or counterclock wise
    
    def doIntersect(self, p1, q1, p2, q2) -> bool:
        # Find the four orientations needed for general and special cases
        o1 = self.checkOrientation(p1, q1, p2) 
        o2 = self.checkOrientation(p1, q1, q2) 
        o3 = self.checkOrientation(p2, q2, p1) 
        o4 = self.checkOrientation(p2, q2, q1) 
        # General case
        if o1 != o2 and o3 != o4:
            return True
        # Special Cases
        # p1, q1 and p2 are colinear and p2 lies on segment p1q1
        if o1 == 0 and self.onSegment(p1, p2, q1):
           return True
        # p1, q1 and q2 are colinear and q2 lies on segment p1q1
        if o2 == 0 and self.onSegment(p1, q2, q1):
           return True 
        # p2, q2 and p1 are colinear and p1 lies on segment p2q2
        if o3 == 0 and self.onSegment(p2, p1, q2):
           return True 
        # p2, q2 and q1 are colinear and q1 lies on segment p2q2
        if o4 == 0 and self.onSegment(p2, q1, q2):
           return True 
        return False # Doesn't fall in any of the above cases 

    def onSegment(self, p, q, r) -> bool: 
        return q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y)