from setuptools import setup, find_packages

setup(name='vestibulum',
      version='0.1',
      description='Static gallery generator',
      url='https://github.com/malcodeman/Gallery-Generator',
      author='malcodeman',
      license=license,
      py_modules=['vestibulum/main'],
      packages=find_packages(exclude=('tests', 'docs')),
      entry_points = {
        'console_scripts': ['vesti build = vestibulum.main:main'],
      },
      zip_safe=False)
