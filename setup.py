from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sga_chits/__init__.py
from sga_chits import __version__ as version

setup(
	name="sga_chits",
	version=version,
	description="SGA Chit Management",
	author="White Hat Global",
	author_email="rk@whitehatglobal.org",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
