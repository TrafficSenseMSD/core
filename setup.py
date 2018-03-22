import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    install_requires=required,
    name="trafficsense_core",
    version="0.3",
    description="Framework for working with SUMO and TraCI to support traffic light optimization",
    author="",
    packages=find_packages(),
    entry_points={
         'console_scripts': ['ts_runner=ts_core.cli.ts_runner:main',
                             'ts_config=ts_core.cli.ts_config:main']}
)
