"""

.. _ts_config_bindings:

SUMO XSD Python Bindings
------------------------

Bindings were used to guarantee schema and type correctness when generating SUMO configuration files. 

SUMO provides schema definitions for all the XML files used in the SUMO ecosystem. The enumeration of the files
and their definitions can be found `here <http://sumo.dlr.de/wiki/Other/File_Extensions>`_.

At the time of this release, bindings for the following were included. 


==============      ============
SUMO Extension      Python File 
==============      ============
add.xml             additional_xml.py
con.xml             con_xml.py
edg.xml             edges_xml.py
net.xml             netflie.py
nod.xml             nodes_xml.py
rou.xml             routes.py
.sumocfg            sumocfg.py
===============     ============

"""