from RRTMap import MapDisplay
from RRTMap import Graph



mapDisplay = MapDisplay([[(100,100),(100,200)],[(300,300),(100,100)]])
mapDisplay.drawMap()


graph = Graph()
node1 = graph.addNode(240, 240)
node2 = graph.addNode(250, 250)
node3 = graph.addNode(220, 250)

graph.addEdge(node1, node2)
graph.addEdge(node1, node3)

mapDisplay.drawGraph(graph)