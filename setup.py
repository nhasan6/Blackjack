# Blackjack/setup.py
from setuptools import setup, find_packages

setup(
    name='blackjack',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "pygame-ce>=2.5.3"
    ],
)