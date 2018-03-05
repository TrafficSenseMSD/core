import ts_core.config.bindings.routes as routes
import pyxb

def sample_route_file():
    r = routes.routes()

    #######
    flow1 = routes.flowType(id="type1", probability=0.2) # begin="10", end= "1000", probability="0.2", accel="2.7", decel="4.5", sigma="0.8", length="5", minGap="2.5", maxSpeed="13.41", departSpeed="13.41", departLane="random", type="vehicledist1i", route="routedist1i")

    r.flow.append(flow1)

    r.vType.append(
        routes.vTypeType(id="typeWE", accel="5", decel="4.5", sigma="0.8", length="5", minGap="2.5", maxSpeed="30", guiShape="passenger"))
    r.vType.append(
        routes.vTypeType(id="typeNS", accel="0.8", decel="4.5", sigma="0.05", length="7", minGap="3", maxSpeed="25", guiShape="bus"))

    vTypeDist1 = routes.vTypeDistributionType(id="vehicledist1i")
    vTypeDist1.vType.append(
        routes.vTypeType(id="type11", accel="0.8", decel="4.5", length="5", maxSpeed="30", probability="0.8"))
    vTypeDist1.vType.append(
        routes.vTypeType(id="type21", accel="1.8", decel="4.5", length="15", maxSpeed="25", probability="0.2"))

    # r.vTypeDistribution.append(vTypeDist1)

    routeDist1 = routes.vehicleRouteDistributionType(id="routedist1i")
    routeDist1.route.append(routes.routeDistRouteType(id="route01", color="255,0,0", edges="1i 4o", probability="0.2"))
    routeDist1.route.append(routes.routeDistRouteType(id="route11", color="0,255,0", edges="1i 3o", probability="0.2"))
    routeDist1.route.append(routes.routeDistRouteType(id="route21", color="0,0,255", edges="1i 2o", probability="0.6"))
    #r.routeDistribution.append(routeDist1)


    flow1.type = vTypeDist1.id
    flow1.routeDistribution = routeDist1


    #######
    vTypeDist1 = routes.vTypeDistributionType(id="vehicledist2i")
    vTypeDist1.vType.append(
        routes.vTypeType(id="type12", accel="0.8", decel="4.5", length="5", maxSpeed="30", probability="0.8"))

    vTypeDist1.vType.append(
        routes.vTypeType(id="type22", accel="1.8", decel="4.5", length="15", maxSpeed="25", probability="0.2"))

    r.vTypeDistribution.append(vTypeDist1)

    routeDist1 = routes.routeDistributionType(id="routedist2i")
    routeDist1.route.append(routes.routeDistRouteType(id="route02", color="0,255,0", edges="2i 4o", probability="0.2"))
    routeDist1.route.append(routes.routeDistRouteType(id="route12", color="255,0,0", edges="2i 3o", probability="0.2"))
    routeDist1.route.append(routes.routeDistRouteType(id="route22", color="0,0,255", edges="2i 1o", probability="0.6"))
    r.routeDistribution.append(routeDist1)

    #######
    vTypeDist1 = routes.vTypeDistributionType(id="vehicledist3i")
    vTypeDist1.vType.append(
        routes.vTypeType(id="type13", accel="0.8", decel="4.5", length="5", maxSpeed="30", probability="0.8"))

    vTypeDist1.vType.append(
        routes.vTypeType(id="type23", accel="1.8", decel="4.5", length="15", maxSpeed="25", probability="0.2"))

    r.vTypeDistribution.append(vTypeDist1)

    routeDist1 = routes.routeDistributionType(id="routedist3i")
    routeDist1.route.append(routes.routeDistRouteType(id="route03", color="0,0,255", edges="3i 4o", probability="0.6"))
    routeDist1.route.append(routes.routeDistRouteType(id="route13", color="0,255,0", edges="3i 2o", probability="0.2"))
    routeDist1.route.append(routes.routeDistRouteType(id="route23", color="255,0,0", edges="3i 1o", probability="0.2"))
    r.routeDistribution.append(routeDist1)

    #######
    vTypeDist1 = routes.vTypeDistributionType(id="vehicledist4i")
    vTypeDist1.vType.append(
        routes.vTypeType(id="type14", accel="0.8", decel="4.5", length="5", maxSpeed="30", probability="0.8"))

    vTypeDist1.vType.append(
        routes.vTypeType(id="type24", accel="1.8", decel="4.5", length="15", maxSpeed="25", probability="0.2"))

    r.vTypeDistribution.append(vTypeDist1)

    routeDist1 = routes.routeDistributionType(id="routedist4i")
    routeDist1.route.append(routes.routeDistRouteType(id="route04", color="255,0,0", edges="4i 2o", probability="0.2"))
    routeDist1.route.append(routes.routeDistRouteType(id="route14", color="0,20,255", edges="4i 3o", probability="0.6"))
    routeDist1.route.append(routes.routeDistRouteType(id="route24", color="0,255,0", edges="4i 1o", probability="0.2"))
    r.routeDistribution.append(routeDist1)



    from xml.dom import minidom
    xmlstr = minidom.parseString(r.toxml("utf-8").decode('utf-8')).toprettyxml(indent="   ")
    print(xmlstr)




"""
http://sumo.dlr.de/xsd/sumoConfiguration.xsd
"""

