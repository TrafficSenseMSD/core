import ts_core.config.bindings.con_xml as conn

con = conn.connections()

con.append(conn.connectionType(from_="1i", to="2o", fromLane="1", toLane="1"))
con.append(conn.connectionType(from_="1i", to="2o", fromLane="0", toLane="0"))
con.append(conn.connectionType(from_="1i", to="4o", fromLane="2", toLane="2"))
con.append(conn.connectionType(from_="1i", to="3o", fromLane="0", toLane="0"))

con.append(conn.connectionType(from_="2i", to="1o", fromLane="1", toLane="1"))
con.append(conn.connectionType(from_="2i", to="1o", fromLane="0", toLane="0"))
con.append(conn.connectionType(from_="2i", to="3o", fromLane="2", toLane="2"))
con.append(conn.connectionType(from_="2i", to="4o", fromLane="0", toLane="0"))

con.append(conn.connectionType(from_="3i", to="1o", fromLane="2", toLane="2"))
con.append(conn.connectionType(from_="3i", to="2o", fromLane="0", toLane="0"))
con.append(conn.connectionType(from_="3i", to="4o", fromLane="1", toLane="1"))
con.append(conn.connectionType(from_="3i", to="4o", fromLane="0", toLane="0"))

con.append(conn.connectionType(from_="4i", to="1o", fromLane="0", toLane="0"))
con.append(conn.connectionType(from_="4i", to="2o", fromLane="2", toLane="2"))
con.append(conn.connectionType(from_="4i", to="3o", fromLane="1", toLane="1"))
con.append(conn.connectionType(from_="4i", to="3o", fromLane="0", toLane="0"))


from xml.dom import minidom
xmlstr = minidom.parseString(con.toxml("utf-8").decode('utf-8')).toprettyxml(indent="   ")
print(xmlstr)
