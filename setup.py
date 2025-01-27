import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="flaskr",
    version="1.0.0",
    url="https://flask.palletsprojects.com/tutorial/",
    license="BSD",
    maintainer="Madhur Chaini",
    maintainer_email="madhurchaini@gmail.com",
    description="The basic blog app built in the Flask tutorial.",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"],
)
