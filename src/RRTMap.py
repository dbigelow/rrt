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
	def __init__(self, name, x, y):
		self.name = name
		self.x = x
		self.y = y


mapDisplay = MapDisplay([[(100,100),(100,200)],[(300,300),(100,100)]])


tree = {}


mapDisplay.drawMap()
