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
  description='A collection set of technical groups information',
  author='Samina Fu',
  author_email='sufuf3@gmail.com',
  url='https://github.com/sufuf3/TGmeetup',
  keywords=['TechGroup', 'TGmeetup', 'meetup', 'community'],
  setup_requires=["requests"],
  entry_points=entry_points,
)
