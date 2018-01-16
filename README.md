# TGmeetup

[![Build Status](https://travis-ci.org/TGmeetup/TGmeetup.svg?branch=master)](https://travis-ci.org/TGmeetup/TGmeetup)

[中文版](documents/README_zh-tw.md)

> A collection set of technical groups' information

This is a collection set of technical groups' meetup. Collect the technical meetup information and get the activity from meetup platform, such as Meetup, KKTIX ... etc. The user can use this tool to find technical meetup and attend it.

![](header.png)

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
- [License](#license)


## Background
因應不論是台灣或是各地，技術類的社群林立，但發現現今有以下的幾種情況：
- 對於一般使用者
   1. 不知道社群相關資訊，不知道從何找起
   2. 想要參加，但不知道附近有哪些社群可以參加，以及社群的資訊與文化是如何？
   3. 跨領域中，想透過參與社群讓自己抓到可以學習方向，但不知道該領域的社群有哪些
   4. 想知道附近有哪些社群近期有聚會，而不是就自己所知的社群一個一個搜尋
- 社群維護者
   1. 太多社群活動，不想和其他社群撞期，只能以自身所知的社群來搜集活動資訊
   2. 想知道同類型的社群，大家辦的活動都是什麼主題
...
很多的情況，雖然人工都可以花點時間進行，但是如果有一個整合平台，那大家就不用那麼辛苦的搜集。
因此，建立的 TGmeetup 專案，搜集各地的社群資訊，透過活動報名平台的 API ，來取得大家的活動資訊，讓大家方便搜尋。而公開的社群 package.json 資訊，也讓大家可以維護相關的資訊，並取得有用的訊息。

## Install
This project uses python3 on Unix-like and MacOS. Go check them out if you don't have them locally installed.
```sh
$ git clone https://github.com/sufuf3/TGmeetup.git
$ cd TGmeetup
$ cp API.cfg.sample API.cfg
$ make install
```
Note: Please ADD YOUR MEETUP KEY into API.cfg.

## Usage
```sh
usage: tgmeetup [-h] [-u] [-c COUNTRY] [-t CITY] [-n NAME] [-k KEYWORD]

TGmeetup

optional arguments:
  -h, --help            show this help message and exit
  -u, --update          Update the events.json infomation.
  -c COUNTRY, --country COUNTRY
                        This is a country code which follow ISO 3166-1
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
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

### Code style
Follow PEP 8
```sh
autopep8 --in-place --aggressive --aggressive <filename>
```

### Tests
Describe and show how to run the tests with code examples.

## Contributors
Thanks to these contributors, you can see them all here: https://github.com/TGmeetup/TGmeetup/graphs/contributors

## Contribute
Feel free to dive in! [Open an issue](https://github.com/RichardLitt/standard-readme/issues/new) or submit PRs.
To submit PRs to TGmeetup, please refer to [CONTRIBUTING.md](). It should contain most of the things you'll need to get your contribution started!


## License
MIT
