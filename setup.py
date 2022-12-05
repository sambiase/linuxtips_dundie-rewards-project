import os.path

from setuptools import setup, find_packages


def read(*paths):
    """
    Reads the contents of a file in a Safe Way
    """

    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *paths)
    with open(filepath) as file_:
        return file_.read().strip()


def read_requirements(path):
    """
    Returns a list os Requirements from a Text File
    """
    # list comprehension that reads each line of a given file
    return [line.strip() for line in read(path).split('\n') if not line.startswith(('#', 'git+', '"', '-'))]


setup(
    name='Dundie',
    author='Sambiase',
    description='Reward Point System',
    long_description=read('README.md'),
    long_description_content_type = 'text/markdown',
    python_requires='>=3.9', # projeto somente roda em versoes maiores ou iguais a 3.9
    version='0.1.0',
    packages=find_packages(),  # o find_packages importa todos os subpacotes dentro de dundie que tenham o __init__.py
    # packages=['dundie'] usariamos assim caso quisessemos importar somente o pacote dundie

    # entry points é usado para poder executar o programa via CLI
    entry_points={
        'console_scripts': [
            'dundie = dundie.__main__:main'
        ]
    },
    install_requires=read_requirements('requirements.txt'),
    extra_require={
        'test': read_requirements('requirements.test.txt'),
        'dev': read_requirements('requirements.dev.txt')
    }
)
