# Welcome to TrafficSenseMSD
TrafficSenseMSD is an open-source traffic light performance tuning and optimization tool build
by RIT students for Multidisciplinary Senior Design. The design and project process documentation can be found [here](http://edge.rit.edu/edge/P18393/public/Home)

[![Build Status](https://travis-ci.org/TrafficSenseMSD/core.svg?branch=master)](https://travis-ci.org/TrafficSenseMSD/core)


# Documentation
For the official source code documentation, go [here](https://trafficsensemsd.github.io/core/)


# Installation Guides

## Windows Installation
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

#3 Linux Install
[SUMO Linux Install Docs](http://sumo.dlr.de/wiki/Installing/Linux_Build)

The above documentation is spotty at best.  You will likely be able to follow the mac

## Mac Installation
[The somewhat difficult to follow SUMO install docs for Mac OS](http://sumo.dlr.de/wiki/Installing/MacOS_Build_w_Homebrew)

1) Install Homebrew package manager
2) `wget -o sumo-src-0.32.0.tar.gz http://prdownloads.sourceforge.net/sumo/sumo-src-0.32.0.tar.gz?download`
3) `tar -xzvf sumo-src-0.32.0.tar.gz`
4) `cd ./sumo-src-0.32.0`

5) 
``` brew update
    brew install Caskroom/cask/xquartz
    brew install autoconf
    brew install automake
    brew install pkg-config
    brew install libtool
    brew install gdal
    brew install proj
    brew install xerces-c
    brew install fox
```
    
6) `export CPPFLAGS="$CPPFLAGS -I/opt/X11/include/"`
    `export LDFLAGS="-L/opt/X11/lib"`
    
7) `autoreconf -i`
8) `./configure CXX=clang++ CXXFLAGS="-stdlib=libc++ -std=gnu++11" --with-xerces=/usr/local --with-proj-gdal=/usr/local`
9) ```make -j`sysctl -n hw.ncpu` ```
10) `export SUMO_HOME=$(pwd)`

Don't do `make install`. Things get all messed up

