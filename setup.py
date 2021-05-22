from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='pitone',
    version='0.0.0',
    description='__template__',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Pitone',
    author_email='pitone@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='Sunday Trader',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.7, <4',
    install_requires=[],
    extras_require={
        'dev': [],
    },
    scripts=[],
)
