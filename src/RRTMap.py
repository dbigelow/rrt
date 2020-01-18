import cv2
import numpy as np

class Colors:
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

class MapDisplay:

    def __init__(self, map, width=500, height=500):
        self.map = map
        self.width = width
        self.height = height

    def drawMap(self):
        blank_image = self.loadMap()
        cv2.imshow("map",blank_image)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows() # destroys the window showing image

    def drawGraph(self, graph):
        map_image = self.loadMap()
        dotColor = Colors.GREEN
        for node in graph.graph.keys():
            cv2.circle(map_image, (node.x, node.y), 3, dotColor, 3)
            dotColor = Colors.BLUE
            for node2 in graph.graph[node]:
                cv2.line(map_image, (node.x, node.y), (node2.x, node2.y), Colors.BLUE, 1)
        cv2.imshow("map",map_image)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows() # destroys the window showing image

    def loadMap(self):
        blank_image = np.zeros((self.height, self.width, 3), np.uint8)
        blank_image[:,:] = Colors.WHITE

        for i in self.map:
            p1 = i[0]
            p2 = i[1]
            cv2.line(blank_image, (p1.x,p1.y), (p2.x,p2.y), Colors.BLACK, 1)
        return blank_image

    def drawPoint(self, image, point, color):
        pass
        # cv2.point()

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

