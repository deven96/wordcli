import os
import sys
import setuptools
from setuptools.command.install import install

CURRENT_DIR = os.getcwd()
REQUIREMENTS = 'requirements.txt'
WIN_REQUIREMENTS = 'win-requirements.txt'
requires = [line.strip('\n') for line in open(REQUIREMENTS).readlines()]
with open("README.md", "r") as fh:
    long_description = fh.read()

windows_requires = [line.strip('\n') for line in open(WIN_REQUIREMENTS).readlines()]

VERSION = "0.1.1"

setuptools.setup(
    name="WordCLI",
    version=VERSION,
    author='Diretnan Domnan',
    author_email="diretnandomnan@gmail.com",
    description="WordCLI is a command line interface to interact with the popular WORDNET corpus",
    url="https://github.com/deven96/wordcli",
    packages=setuptools.find_packages(),
    # install_requires=requires,
    # install windows requirements
    install_requires= requires+windows_requires if sys.platform.startswith('win') \
                    else requires,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU",
    keywords='nltk dictionary wordnet commandline',
    classifiers=(
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    # move script depending on platform
    entry_points={
                  'console_scripts': [
                      'wordcli=wordcli.cli:main'
                  ]
              },
    package_data={
        '': ['*.*'],
    },
    test_suite='nose.collector',
    tests_require=['nose'],
    include_package_data=True,
    zip_safe=True,
)

# nltk should be available now
from wordcli.utils import download_corpus
download_corpus()