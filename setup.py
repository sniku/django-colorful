#!/usr/bin/env python

from setuptools import setup, find_packages

from colorful import VERSION

github_url = 'https://github.com/sniku/django-colorful'

setup(
    name='django-colorful',
    version='.'.join(str(v) for v in VERSION),
    description='An extension to the Django web framework that provides database and form color fields',
    long_description=open('README.markdown').read(),
    url=github_url,
    author='Pawel Suwala',
    author_email='pawel.suwala@fsfe.org',
    requires=[
        'Django (>=1.2)',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license='MIT License',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
