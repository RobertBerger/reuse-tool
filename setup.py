#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017  Free Software Foundation Europe e.V.
#
# This file is part of reuse, available from its original location:
# <https://git.fsfe.org/reuse/reuse/>.
#
# reuse is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# reuse is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# reuse.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0+

import os

from setuptools import setup

requirements = [
    'click',
    'python-debian',
]
git_extras = []

if not os.environ.get('REUSE_DEV'):
    git_extras.append('pygit2')

test_requirements = [
    'pytest',
]

if __name__ == '__main__':
    setup(
        name='fsfe-reuse',
        version='0.0.4',
        url='https://git.fsfe.org/reuse/reuse',
        license='GPL-3.0+',

        author='Carmen Bianca Bakker',
        author_email='carmenbianca at fsfe dot org',

        description='reuse is a tool for compliance with the REUSE Initiative '
            'recommendations.',
        long_description=open('README.md').read(),

        package_dir={
            '': 'src'
        },
        packages=[
            'reuse',
        ],

        entry_points={
            'console_scripts': [
                'reuse = reuse._main:cli',
            ],
        },

        install_requires=requirements,
        tests_require=test_requirements,
        extras_require={
            'git': git_extras,
        },

        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: '
            'GNU General Public License v3 or later (GPLv3+)',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
        ],
    )
