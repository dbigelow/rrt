from RRTMap import MapDisplay
from RRTMap import Graph
from RRTMap import Node
from RRTAlgorithim import RRT


mapDisplay = MapDisplay([[Node(100,100),Node(100,200)],[Node(0,200),Node(100,200)],[Node(300,300),Node(100,100)],[Node(300,300),Node(450,300)]])
mapDisplay.drawMap()
node1 = Node(50, 50)
node2 = Node(250, 450)
rrt = RRT(node1,node2,mapDisplay)
while not rrt.explore():
    rrt.mapDisplay.drawGraph(rrt.Tree, rrt.end_node)
rrt.mapDisplay.drawGraph(rrt.Tree, rrt.end_node)
