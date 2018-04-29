#!/bin/bash
python "/home/gsoponski/sumo-0.32.0/tools/randomTrips.py" -n osm.net.xml --seed 42 --fringe-factor 40 -p 0.963897 -r osm.passenger.rou.xml -o osm.passenger.trips.xml -e 3600 --vehicle-class passenger --vclass passenger --prefix veh --min-distance 300 --trip-attributes 'speedDev="0.1" departLane="best"' --validate
