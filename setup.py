import setuptools
from distutils.core import setup

entry_points = {
    'console_scripts': [
        'TGmeetup = TGmeetup.tgmeetup:main'
    ]
}

setup(
  name='TGmeetup',
  packages=['TGmeetup'],
  version='0.1.0',
  description='technical group meetup',
  author='sufuf3',
  author_email='sufuf3@gmail.com',
  url='https://github.com',
  keywords=['TechGroup', 'TGmeetup', 'meetup'],
  classifiers=[],
  setup_requires=['pytest-runner'],
  tests_require=['pytest'],
  entry_points=entry_points,
)
