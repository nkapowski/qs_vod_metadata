from setuptools import setup, find_packages
import sys
from distutils.core import setup
import py2exe

long_description = (
    "This project contains a library and tools for manipulating and "
    "generating metadata files that conform to the CableLabs VOD Metada 1.1 "
    "specification"
)

# Install requires config parser for Python 2.x
if sys.version_info[0] < 3:
    install_requires = ['configparser']
    tests_require = ['mock']
else:
    install_requires = []
    tests_require = []

    name='qs_vod_metadata',
    version='2016.1.6',
    license='MIT',
    #url='https://github.com/bbayles/vod_metadata',
    url = 'https://bitbucket.org/quicksisver_dev_phase_1/metadata_gen/src',
	download_url = 'https://bitbucket.org/quicksisver_dev_phase_1/metadata_gen/src',
    description='CableLabs VOD Metadata 1.1 library and tools',
    long_description="Library and tools for CableLabs VOD Metadata 1.1",

    author='Bo Bayles',
    author_email='bbayles@gmail.com',
    maintainer='Natalie Kapovski',
    maintainer_email='natalie@latto.tv',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Telecommunications Industry',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    keywords='cablelabs vod metadata',

    packages=find_packages(exclude=[]),
    test_suite='tests',

    install_requires=install_requires,
    tests_require=tests_require,

    package_data={'qs_vod_metadata': ["*.ini", "*.mp4", "*.pth", "*.xml"]},