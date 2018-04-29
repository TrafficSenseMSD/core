"""

.. _ts_config_bindings:

SUMO XSD Python Bindings
========================

While there are other simpler XML generation tools, XSD bindings were used to guarantee schema and type correctness 
when generating SUMO configuration files. 

The primary usage for these bindings can be found here.

SUMO provides schema definitions for all the XML files used in the SUMO ecosystem. The enumeration of the files
and their definitions can be found `here <http://sumo.dlr.de/wiki/Other/File_Extensions>`_ .

At the time of this release, bindings for the following were included:

+------------------+--------------------+
|SUMO Extension    | Python File        |
+==================+====================+
|add.xml           |additional_xml.py   |
+------------------+--------------------+
|con.xml           |con_xml.py          |
+------------------+--------------------+
|edg.xml           |edges_xml.py        |
+------------------+--------------------+
|net.xml           |netflie.py          |
+------------------+--------------------+
|nod.xml           |nodes_xml.py        |
+------------------+--------------------+
|rou.xml           |routes.py           |
+------------------+--------------------+
|.sumocfg          |sumocfg.py          |
+------------------+--------------------+

Note that only add.xml, edg.xml, and .sumocfg are actually used in this release. 

Regenerating SUMO XSD Bindings
------------------------------

From a Python environment with ``pyxb`` installed run:

``pyxbgen -u <foo.xsd> -m <module name>``

Move the generated files to the ``bindings`` directory and test that everything works as expected. 



"""