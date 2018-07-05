# TGmeetup

[![Build Status](https://api.travis-ci.org/TGmeetup/TGmeetup.svg?branch=master)](https://travis-ci.org/TGmeetup/TGmeetup)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.me/tgmeetup/5)

[英文版](../README.md)

> 一個搜集與整合技術類社群的專案

這是一個搜集與整合技術類社群的專案。我們搜集所有有關於社群的資訊，並透過大家的 Meetup 連結（如：Meetup, KKTIX...），透過 API 拿取最新的活動資訊。讓大家取得社群資訊以及社群的活動資訊的專案。

![](../imgs/output.gif)

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
這專案可執行於 Unix-like 與 MacOS 系統上，並且需要有 python3 的環境。
```sh
$ sudo apt install python-setuptools
$ git clone https://github.com/TGmeetup/TGmeetup.git
$ cd TGmeetup
$ cp API.cfg.sample API.cfg
$ make install
```
請注意：
1. 請到 Meetup API 註冊 OAuth consumer: https://secure.meetup.com/meetup_api/oauth_consumers/create/  。這邊為操作說明： https://hackmd.io/s/ByrxYmi4G 。
2. 如果您無法執行 `make install`，請執行 `sh install.sh`。

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
$ sudo apt install python-setuptools
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

### Code style
遵循 PEP8 規則
```sh
autopep8 --in-place --aggressive --max-line-length=88 <filename>
```

### Tests
使用 `pytest` 進行測試。

## Contributors
謝謝貢獻者們，您可以到 https://github.com/TGmeetup/TGmeetup/graphs/contributors 看到他們。

## Contribute
歡迎您隨意[開 issue](https://github.com/RichardLitt/standard-readme/issues/new) 或送 PR 唷！
若您想要送 PR 到 TGmeetup ，請您先看看 [CONTRIBUTING.md](CONTRIBUTING_zh-tw.md)。這些內容可以幫助您更快了解如何貢獻本專案。謝謝您的加入！

## Communication
- [TGmeetup 網站](https://tgmeetup.github.io/)
- [Telegram 群](https://t.me/tgmeetup)

## License
MIT
