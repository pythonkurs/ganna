from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='ganna',
      version=version,
		scripts = ['scripts/getting_data.py','scripts/check_repo.py'],
      description="Exercise 2 - NY trasportation",
      long_description="""\
Calculate fraction of escalator that needs to be repared""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='andrea ganna',
      author_email='andrea.ganna@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
