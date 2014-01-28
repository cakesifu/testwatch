import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "nosewatch",
    version = "0.0.1",
    author = "Cezar Berea",
    author_email = "berea.cezar@gmail.com",
    description = ("An demonstration of how to create, document, and publish "
                                   "to the cheese shop a5 pypi.org."),
    license = "BSD",
    keywords = "Watch and re-run nosetests",
    url = "http://packages.python.org/",
    packages=['nosewatch', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    entry_points = {
        'console_scripts': [
            'nosewatch = nosewatch:run'
        ]
    }
)
