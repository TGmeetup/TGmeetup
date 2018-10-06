# Contributing to TGmeetup

[中文版](documents/CONTRIBUTING_zh-tw.md)

Thanks for taking the time to contribute!
The following is a set of guidelines for contributing to TGmeetup. Please take a moment to review this document in order to make the contribution process easy and effective for everyone involved.

Please note we have a [code of conduct](CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.

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

We use GitHub issues to track public bugs. Report a bug by opening a new issue; it's that easy!

### Request a community

For the new community request issue, please fill in the information of the community to let people know.

### Bug reports

A bug is a _demonstrable problem_ that is caused by the code in the repository. Good bug reports are extremely helpful - thank you!

Guidelines for bug reports:

1. **Use the GitHub issue search** &mdash; check if the issue has already been reported.

2. **Check if the issue has been fixed** &mdash; try to reproduce it using the latest `master` branch in the repository.

3. **Isolate the problem** &mdash; ideally create a reduced test case.

A good bug report shouldn't leave others needing to chase you up for more information. Please try to be as detailed as possible in your report. What is your environment? What steps will reproduce the issue? What OS experiences the problem? What would you expect to be the outcome? All these details will help people to fix any potential bugs.

Example:

> Short and descriptive example bug report title
>
> A summary of the issue and the browser/OS environment in which it occurs. If suitable, include the steps required to reproduce the bug.
>
> 1. The first step
> 2. The second step
> 3. etc.
>
>
> The other information you want to share that is relevant to the issue being reported. This might include the lines of code that you have identified as causing the bug, and potential solutions (and your opinions on their merits).

### Feature requests

Feature requests are welcome. But take a moment to find out whether your idea fits with the scope and aims of the project. It would make a strong case to convince the project's developers of the merits of this feature. Please provide as much detail and context as possible.

## Pull requests

Pull requests are the best way to propose changes to the codebase (we use [Github Flow](https://guides.github.com/introduction/flow/index.html)). We actively welcome your pull requests:

1. Fork the repo and create your branch from `master`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

### Add a community

Please read [package.json.sample](documents/package.json.sample) which is a sample package.json. If you would like to add a technical group information, please follow the following steps.
(Please search the existing pull request or issue before you make your contribution. According to respect rule, we would keep the earlier pull request. If there is a duplicated pull request, we will close it and sorry for the inconvenience. However, if the contributor does not revise the pull request for a long time, you could leave a message to ask how to improve the pull request. We can discuss this, maybe close the origin pull request and let you send a new one to improve it. Many thanks.)
1. Please search the country code of technical group which under [community](community) or [conference](conference) folder. If there is a country code, please move to under the folder, otherwise, please create a folder with country code.
2. Create a folder of the technical group name, the folder name should be an English word. Using the abbreviation of the technical group or the registration URL of the group is a suggestion.
3. Create a new file which under this folder and name it as package.json.
4. Edit package.json. Please read [package.json.sample](documents/package.json.sample) and follow the Json format.
   - Required fields: `name`, `title`, `countrycode`, `city`, `keywords`, `registration`
   - Non-Required fields, but can enrich information of technical group: `description`, `homepage`, `contact`, `contributors`, `repository`, `chat`, `social-media`
   - These are keys introduction:
      - `name`: A necessary object. It's a string. This value should be the same as the folder name, also should be an English word. Using the abbreviation of the technical group or the registration URL of the group is a suggestion.
      - `title`: A necessary object. It's a string. Put the whole name of the technical group.
      - `category`: A necessary object. It's a string. Put **community** or **conference** in it.
      - `countrycode`: A necessary object. It's a string. The country code should be followed the rule of ISO 3166-1 alpha-2.
      - `city`: A necessary object with a string value. The value is a city name.
      - `keywords`: A necessary object. Put keywords in it. It's an array of strings. This helps people discover the technical group.
      - `registration`: A necessary object. It's a dictionary. Include tow
 keys:
         - type: Put the registration planform name in it. Now, we support Meetup and KKTIX. If there is another registration platform, we will add the feature and support it.
         - url: Put the registration link of the technical group.
      - `description`: A non-necessary object. Put a description in it. It's a string. This helps people discover the technical group.
      - `homepage`: A non-necessary object. It's a string. The url to the technical group homepage.
      - `contact`: A non-necessary object. It's a string. Put the contact information in it.
      - `contributors`: A non-necessary object. It's a string. It's the information of the group organizer.
      - `repository`: A non-necessary object. It's a dictionary. Specify the place where your code lives. This is helpful for people who want to contribute. The URL should be a publicly available url that can be handed directly to a VCS program without any modification. 
      - `chat`: A non-necessary object. It's a list. This is a chatroom platform of the technical group.
      - `social_media`: A non-necessary object. It's a list. Put the social media link in it.
      - `color`: A non-necessary object. It's a string. Put the Hex color code in it.
      - `logo_url`: A non-necessary object. It's a string. Put the logo URL in it.
5. After finish it, please save the file. According to the contribution process of GitHub Flow. Please follow the commit message as the following.
Note 1: Please remove `<>` when you edit the commit message.
Note 2: `<group type>` = `community` or `conference`
Note 3: If there is an related issue, please add `, close #<issue number>` or `, cc #<issue number>` after commit message title(or body).
```
[<group type>] Add <countrycode>/<the name of technical group>
```

### For new Contributors

If you never sent a pull request before, welcome :tada: [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github) to help you send one 

1. [Fork](http://help.github.com/fork-a-repo/) the project, clone your fork, and configure the remotes:

   ```bash
   # Clone your fork of the repo into the current directory
   git clone https://github.com/<your-username>/<repo-name>
   # Navigate to the newly cloned directory
   cd <repo-name>
   # Assign the original repo to a remote called "upstream"
   git remote add upstream https://github.com/TGmeetup/<repo-name>
   ```

2. If you cloned a while ago, get the latest changes from upstream:

   ```bash
   git checkout master
   git pull upstream master
   ```

3. Create a new topic branch (off the main project development branch) to contain your feature, change, or fix:

   ```bash
   git checkout -b <topic-branch-name>
   ```

4. Make sure to update, or add to the tests when appropriate. Patches and features will not be accepted without tests. Run `pytest` to check that all tests pass after you've made changes. Look for a `Testing` section in the project’s README for more information.

5. Push your topic branch up to your fork:

   ```bash
   git push origin <topic-branch-name>
   ```

6. Go to this [TGmeetup repo](https://github.com/TGmeetup/TGmeetup) and [open a Pull Request](https://help.github.com/articles/using-pull-requests/) with a clear title and description.


## Styleguides
### Git Commit Messages
- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the subject line to 50 characters
- Wrap the body at 72 characters
- Need reference issues and pull requests liberally

### Package.json format
Here is an sample [documents/package.json.sample](documents/package.json.sample), please follow it.  
Also, we use 2 spaces for indentation rather than tabs.  
The Required fields is: `name`, `title`, `countrycode`, `city`, `keywords`, `registration`.  

### Use a Consistent Coding Style
Follow PEP8 rules.

## License
By contributing, you agree that your contributions will be licensed under its MIT License.


