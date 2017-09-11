#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pkgversion import list_requirements, pep440_version, write_setup_py
from setuptools import find_packages

write_setup_py(
    name='etcd-config',
    version=pep440_version(),
    description="A dynamic settings management solution using ETCD",
    long_description=open('README.rst').read(),
    author="Andrey Makhnach",
    author_email='andrey.makhnach@kpn.com',
    url='https://github.com/kpn-digital/py-etcd-config',
    install_requires=list_requirements('requirements/requirements-base.txt'),
    packages=find_packages(exclude=['etcd_config.tests*']),
    tests_require=['tox'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
