import ts_core.configuration.bindings.routes as routes


r = routes.routes()
r.vType.append(
    routes.vTypeType(id="typeWE", accel="5", decel="4.5", sigma="0.8", length="5", minGap="2.5", maxSpeed="30", guiShape="passenger"))
r.vType.append(
    routes.vTypeType(id="typeNS", accel="0.8", decel="4.5", sigma="0.05", length="7", minGap="3", maxSpeed="25", guiShape="bus"))

vTypeDist1 = routes.vTypeDistributionType(id="vehicledist1i")
vTypeDist1.vType.append(
    routes.vTypeType(id="type11", accel="0.8", decel="4.5", length="5", maxSpeed="30", probability="0.8"))
vTypeDist1.vType.append(
    routes.vTypeType(id="type21", accel="1.8", decel="4.5", length="15", maxSpeed="25", probability="0.2"))
r.vTypeDistribution.append(vTypeDist1)

vTypeDist1 = routes.vTypeDistributionType(id="routedist1i")
vTypeDist1.vType.append(
    routes.vTypeType(id="type11", accel="0.8", decel="4.5", length="5", maxSpeed="30", probability="0.8"))
vTypeDist1.vType.append(
    routes.vTypeType(id="type21", accel="1.8", decel="4.5", length="15", maxSpeed="25", probability="0.2"))
r.vTypeDistribution.append(vTypeDist1)

routeDist1 = routes.routeDistributionType(id="routedist2i")
routeDist1.route.append(routes.routeDistRouteType(id="route02", color="0,255,0", edges="2i 4o", probability="0.2"))
routeDist1.route.append(routes.routeDistRouteType(id="route12", color="255,0,0", edges="2i 3o", probability="0.2"))
routeDist1.route.append(routes.routeDistRouteType(id="route22", color="0,0,255", edges="2i 1o", probability="0.6"))

r.routeDistribution.append(routeDist1)

from xml.dom import minidom
xmlstr = minidom.parseString(r.toxml("utf-8").decode('utf-8')).toprettyxml(indent="   ")
print(xmlstr)




"""
http://sumo.dlr.de/xsd/sumoConfiguration.xsd
"""

