from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in properties_integration/__init__.py
from properties_integration import __version__ as version

setup(
	name="properties_integration",
	version=version,
	description="Properties Managment",
	author="Jenan Alfahham",
	author_email="jenan_fh95@hotmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
