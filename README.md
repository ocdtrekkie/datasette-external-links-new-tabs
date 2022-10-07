# datasette-external-links-new-tabs

[![PyPI](https://img.shields.io/pypi/v/datasette-external-links-new-tabs.svg)](https://pypi.org/project/datasette-external-links-new-tabs/)
[![Changelog](https://img.shields.io/github/v/release/ocdtrekkie/datasette-external-links-new-tabs?include_prereleases&label=changelog)](https://github.com/ocdtrekkie/datasette-external-links-new-tabs/releases)
[![Tests](https://github.com/ocdtrekkie/datasette-external-links-new-tabs/workflows/Test/badge.svg)](https://github.com/ocdtrekkie/datasette-external-links-new-tabs/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/ocdtrekkie/datasette-external-links-new-tabs/blob/main/LICENSE)

Datasette plugin to open external links in new tabs

## Installation

Install this plugin in the same environment as Datasette.

    datasette install datasette-external-links-new-tabs

## Usage

There are no usage instructions, it simply opens external links in a new tab.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-external-links-new-tabs
    python3 -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
