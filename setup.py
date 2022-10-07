from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-external-links-new-tabs",
    description="Datasette plugin to open external links in new tabs",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Jacob Weisz",
    url="https://github.com/ocdtrekkie/datasette-external-links-new-tabs",
    project_urls={
        "Issues": "https://github.com/ocdtrekkie/datasette-external-links-new-tabs/issues",
        "CI": "https://github.com/ocdtrekkie/datasette-external-links-new-tabs/actions",
        "Changelog": "https://github.com/ocdtrekkie/datasette-external-links-new-tabs/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License"
    ],
    version=VERSION,
    packages=["datasette_external_links_new_tabs"],
    entry_points={"datasette": ["external_links_new_tabs = datasette_external_links_new_tabs"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    python_requires=">=3.7",
)
