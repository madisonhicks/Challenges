"""
Simple setup for challenges
"""

from setuptools import setup, find_packages


NAME = 'challenges'
URL = 'https://github.com/madisonhicks/Challenges'
AUTHOR = 'Madison Hicks & Matthew Planchard'
EMAIL = 'madison.carlisle.hicks@gmail.com'

SHORT_DESC = 'fun coding challenges'
LONG_DESC = SHORT_DESC
KEYWORDS = []

PACKAGE_DEPENDENCIES = [
    'ipdb',
    'pytest',
]
SETUP_DEPENDENCIES = []
TEST_DEPENDENCIES = []
EXTRAS_DEPENDENCIES = {}

ENTRY_POINTS = {}


# See https://pypi.python.org/pypi?%3Aaction=list_classifiers for all
# available setup classifiers
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    # 'Development Status :: 5 - Production/Stable',
    # 'Environment :: Web Environment',
    'Intended Audience :: Developers'
    # 'License :: Other/Proprietary License',
    # 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.6'
]


__version__ = '0.1.0'


setup(
    name=NAME,
    version=__version__,
    description=SHORT_DESC,
    long_description=LONG_DESC,
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    packages=find_packages(exclude=['*.tests', '*.tests.*']),
    install_requires=PACKAGE_DEPENDENCIES,
    setup_requires=SETUP_DEPENDENCIES,
    tests_require=TEST_DEPENDENCIES,
    extras_require=EXTRAS_DEPENDENCIES,
)
