#!/usr/bin/env python3
from setuptools import setup

setup(
    name="binance-client",
    version="1.0.1",
    packages=['binance', 'binance.impl', 'binance.impl.utils', 'binance.exception', 'binance.model', 'binance.base', 'binance.constant'],
    install_requires=['requests', 'apscheduler', 'websocket-client', 'urllib3']
)

