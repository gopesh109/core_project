from setuptools import setup, find_packages

setup(
    name='django-core',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Django>=3.2,<4.0',
        'gunicorn>=20.0.0',
        'shared-models',
        'shared-utils',
    ],
)
