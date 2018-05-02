# Welcome to TrafficSenseMSD
TrafficSenseMSD is an open-source traffic light performance tuning and optimization tool build
by RIT students for Multidisciplinary Senior Design. The design and project process documentation can be found [here](http://edge.rit.edu/edge/P18393/public/Home)

[![Build Status](https://travis-ci.org/TrafficSenseMSD/core.svg?branch=master)](https://travis-ci.org/TrafficSenseMSD/core)


# Documentation
For the official source code documentation, go [here](https://trafficsensemsd.github.io/core/)


----------------------------------------
----------Windows Installation----------
----------------------------------------
Prerequisites:
1) python 3.5+
2) GIT
3) pip

Steps:
In a terminal with privileges:
1) Navigate to the directory in which you want to install this
2) Clone the GIT repository ("git clone https://github.com/TrafficSenseMSD/core.git")
3) Navigate to the "core" directory
4) Install this location as a python package ("pip install [-e] ."). Use -e if you intend on editing any of the files to add functionality
5) Install SUMO 0.32.0. Sumo provides installers for Windows 32 and 64 bit versions


Usage (As of TrafficSenseMSD version 0.72.0):
ts_core build -c <path> -p <path>
ts_runner <path> [--gui]

