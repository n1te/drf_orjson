#!/usr/bin/env python

from setuptools import setup

setup(
    name='drf_orjson',
    version='0.3',
    description='DRF ORJSON Renderer',
    license='MIT',
    author='Stanislav Shershnev',
    author_email='shershnev.stas@gmail.com',
    url='https://github.com/n1te/drf_orjson',
    packages=['drf_orjson'],
    install_requires=['django', 'orjson', 'djangorestframework'],
    tests_require=['pytest'],
    python_requires=">=3.5",
)
