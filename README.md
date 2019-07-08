# TGmeetup

[![Build Status](https://api.travis-ci.org/TGmeetup/TGmeetup.svg?branch=master)](https://travis-ci.org/TGmeetup/TGmeetup)
[![Financial Contributors on Open Collective](https://opencollective.com/TGmeetup/all/badge.svg?label=financial+contributors)](https://opencollective.com/TGmeetup) [![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.me/tgmeetup/5)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FTGmeetup%2FTGmeetup.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2FTGmeetup%2FTGmeetup?ref=badge_shield)

[中文版](documents/README_zh-tw.md)

> A collection set of technical groups' information

This is a collection set of technical groups' meetup. Collect the technical meetup information and get the activity from meetup platform, such as Meetup, KKTIX ... etc. The user can use this tool to find technical meetup and attend it.

![](imgs/output.gif)

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Development setup](#development-setup)
    - [Guide](#guide)
    - [Code style](#code-style)
    - [Tests](#tests)
- [Contributors](#contributors)
- [Contribute](#contribute)
- [Communication](#communication)
- [License](#license)


## Background
There are lots of technical communities all over the world, but the following problems come with that.
- For attendants
    1. Have no idea to find communities' info.
    2. The desire to attend communities, but don't know the neighbouring communities which they may attend and the information and culture of the communities.
    3. Would like to know the upcoming meetups around them, instead of searching in known communities.
- For maintainers
    1. It's hard to prevent from clashing with other communities meetups.
    2. Hope to know other communities' which are in the similar field topic.

If there were a platform collecting that information, people can save a lot of time.
Thus, TGmeetup project collects the communities' and activities' information thru the registration platform's API, and make it much easier to search for the information which hit the spot. Besides, the package.json files describing the public communities are good for maintaining.

## Install
This project uses python3 on Unix-like and MacOS. Go check them out if you don't have them locally installed.
```sh
$ sudo apt install python-setuptools
$ git clone https://github.com/TGmeetup/TGmeetup.git
$ cd TGmeetup
$ cp API.cfg.sample API.cfg
$ make install
```
Note: 
1. Please ADD YOUR MEETUP KEY into API.cfg.
2. If you can't run `make install`, please run `sh install.sh`.

## Usage
```sh
usage: tgmeetup [-h] [-u] [-c COUNTRY] [-t CITY] [-n NAME] [-k KEYWORD]

TGmeetup

optional arguments:
  -h, --help            show this help message and exit
  -u, --update          Update the events.json infomation.
  -c COUNTRY, --country COUNTRY
                        This is a country code which follows ISO 3166-1
                        alpha-2.
  -t CITY, --city CITY  This is a city name.
  -n NAME, --name NAME  This is a community short name.
  -k KEYWORD, --keyword KEYWORD
                        This is a keyword of community. This could help find
                        the related community.
```

## Development setup

### Guide
```sh
$ sudo apt install python-setuptools
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

### Code style
Follow PEP 8
```sh
autopep8 --in-place --aggressive --max-line-length=88 <filename>
```

### Tests
Using `pytest`.

## Contributors
Thanks to these contributors, you can see them all here: https://github.com/TGmeetup/TGmeetup/graphs/contributors

## Contribute
Feel free to dive in! [Open an issue](https://github.com/TGmeetup/TGmeetup/issues/new) or submit PRs.
To submit PRs to TGmeetup, please refer to [CONTRIBUTING.md](CONTRIBUTING.md). It should contain most of the things you'll need to get your contribution started!

## Communication
- [TGmeetup website](https://tgmeetup.github.io/)
- [Community/Developer Telegram Group](https://t.me/tgmeetup)
- [HelloGitHub vol‧29](https://hellogithub.com/periodical/volume/29/#TGmeetup)

## Contributors

### Code Contributors

This project exists thanks to all the people who contribute. [[Contribute](CONTRIBUTING.md)].
<a href="https://github.com/TGmeetup/TGmeetup/graphs/contributors"><img src="https://opencollective.com/TGmeetup/contributors.svg?width=890&button=false" /></a>

### Financial Contributors

Become a financial contributor and help us sustain our community. [[Contribute](https://opencollective.com/TGmeetup/contribute)]

#### Individuals

<a href="https://opencollective.com/TGmeetup"><img src="https://opencollective.com/TGmeetup/individuals.svg?width=890"></a>

#### Organizations

Support this project with your organization. Your logo will show up here with a link to your website. [[Contribute](https://opencollective.com/TGmeetup/contribute)]

<a href="https://opencollective.com/TGmeetup/organization/0/website"><img src="https://opencollective.com/TGmeetup/organization/0/avatar.svg"></a>
<a href="https://opencollective.com/TGmeetup/organization/1/website"><img src="https://opencollective.com/TGmeetup/organization/1/avatar.svg"></a>
<a href="https://opencollective.com/TGmeetup/organization/2/website"><img src="https://opencollective.com/TGmeetup/organization/2/avatar.svg"></a>
<a href="https://opencollective.com/TGmeetup/organization/3/website"><img src="https://opencollective.com/TGmeetup/organization/3/avatar.svg"></a>
<a href="https://opencollective.com/TGmeetup/organization/4/website"><img src="https://opencollective.com/TGmeetup/organization/4/avatar.svg"></a>
<a href="https://opencollective.com/TGmeetup/organization/5/website"><img src="https://opencollective.com/TGmeetup/organization/5/avatar.svg"></a>
<a href="https://opencollective.com/TGmeetup/organization/6/website"><img src="https://opencollective.com/TGmeetup/organization/6/avatar.svg"></a>
<a href="https://opencollective.com/TGmeetup/organization/7/website"><img src="https://opencollective.com/TGmeetup/organization/7/avatar.svg"></a>
<a href="https://opencollective.com/TGmeetup/organization/8/website"><img src="https://opencollective.com/TGmeetup/organization/8/avatar.svg"></a>
<a href="https://opencollective.com/TGmeetup/organization/9/website"><img src="https://opencollective.com/TGmeetup/organization/9/avatar.svg"></a>

## License
MIT


[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FTGmeetup%2FTGmeetup.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2FTGmeetup%2FTGmeetup?ref=badge_large)
