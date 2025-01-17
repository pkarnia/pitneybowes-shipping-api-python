# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@pb.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "PitneyBowesShippingAPI"
VERSION = "1.0.3"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Shipping API",
    author="OpenAPI Generator community",
    author_email="support@pb.com",
    url="https://github.com/PitneyBowes/pitneybowes-shipping-api-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Shipping API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description="""\
    Pitney Bowes Shipping API Package.  # noqa: E501
    """
)
