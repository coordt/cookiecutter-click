#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is used to create the package we'll publish to PyPI.
"""

import os
from m2r import parse_from_file
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


def parse_reqs(filepath):
    with open(filepath, 'r') as f:
        reqstr = f.read()
    requirements = []
    for line in reqstr.splitlines():
        line = line.strip()
        if line == '':
            continue
        elif not line or line.startswith('#'):
            # comments are lines that start with # only
            continue
        elif line.startswith('-r') or line.startswith('--requirement'):
            _, new_filename = line.split()
            new_file_path = os.path.join(os.path.dirname(filepath or '.'),
                                         new_filename)
            requirements.extend(parse_reqs(new_file_path))
        elif line.startswith('-f') or line.startswith('--find-links') or \
                line.startswith('-i') or line.startswith('--index-url') or \
                line.startswith('--extra-index-url') or \
                line.startswith('--no-index'):
            continue
        elif line.startswith('-Z') or line.startswith('--always-unzip'):
            continue
        else:
            requirements.append(line)
    return requirements


version = "{{cookiecutter.project_version}}"
readme = open('README.rst').read()
history = parse_from_file('CHANGELOG.md')


setup(
    name="{{cookiecutter.project_name}}",
    description="{{cookiecutter.project_description}}",
    long_description=readme + '\n\n' + history,
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    version=version,
    install_requires=parse_reqs('requirements.txt'),
    entry_points="""
    [console_scripts]
    {{cookiecutter.cli_name}}={{cookiecutter.package_name}}.cli:cli
    """,
    python_requires=">={{cookiecutter.python_version}}",
    license={% if cookiecutter.license != "None" %}"{{cookiecutter.license}}"{% else %}None{% endif %},  # noqa
    author= "{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    url= "https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.package_name}}",
    keywords=[
        # Add package keywords here.
    ],
    # See https://PyPI.python.org/PyPI?%3Aaction=list_classifiers
    classifiers=[
      # How mature is this project? Common values are
      #   3 - Alpha
      #   4 - Beta
      #   5 - Production/Stable
      'Development Status :: 3 - Alpha',

      # Indicate who your project is intended for.
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Libraries',

      # Pick your license.  (It should match "license" above.)
      {% if cookiecutter.license != 'None' %}  # noqa
      '''License :: OSI Approved :: {{cookiecutter.license}} License''',
      {%endif%}  # noqa
      # Specify the Python versions you support here. In particular, ensure
      # that you indicate whether you support Python 2, Python 3 or both.
      'Programming Language :: Python :: {{cookiecutter.python_version}}',
    ],
    include_package_data=True
)
