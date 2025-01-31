from setuptools import setup, find_packages

setup(
    name='PyArchitecture',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python library for architectural design and simulation.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/pyarchitecture',
    license='MIT',
)
