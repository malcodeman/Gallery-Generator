import setuptools


def readme():
    with open('README.md') as f:
        return f.read()


setuptools.setup(name='pygram',
                 version='0.1',
                 description='Static gallery generator',
                 long_description=readme(),
                 url='https://github.com/malcodeman/pygram',
                 author='malcodeman',
                 packages=setuptools.find_packages(),
                 entry_points={
                     'console_scripts': ['pygram = pygram.main:main'],
                 },
                 zip_safe=False)
