from setuptools import setup

setup(
    name='CPU_FAN_BBB',
    version='0.0.1',
    author='Abdelhamed Eldeeb',
    description='Controls a fan for beaglebone black using a thermistor on top of the CPU',
    py_modules=["CPU_FAN_BBB"],
    package_dir={'':'src'},
    classifiers=[
        "Programmubg Language :: Python :: 3"
        "License :: OSI Approved :: GNU General Public License v2 or Later (GPLv2+)"
        "Operatin System :: Unix"
    ]
)