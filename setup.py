import setuptools
from distutils.core import setup

entry_points = {
    'console_scripts': [
        'tgmeetup = TGmeetup.tgmeetup:main'
    ]
}

setup(
  name='tgmeetup',
  packages=['TGmeetup', 'TGmeetup.libs', 'TGmeetup.libs.RegistrationAPI'],
  version='0.2.1',
  description='A collection set of technical groups information',
  author='Samina Fu',
  author_email='sufuf3@gmail.com',
  url='https://github.com/sufuf3/TGmeetup',
  keywords=['TechGroup', 'TGmeetup', 'meetup', 'community'],
  install_requires=["requests", "ConfigParser", "pathlib", "terminaltables", "termcolor", "geocoder"],
  entry_points=entry_points,
)
