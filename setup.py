from setuptools import setup, find_packages

setup(
    name='Dundie',
    author='Sambiase',
    description='Reward Point System',
    version='0.1.0',
    packages=find_packages(), # o find_packages importa todos os subpacotes dentro de dundie que tenham o __init__.py
    # packages=['dundie'] usariamos assim caso quisessemos importar somente o pacote dundie
)
