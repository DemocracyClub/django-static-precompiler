from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import os
import sys


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    if sys.version < '3':
        return open(path).read()
    return open(path, encoding="utf-8").read()


README = read('README.rst')
CHANGES = read('CHANGES.rst')

setup(
    name="django-static-precompiler",
    packages=find_packages(),
    version="0.8",
    author="Andrey Fedoseev",
    author_email="andrey.fedoseev@gmail.com",
    url="https://github.com/andreyfedoseev/django-static-precompiler",
    description="Django template tags to compile all kinds of static files "
                "(SASS, LESS, CoffeeScript).",
    long_description="\n\n".join([README, CHANGES]),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords=["sass", "scss", "less", "css", "coffeescript", "javascript"],
    tests_require=[
        "pytest",
        "pytest-django",
        "pretend",
    ],
    cmdclass={
        "test": PyTest
    },
)
