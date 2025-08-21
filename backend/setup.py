#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='planning',
    version='0.0.1',
    description='Planning Backend',
    author='Jeremy',
    packages=find_packages("src"),
    package_dir={'': 'src'},
    install_requires=[
        "Django==5.2",
        "daphne==4.1.2",
        "channels==4.2.2",
        "channels_redis==4.2.1",
        "djangorestframework==3.16.0",
        "djangorestframework_simplejwt==5.5.0",
        "django-redis==5.4.0",
        "PyMySQL==1.1.1",
    ],
    extras_require={
        'dev': [
            'black==25.1.0',
            'flake8==7.2.0',
            'ipython==8.35.0',
            'websocket-client==1.8.0',
        ],
    },
    zip_safe=True
)
