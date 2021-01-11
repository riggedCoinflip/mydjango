from setuptools import setup, find_packages

setup(
    name='My Site',
    version='0.0.1',

    package_dir={'': 'src'},
    packages=find_packages('src'),

    install_requires=['django', 'psycopg2'],  # add other dependencies here
)