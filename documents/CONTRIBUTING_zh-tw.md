# 貢獻 TGmeetup

[英文版](../CONTRIBUTING.md)

非常感謝您投入時間貢獻於 TGmeetup 專案！  
以下是有關於如何貢獻 TGmeetup 的指南。請您花點時間閱讀這份文件，透過這份文件，您會更了解如何簡單且有效的來進行貢獻的程序。  
我們有[行為守則](../CODE_OF_CONDUCT.md)，請您花點時間閱讀，這將會對於您投入此專案時，會有良好的互動。  
謝謝您的參與及貢獻。


## Table of Contents

- [Open issues](#open-issues)
    - [Request a community](#request-a-community)
    - [Bug reports](#bug-reports)
    - [Feature requests](#feature-requests)
- [Pull requests](#pull-requests)
    - [Add a community](#add-a-community)
    - [For new Contributors](#for-new-contributors)
    - [Tests](#tests)
- [Styleguides](#styleguides)
    - [Git Commit Messages](#git-commit-messages)
    - [Package.json format](#package.json-format)
    - [Use a Consistent Coding Style](#use-a-consistent-coding-style)
- [License](#license)

## Open issues

我們使用 GitHub issues 來追蹤公開的問題。透過建立 issue 來回報問題或是加技術社群的資訊是很容易的。我們主要以英文來描述問題。

### Request a community

在開 issue 請求添加新的技術社群時，請填寫相關的資訊與連結，方便讓人們知道。

### Bug reports

當 repo 的程式出現 BUG 時，請提出驗證。好的 Bug 回報是很有用的。謝謝！

Bug 回報指南：

1. **使用 GitHub issue 來搜尋** &mdash; 確認是否已經有存在的 issue 已經回報。

2. **確認是否有 issue 已經被修復** &mdash; 請嘗試使用 repository 中最新的 `master` 分支來重現它。

3. **隔離問題** &mdash; 建立一個簡單的測試範例。

一個好的錯誤報告不應該讓其他人請你提供更多的資訊。 請您盡量在報告中描述的越詳細越好。包含你的環境是什麼？哪些步驟會出現此問題？是在什麼作業系統下遇到問題？你期望的結果呢是什麼？這些細節將幫助人們修復任何一個潛在的錯誤。謝謝。

範例：

> Short and descriptive example bug report title
>
> A summary of the issue and the browser/OS environment in which it occurs. Ifsuitable, include the steps required to reproduce the bug.
>
> 1. The first step
> 2. The second step
> 3. etc.
>
>
> The other information you want to share that is relevant to the issue being reported. This might include the lines of code that you have identified as causing the bug, and potential solutions (and your opinions on their merits).

### Feature requests

我們歡迎功能的請求。但請您花一點時間，找出您的想法是否符合專案的範圍和目標。說服這個專案的開發者關於您這個功能的優點是一個很好的例子。 請您盡可能的提供更多的細節和內容。謝謝。

## Pull requests

發出 pull requests 是對 codebase 進行更動的最佳方式。(我們使用 [Github Flow](https://guides.github.com/introduction/flow/index.html)). 我們非常歡迎您的 pull requests:

1. Fork 本專案的 repo 並且從 `master` 建立你的分支
2. 如果你已經添加您的程式碼，請先測試過現有的測試，並且添加您的程式碼的測試。
3. 如果您有添加新功能，請一起更新 README 檔案。
4. 確保都有通過每一項測試。
5. 確保程式碼都為有效的程式。
6. 送出 pull request。

### Add a community

請參閱 [package.json.sample](package.json.sample)，這是一份 package.json 範例檔。要加入技術社群資訊，請依據以下順序進行。  
(再進行之前，請搜尋是否有存在的 pull request ，以及是否有相關的 issue，依據尊重原則，我們會保留先送 pull request 的貢獻者，若是後面有重複的 pull request，我們只能非常抱歉的請您關閉該重複的 pull request。若發現原貢獻者遲遲為修改該 pull request，還請您在該 pull request 留言詢問，倘若太久，我們也可以討論是否關閉原 pull request ，讓您重新送一個 pull request 進行貢獻，謝謝。)  
1. 找尋 [community](../community) 或 [conference](../conference) 目錄底下目前是否有該技術社群所存在的 country code ？如果有請到該目錄底下，沒有請建立一個新的 country code 資料夾。
2. 創建一個屬於該社群的目錄名(資料夾名稱)，目錄名應為一個英文單字，建議為該社群的縮寫，或是活動報名 URL 的社群名。
3. 進到該新建的目錄底下，並且建立一個新的檔案，檔案名為 package.json。
4. 編輯 package.json，請參閱[package.json.sample](package.json.sample) ，並請遵循 Json 格式。
   - 必要欄位有：`name`, `title`, `countrycode`, `city`, `keywords`, `registration`
   - 非必要欄位，但可以讓該社群資訊更豐富的欄位：`description`, `homepage`, `contact`, `contributors`, `repository`, `chat`, `social-media`
   - 以下為各欄位(key)介紹：
      - `name`: 必要欄位(object)，值(value)為一個字串，該字串的名稱需和該目錄資料夾同名，且為一個英文單字，建議為該社群的縮寫，或是活動報名 URL 的社群名。
      - `title`: 必要欄位(object)，值(value)為字串，該字串為該社群真正的名字，中間可以有空白。
      - `countrycode`: 必要欄位(object)，值(value)為字串，該 country code 須遵循 ISO 3166-1 alpha-2 的規範。
      - `category`: 必要欄位(object)，值(value)為字串，為 **community** 或 **conference**。
      - `city`: 必要欄位(object)，值(value)為字串，為城市的欄位。
      - `keywords`: 必要欄位(object)，值(value)為 List ，為搜尋的關鍵字，只要是與該技術社群相關的關鍵字，都可以放到這裡。請使用一個字一行，方便閱讀。
      - `registration`: 必要欄位(object)，值(value)為 Dictionary 。當中包含兩種key：
         - type: 該值(value)主要填入報名的平台名稱，目前只支援 Meetup 或 kktix，您也可填寫其他的平台名稱，待未來功能加入時，可以支援。
         - url: 為報名連結。
      - `description`: 非必要欄位(object)，值(value)為一個字串，為該技術社群的描述。
      - `homepage`: 非必要欄位(object)，值(value)為一個字串，為該社群的網站。
      - `contact`: 非必要欄位(object)，值(value)為一個字串，為該社群公開的聯繫方式。
      - `contributors`: 非必要欄位(object)，值(value)為一個字串，為該社群的維護者資訊。
      - `repository`: 非必要欄位(object)，值(value)為一個 Dictionary，為該社群的 Git repository，例如： GitHub 的 organization 主要連結。
      - `chat`: 非必要欄位(object)，值(value)為 List ，為該社群討論的平台連結。
      - `social_media`: 非必要欄位(object)，值(value)為 List ，為該技術社群的社群媒體連結。
      - `color`: 非必要欄位(object)，值(value)一個字串 ，為該技術社群的代表 Hex 色碼。
      - `logo_url`: 非必要欄位(object)，值(value)一個字串 ，為該技術社群的 logo URL。若上傳 logo 請放在同個社群目錄底下，並填上該圖片的檔名。
5. 編輯完畢後，請將該檔案存檔。依據 GitHub Flow 進行貢獻。 commit message 請參考以下範例描述。  
註一：`<>`請於您編輯該 commit message 的時候移除  
註二：`<group type>` = `community` 或 `conference`  
註三：若有關聯的 issue 請於該 commit message title(或 body) 後面加上 `, close #<issue number>` 或是 `, cc #<issue number>`。  
```
[<group type>] Add <countrycode>/<技術社群名稱>
```

### For new Contributors

如果您從未發送過 pull request ，歡迎參閱 [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github)，本篇的教學會幫助您了解如何送一個 pull request 的。

1. [Fork](http://help.github.com/fork-a-repo/) 本專案，clone 您 fork 的專案到您的本機端，並且設定您的 remotes:

   ```bash
   # Clone your fork of the repo into the current directory
   git clone https://github.com/<your-username>/<repo-name>
   # Navigate to the newly cloned directory
   cd <repo-name>
   # Assign the original repo to a remote called "upstream"
   git remote add upstream https://github.com/TGmeetup/<repo-name>
   ```

2. 如果您 clone 下來的專案有些過時，請從 upstream 取得最新的更新(最新的 commit):

   ```bash
   git checkout master
   git pull upstream master
   ```

3. 創建一個新的主題分支(不包含主要專案的開發分支）以包含您的功能、更改或修復：

   ```bash
   git checkout -b <topic-branch-name>
   ```

4. 請適當地確保更新或加入測試。沒有測試，我們將沒辦法接受修補或是新功能。請執行 `pytest` 來檢查您的程式是否有通過所有的測試。請到專案的 README 頁面的 `Testing` 取得更多的資訊。

5. Push 你的分支到您的 fork repository:

   ```bash
   git push origin <topic-branch-name>
   ```

6. 請到本專案的 GitHub 頁面 [TGmeetup repo](https://github.com/TGmeetup/TGmeetup) 並且 [開一個 Pull Request](https://help.github.com/articles/using-pull-requests/)，請在該 Pull request 中寫下清楚的標題與詳細的描述。


## Styleguides
### Git Commit Messages
- 請使用現在式 ("Add feature" 不是 "Added feature")
- 請使用祈使語氣 ("Move cursor to..." 不是 "Moves cursor to...")
- Commit message 的 subject line 請縮減於 50 個字元內
- Commit message 的 body 每一行請少於 72 字元內
- 在 commit message 中請關聯相關的 issue 或 pull requests 的編號

### Package.json format
請參閱範例 [package.json.sample](package.json.sample)，並請遵循它。  
同時，在 Json 的格式中，我們使用兩個空白作為縮排，請不要使用 tab 或是其他的縮排格式。  
必要的欄位包含：`name`, `title`, `countrycode`, `city`, `keywords`, `registration`.  

### Use a Consistent Coding Style
遵循 PEP8 的規則。

## License
在貢獻本專案時，您同意您的貢獻將依據 MIT 授權進行。謝謝！

