# setup.py

from setuptools import setup, find_packages

setup(
    name='john',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['requests'],  # Add any other dependencies here
    author='Your Name',
    author_email='your.email@example.com',
    description='Interface with different AI models',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/john',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
