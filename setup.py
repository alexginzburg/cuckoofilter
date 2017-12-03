# coding=utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = '1.0'
__author__ = 'Jiawen Guan'

with open('README.md') as f:
    readme = f.read()


setup(name='cuckoofilter',
      version=__version__,
      description='Cuckoo Filter implementation using Python',
      long_description=readme,
      author=__author__,
      author_email='jesus.jiawen@gmail.com',
      url='https://github.com/shenaishiren/cuckoofilter',
      license='GPL-3.0',
      packages=['cuckoofilter'],
      install_requires=["mmh3"],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'License :: OSI Approved :: General Public License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6'
      ],
)