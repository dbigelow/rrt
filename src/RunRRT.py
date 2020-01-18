from RRTMap import MapDisplay
from RRTMap import Graph
from RRTMap import Node
from RRTAlgorithim import RRT


map = [
	[Node(100,100),Node(100,200)],
	[Node(20,200),Node(100,200)],
	[Node(300,300),Node(100,100)],
	[Node(300,300),Node(300,400)],
	[Node(300,400),Node(200,400)]
]

mapDisplay = MapDisplay(map)
mapDisplay.drawMap()
node1 = Node(50, 150)
node2 = Node(125, 175)
rrt = RRT(node1,node2,mapDisplay)
while not rrt.explore():
    rrt.mapDisplay.drawGraph(rrt.Tree, rrt.end_node)
rrt.mapDisplay.drawGraph(rrt.Tree, rrt.end_node)
