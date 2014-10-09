import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "testwatch",
    version = "0.0.1",
    author = "Cezar Berea",
    author_email = "berea.cezar@gmail.com",
    description = ("A watcher that runs tests when source files change"),
    license = "MIT",
    keywords = "Watch and re-run tests",
    url = "http://packages.python.org/",
    packages=['testwatch'],
    install_requires=['nose', 'pyinotify'],
    test_requires=[],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points = {
        'console_scripts': [
            'testwatch = testwatch:run'
        ]
    }
)
