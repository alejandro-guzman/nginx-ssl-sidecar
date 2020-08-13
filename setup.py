from setuptools import setup, find_packages

setup(
    name='simple-api',
    version='0.1.0',
    author='Alejandro Guzman',
    author_email='',
    description='An example hello world app',
    long_description=open('README.md').read(),
    url='https://github.com/alejandro-guzman/',
    license='MIT',
    keywords='flask api example',
    packages=find_packages(),
    install_requires=[
        'flask'
    ],
    entry_points={
        'console_scripts': ['simple-api=simpleapi.app:main'],
    },
    project_urls={
        'Source Code': 'https://github.com/alejandro-guzman/',
    },
    python_requires='>=3.7'
)