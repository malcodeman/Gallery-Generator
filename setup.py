from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name='vestibulum',
      version='0.1',
      description='Static gallery generator',
      long_description=readme,
      url='https://github.com/malcodeman/Vestibulum',
      author='malcodeman',
      license=license,
      py_modules=['vestibulum/main'],
      packages=find_packages(exclude=('tests', 'docs')),
      entry_points = {
        'console_scripts': ['vestibulum = vestibulum.main:main'],
      },
      zip_safe=False)
