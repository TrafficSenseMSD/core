import ts_core.config.bindings.nodes_xml as nodes

n = nodes.nodes()

n.append(nodes.nodeType(id=0, x=0, y=0, type="traffic_light"))
n.append(nodes.nodeType(id=1, x=-500, y=0, type="traffic_light"))
n.append(nodes.nodeType(id=2, x=500, y=0, type="traffic_light"))
n.append(nodes.nodeType(id=3, x=0, y=-500, type="traffic_light"))
n.append(nodes.nodeType(id=4, x=0, y=500, type="traffic_light"))

from xml.dom import minidom

xmlstr = minidom.parseString(n.toxml("utf-8").decode('utf-8')).toprettyxml(indent="   ")
print(xmlstr)



