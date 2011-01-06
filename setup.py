#!/usr/bin/env python

# Credit to bartTC and https://github.com/bartTC/django-memcache-status for ideas

try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command.test import test


setup(
    name='nexus-admin',
    version='0.1',
    author='Jason Mayfield (mostly copied from David Cramer)',
    author_email='jwmayfield@gmail.com',
    url='http://github.com/jwmayfield/nexus-admin',
    description = 'Django Admin Plugin for Nexus',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'nexus>=0.1.1',
    ],
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
