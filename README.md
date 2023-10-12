❗❗ Replace this readme with a description of your project as soon as possible ❗❗

# python-template-maxi
Hi! This is an advanced template for Python projects. 
The purpose of this template is to be a complete template with simple checks in place to maintain a minimum level of code quality.
However, it is not intended to teach you how to write good code. 
That part is up to you :)


### Python templates

|        | link | Focus                             |
|:------:|:----:|-----------------------------------|
| 🐍     | [Mini](https://github.com/adraismawur/python-template-mini) | File and code structure           |
| 🐍🐍   | [Midi](https://github.com/adraismawur/python-template-midi) | Environments, Requirements and packaging        |
| 🐍🐍🐍 | [Maxi](https://github.com/adraismawur/python-template-maxi) | Testing, Automatic formatting and checks   |


### Table of contents:

- [Quick start](#quick-start)
- [Why should I use this?](#why-should-i-use-this)
- [What is included in this repository?](#what-is-included-in-this-repository)
- [Guide to elements introduced here](#guide-to-elements-introduced-here)

## Quick start:

### Before you begin

❗ Compared to the previous templates, this repository introduces more concepts.  
❗ Some of the elements introduced here can feel annoying to work with until you get used to them.  

### Prerequisites

❗ This template assumes you are familiar with the concepts explained in the [Mini template](https://github.com/adraismawur/python-template-mini) and the [Midi template](https://github.com/adraismawur/python-template-midi)  

- Black
- Flake8
- Mypy

### Set up the repository (local only)

❕Choose this if you are just starting out, or if you do not want to create a page on Github for your code.

1. On this GitHub page, click the **Code** dropdown button in the top-right
2. Click Download ZIP
3. Extract the files somewhere in a new directory
4. Open a shell in the directory where you have extracted the files
5. Edit the readme file to describe your project
6. Run `git add .` to stage all files
7. Run `Git commit -m "initial commit"` to make your first commit

### Set up a remote repository (on GitHub)

❕Choose this if you want to ensure your code is always saved online, or if you want to share your code.

1. Create a new repository of your own by pressing the green button in the top right named "use this template" -> Create a new repository.
   Or [click here](https://github.com/new?template_name=python-template-mini&template_owner=adraismawur)
2. Give your repository a nice name and description
3. Choose whether you want the repository to be public (anyone can see your code), or private.
4. Press "Create repository"

You will be taken to your own github repository page after a few seconds.
From here, you can make edits directly to your files, but it is more practical to download your repository to your local device. (cloning)

1. On your github repository page, click the green button with the text "Code" in the top-right
2. Copy the URL that starts with ```git@github.com:```
3. On your device, open a terminal and navigate to a folder where you want your project to be stored
4. Use the command ```git clone [git url from step 2]```

Your repository will now appear in the folder you navigated to in step 3

### Start coding!

Generally, it is recommended to have the starting point of your code in a file with the name `main.py` inside a folder with the name `your_project_name`.
In there, the `main()` function calls all other functions from separate folders (called modules).

Things to consider while you do so:
- Commit early, commit often
- Aim for ~300 lines of code max for a python file
- You do not have to use the template/ subfolder if you have only a few functions/files
- Have fun!


## Why should I use this?

Regardless of our skill level or best intentions, we all make mistakes when coding.

This template contains a few automated checks against your code that you can use to prevent some mistakes before they are commited, or when they are pushed to the repository.

## What is included in this repository?

- Everything that is included in the [Mini repository](https://github.com/adraismawur/python-template-mini)
  - A [README](#a-readme-file) file
  - A (copyleft) [license](#a-license)
  - A basic [folder structure](#folder-structure)
  - A .gitignore file
- Everything that is included in the [Midi repository](https://github.com/adraismawur/python-template-midi)
  - A pyproject.toml file
  - A requirements.txt file
- A test folder with an example unit test
- A black configuration in the _pyproject.toml_ file
- A pre-commit configuration file (.pre-commit-config.yaml), with the following hooks:
  - Black
  - Flake8
  - Mypy
- A GitHub workflow that runs your unit tests every time you push your changes

## Guide to elements introduced here

### Unit testing

A unit test is a small, simple piece of code that tests a unit (usually a specific method) of your code. Unit tests are at their best if they test exactly one condition in exactly one method, but this is usually difficult to achieve.

Unit tests are difficult to write, but when written well can catch instances where a change you have made to your code causes a new issue (regression).
It can also help you first define the ways in which you want your program to behave before writing code (test-driven development).


### Black

[Black](https://github.com/psf/black) is a code formatter. 
Any code base that uses it will have a style that is the same no matter who wrote the code. 
A consistent code style makes it easier to read, maintain and expand on code.


❗ __It is highly recommended that you find a way to automatically apply black whenever you save your code.__

Style and formatting in coding languages can be a topic of contention.
Black has made a couple of choices for you, some of which are explained below.

#### Why does Black use spaces instead of tabs?

Pretty much all of Black's choices come from adhering to the [PEP8 Style guide](https://peps.python.org/pep-0008/).

Wherever it does not, the authors have made their own decisions and are just applying them consistently.

#### Why does Black limit lines to 88 characters?

PEP8 [recommends 79](https://peps.python.org/pep-0008/#maximum-line-length), but Black extends it to reduce average lines of code.

Additional context: 79 is a historical choice (small monitors could commonly support about 80 characters) as well as a practical one; Using a small character limit ensures that you can put multiple files next to each other on common screen sizes, which really helps in comparing files.

### Pre-commit

[pre-commit](https://pre-commit.com/), a Git [hook](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) added to this repository ensures a basic level of code style and prevents some minor issues. 

As the name implies, scripts configured in the hook will be run before attempting to commit changes to your (local) repository.
Since you (hopefully) commit early and often, pre-commit ensures that your code remains nicely stylized and readable.

❗ __When any hook in pre-commit detects an issue, your commit will fail.__

❗ __When a pre-commit hook modifies your files on commit, it not add (stage) the modification for your current commit!__  
❗ __You have to review and add the modification yourself.__

The following hooks are configured in this template:

#### Black

This applies black on any code in your staged changes (modified files you are about to commit) and modifies the code if any issues are found.

#### Flake8

TODO

### Github workflow

TODO

