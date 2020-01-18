import cv2
import numpy as np
from os import system, name 
if name == 'nt':
    from msvcrt import getwch
else:
    from getch import getch as getwch   

def clear(): 
  
    # for windows
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix')
    else: 
        _ = system('clear') 

#ghetto logging:
log_level = "ERROR"


class Colors: #Open cv orders colors as (B,G,R)
    BLUE = (255, 0, 0)
    GREEN = (0, 255, 0)
    RED = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

class MapDisplay:

    def __init__(self, map, width=500, height=500):
        self.map = map
        self.width = width
        self.height = height
        cv2.namedWindow("map", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("map", width, height)

    def drawMap(self):
        blank_image = self.loadMap()
        cv2.imshow("map",blank_image)
        cv2.waitKey(0) # waits until a key is pressed

    def drawGraph(self, graph, goalNode = None):
        if log_level == "DEBUG":
            clear()
        map_image = self.loadMap()


        #draw starting node green
        nodeColor = Colors.GREEN #self.drawPoint(map_image, graph.graph.keys()[0], Colors.GREEN)

        for node in graph.graph.keys():
            map_image = self.drawPoint(map_image, node, nodeColor)
            nodeColor = Colors.BLUE #draw remaining nodes blue

            for node2 in graph.graph[node]:
                cv2.line(map_image, (node.x, node.y), (node2.x, node2.y), Colors.BLUE, 1)

        #Draw the goal node
        map_image = self.drawPoint(map_image, goalNode, Colors.RED)

        cv2.imshow("map",map_image)
        cv2.waitKey(0) # waits until a key is pressed
       

    def loadMap(self):
        blank_image = np.zeros((self.height, self.width, 3), np.uint8)
        blank_image[:,:] = Colors.WHITE

        for i in self.map:
            p1 = i[0]
            p2 = i[1]
            cv2.line(blank_image, (p1.x,p1.y), (p2.x,p2.y), Colors.BLACK, 1)
        return blank_image


    def drawPoint(self, image, node, color):
        if(node):
            if log_level == "DEBUG":
                print("Drawing " + str(color) + " node")
            cv2.circle(image, (node.x, node.y), 2, color, 2)
        return image

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def nodeDistance(self, other) -> float:
        return np.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class Graph:
    def __init__(self):
        self.graph = {}

    def addNodeCoordinates(self, x, y):
        for existing_node in self.graph.keys():
            if existing_node.x == x and existing_node.y == y:
                raise Exception("Node already exists")
        node = Node(x, y)
        self.graph[node] = []
        return node

    def addNode(self, node):
        for existing_node in self.graph.keys():
            if existing_node == node:
                raise Exception("Node already exists")
        self.graph[node] = []

    def addEdge(self, node_from, node_to):
        if node_to not in self.graph[node_from]:
            self.graph[node_from].append(node_to)
        if node_from not in self.graph[node_to]:
            self.graph[node_to].append(node_from)

