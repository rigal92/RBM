from setuptools import setup, find_packages

setup(
    name='RBM',
    version='1.0.0',
    author='RG',
    description='RBM handling',
    packages=find_packages(),    
    install_requires=['numpy', 'matplotlib','pandas'],
)