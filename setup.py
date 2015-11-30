from setuptools import setup, find_packages


setup(
    name='CapitainsFlint',
    version="0.0.1dev",
    description='Ingest and retrieve for Capitains Resources',
    url='http://github.com/Capitains/Flint',
    author='Thibault Clérice',
    author_email='leponteineptique@gmail.com',
    license='MIT',
    packages=find_packages(exclude=("tests")),
    install_requires=[
        "MyCapytain==0.0.9",
    ],
    entry_points={
        'console_scripts': ['cflint=CapitainsFlint.cmd:cmd'],
    },
    test_suite="tests",
    zip_safe=False
)
