import os
import sys

from setuptools import find_packages, setup
from setuptools.command.install import install


VERSION = "0.1.0"
DESCRIPTION = open("README.md", encoding="utf-8").read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""

    description = "verify that the git tag matches our version"

    def run(self):
        tag = os.getenv("CIRCLE_TAG")

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(tag, VERSION)
            sys.exit(info)


setup(
    name="django-runtime-options",
    version=VERSION,
    packages=find_packages(exclude=["tests"]),
    url="https://github.com/pennlabs/django-runtime-options",
    project_urls={
        "Changelog": ("https://github.com/pennlabs/django-runtime-options/blob/master/CHANGELOG.md")
    },
    license="MIT",
    author="Penn Labs",
    author_email="admin@pennlabs.org",
    description="Penn Labs example description",
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    install_requires=["django>=2.0.0"],
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.6",
    cmdclass={"verify": VerifyVersionCommand},
)