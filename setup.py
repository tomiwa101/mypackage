from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='DATASCIENCE Solution python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/tomiwa101/mypackage',
    author='Tomiwa',
    author_email='bentommie22@gmail.com'
)