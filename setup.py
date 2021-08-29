from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in workout_club_management/__init__.py
from workout_club_management import __version__ as version

setup(
	name="workout_club_management",
	version=version,
	description="Workout Club Management",
	author="z1 flexible solution",
	author_email="info@flexiblesolution.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
