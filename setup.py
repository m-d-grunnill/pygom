#!/bin/env python
"""
@author: Edwin Tye (Edwin.Tye@phe.gov.uk)
"""
import re
import subprocess
import numpy
from setuptools import setup
from setuptools.extension import Extension

## For the cython parts ###
try:
    from Cython.Distutils import build_ext
except ImportError:
    use_cython = False
else:
    use_cython = True

cmdclass = { }
ext_modules = [ ]

#For this to work the .c files are not include in GIT except in the release
#release branch (the c files would be created using python setup.py sdist)
if use_cython:
    ext_modules += [
        Extension("pygom.model._tau_leap",
                  ["pygom/model/_tau_leap.pyx"],
                  include_dirs=[numpy.get_include()],
#                  extra_compile_args=['-fopenmp'],
#                  extra_link_args=['-fopenmp']),
)
    ]
    cmdclass.update({ 'build_ext': build_ext })
else:
    ext_modules += [
        Extension("pygom.model._tau_leap",
                  [ "pygom/model/_tau_leap.c" ],
                  include_dirs=[numpy.get_include()],
#                  extra_compile_args=['-fopenmp'],
#                  extra_link_args=['-fopenmp']),
)
    ]
package_data={
   'pygom.data': ['eg1.json'],# An example epijson file
   }


with open('LICENSE.txt', 'r') as f:
    license_file = f.read()

with open('README.rst', 'r') as f:
    readme = f.read()

setup_requires=[
    'setuptools-scm>=3.2.0',
    'setuptools_scm_git_archive'
    ]

install_requires = [
    'dask>=0.13.0',
    'matplotlib>=1.0.0',
    'pandas>=0.15.0',
    'python-dateutil>=2.0.0',
    'python-libsbml>=5.0.0',
    'numpy>=1.6.0',
    'scipy>=0.10.0',
    'sympy>=1.0.0',
    'cython>=0.29'
]

setup(
    name='pygom',
    use_scm_version=True,
    description='ODE modeling in Python',
    long_description=readme,
    license=license_file,
    url='https://github.com/PublicHealthEngland/pygom',
    author="Edwin Tye",
    author_email="Edwin.Tye@phe.gov.uk",
    packages=[
        'pygom',
        'pygom.model',
        'pygom.model.ode_utils',
        'pygom.loss',
        'pygom.utilR'
    ],
    package_data = package_data,
    include_package_data=True,
    cmdclass = cmdclass,
    ext_modules=ext_modules,
    install_requires=install_requires,
    setup_requires=setup_requires,
    test_suite='tests',
    scripts=[]
    )
