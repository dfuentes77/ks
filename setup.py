# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name = "ks",
    version='0.1',
    packages = ["ks"],
    install_requires=[
        'Click',
        'baluhn',
        'scripttest',
        'nose',
    ],
    entry_points = {
        "console_scripts": ['ks = ks.ks:main']
        },
    description = "Kickstarter command line tool.",
    author = "Damian Fuentes",
    author_email = "dfuentes77@gmail.com",
    )

