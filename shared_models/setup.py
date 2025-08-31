from setuptools import setup, find_packages

setup(
    name='shared-models',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Django>=3.2,<4.0',
        'psycopg2-binary>=2.9.0',
    ],
)
