import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    install_requires=required,
    name="tsmsd_core_src",
    version="0.02",
    description="Framework for working with SUMO and TraCI to support traffic light optimization",
    author="",
    packages=find_packages(),
    # entry_points={
    #     'console_scripts': ['build_census=rsds_src.data.etl.us_census.build_census:main',
    #                         'build_rca=rsds_src.data.etl.rca.build_rca:main',
    #                         'build_rca_sponsor_join=rsds_src.data.etl.rca.rca_sponsor_join:main',
    #                         'build_cdf_model=models.sponsor_lead_sourcing.make_cdf_output:main'],
    # }
)
