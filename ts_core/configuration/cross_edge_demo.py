import ts_core.configuration.bindings.edges_xml as edge

e = edge.edges()

# I/O for direction 1
edgei = edge.edgeType(id="1i", from_=1, to=0, priority=78, numLanes=3, speed=19.4444)
edgei.lane.append(edge.laneType(index=0, speed=19.444, shape="0.00,495.05 248.50,495.05"))
e.append(edgei)


edgei = edge.edgeType(id="1o", from_=0, to=1, priority=46, numLanes=3, speed=11.111)
e.append(edgei)

# I/O for direction 2
edgei = edge.edgeType(id="2i", from_=2, to=0, priority=78, numLanes=3, speed=19.4444)
e.append(edgei)

edgei = edge.edgeType(id="2o", from_=0, to=2, priority=46, numLanes=3, speed=11.111)
e.append(edgei)

# I/O for direction 3
edgei = edge.edgeType(id="3i", from_=3, to=0, priority=78, numLanes=3, speed=19.4444)
e.append(edgei)

edgei = edge.edgeType(id="3o", from_=0, to=3, priority=46, numLanes=3, speed=11.111)
e.append(edgei)

# I/O for direction 4
edgei = edge.edgeType(id="4i", from_=4, to=0, priority=78, numLanes=3, speed=19.4444)
e.append(edgei)

edgei = edge.edgeType(id="4o", from_=0, to=4, priority=46, numLanes=3, speed=11.111)

import random
for i in range(510):
    e.append(edge.edgeType(id= str(random.randint(2,10))+"o", from_=0, to=4, priority=46, numLanes=3, speed=11.111))

e.append(edgei)


from xml.dom import minidom

xmlstr = minidom.parseString(e.toxml("utf-8").decode('utf-8')).toprettyxml(indent="   ")
print(xmlstr)
