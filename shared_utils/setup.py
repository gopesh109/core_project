from setuptools import setup, find_packages

setup(
    name='shared-utils',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'boto3>=1.20.0',
        'requests>=2.25.0',
    ],
)
