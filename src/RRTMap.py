import cv2
import numpy as np

class MapDisplay:
	"""A generic blackjack player"""

	def __init__(self, map, width=500, height=500):
		self.map = map
		self.width = width
		self.height = height

	def drawMap(self):
		blank_image = np.zeros((self.height, self.width, 3), np.uint8)
		blank_image[:,:] = (255,255,255)
		#print(blank_image)
		for i in self.map:
			p1 = i[0]
			p2 = i[1]
			print(p1)
			print(p2)
			cv2.line(blank_image, p1, p2, (0,255,0), 1)
		cv2.imshow("map",blank_image)
		cv2.waitKey(0) # waits until a key is pressed
		cv2.destroyAllWindows() # destroys the window showing image
class Node:
	def __init__(self, label, x, y):
		self.label = label
		self.x = x
		self.y = y





class Graph:
	def __init__(self):
		
		self.graph = {}
		self.largest_label = -1 

	def addNode(self, x, y):
		for existing_node in self.graph.keys():
			if existing_node.x == x and existing_node.y == y:
				raise Exception("Node already exists")
		
		largest_label += 1
		label = largest_label
		node = Node(label, x, y)
		self.graph.append(node)
		self.graph[node] = []
		return node

	def addEdge(self, node_from, node_to):
		self.graph[node_from].append(node_to)

mapDisplay = MapDisplay([[(100,100),(100,200)],[(300,300),(100,100)]])
mapDisplay.drawMap()
