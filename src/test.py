from RRTMap import MapDisplay
from RRTMap import Graph
from RRTMap import Node
from RRTAlgorithim import RRT


mapDisplay = MapDisplay([[(100,100),(100,200)],[(300,300),(100,100)]])
mapDisplay.drawMap()


graph = Graph()
node1 = graph.addNodeCoordinates(240, 240)
node2 = graph.addNodeCoordinates(250, 250)
node3 = Node(220, 250)
graph.addNode(node3)

graph.addEdge(node1, node2)
graph.addEdge(node1, node3)

rrt = RRT(node1,node3,graph)

mapDisplay.drawGraph(graph)