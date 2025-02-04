from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in damas_custom/__init__.py
from damas_custom import __version__ as version

setup(
	name="damas_custom",
	version=version,
	description="Damas",
	author="Osama",
	author_email="it@damascenter.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
