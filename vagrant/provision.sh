#!/usr/bin/env bash

sudo apt-get update
sudo apt-get -y install git
sudo apt-get -y install sumo sumo-tools sumo-doc

# load TrafficSenseMSD core
mkdir  -p /srv/deploy/current
(cd /srv/deploy/current && git clone https://github.com/TrafficSenseMSD/core.git)
(cd /srv/deploy/current && git pull)

# Load eilifm fork of core
mkdir  -p /srv/dev/eilifm
(cd /srv/dev/eilifm && git clone https://github.com/eilifm/core.git)
(cd /srv/dev/eilifm && git pull)

