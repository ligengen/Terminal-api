from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
    name="Terminal-api",
    version="0.0.0",
    author="Root",
    author_email="ligen_thu@163.com",
    description="A Python library for mlgridengine lazy terminal.",
    long_description=open("README.rst").read(),
    license="MIT",
    url="https://github.com/ligengen/Terminal-api",
    packages=['Terminal-api'],
    classifiers=[
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Topic :: Multimedia :: Video',
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=True,
    install_requires=[
        'pytest==3.8.2',
        'colorama==0.3.9',
        'requests==2.18.4',
        'coverage==4.5.1',
        'pytz==2018.4',
        'click==7.0',
        'future-fstrings==0.4.4',
        'tokenize-rt==2.1.0',
        'mock==2.0.0',
        'pbr==4.3.0',
    ]
)
