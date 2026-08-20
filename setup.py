#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# RespInPeace - Process and analyse breathing belt (RIP) data.
# Copyright (C) 2018 Marcin Wlodarczak
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# NOTE: originally used distutils.core.setup, which was removed in
# Python 3.12. Switched to setuptools, the drop-in, actively
# maintained replacement.
from setuptools import setup

setup(
    name='rip',
    description='RespInPeace - Process and analyse breathing belt (RIP) data.',
    version='0.9.1',
    py_modules=['rip', 'peakdetect'],
    maintainer='Marcin Wlodarczak',
    maintainer_email='wlodarczak@ling.su.se',
    license='GNU General Public License 3',
    download_url='https://github.com/mwlodarczak/RespInPeace/',
    install_requires=[
        'numpy',
        'scipy',
        'pandas',
        'matplotlib',
        'tgt',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
)
