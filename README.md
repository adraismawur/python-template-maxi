***Replace this readme with a description of your project, and a description of how your code works as soon as possible***

# python-template-1
Hi! This is a simple template for Python projects. This is intended to force very few things, and help you structure your code in a nice way.

The code included in this repository is in itself a small tutorial on how to structure
your python code.  

This template is not intended to teach you how to write good code. That part is up to you :)


### Table of contents:

- [Quick start](#quick-start)
- [What is included in this repository?](*what-is-included-in-this-repository)
- [Why should I use this?](#why-should-i-use-this)

## Quick start:

### Prerequisites

- Git
- [Pre-commit (https://pre-commit.com/)](https://pre-commit.com/)

### Download the files

1. Click the Code dropdown in the top-right
2. Click Download ZIP
3. Extract the files somewhere in a new directory

### Set up the repository (local only)

4. Open a shell in the directory where you have extracted the files
5. Run ```git init``` to initialize the git repository
6. Run ```pre-commit install``` to set up pre-commit
7. Edit the readme file to describe your project
8. Run ```git add .``` to stage all files
9. Run ```Git commit -m "initial commit"``` to make your first commit

### Set up a remote

TODO

### Start coding!

Things to consider while you do so:
- Commit early, commit often
- Aim for ~300 lines of code max for a python file
- You do not have to use the template/ subfolder if you have only a few functions/files
- Have fun!


## What is included in this repository?

- A readme file
- A [copyleft](https://choosealicense.com/licenses/gpl-3.0/) license
- A basic folder structure
- A requirements yml
- Pre-commit, using:
  - [Black](https://github.com/psf/black)



## Why should I use this?

It's difficult to write code. It can be even more difficult to write code that is easy to read and maintain. This template is designed to help you structure your python code in a way that is common for a lot of well-maintained Python projects, while not forcing any of the more difficult aspects of code mainenance on you.  

### Why do I need a readme?

A readme is the first point many people will go to to understand your project, and to figure out how to set up or install your program.

You can put nearly anything you want in a readme, but generally it is expected that the readme describes what your project is about and how you run your application.

Refer to [The markdown guide](https://www.markdownguide.org/basic-syntax) to see what you can do in README.md files.

### Why do I need a license?

You do not *need* a license. But if you do not include a license, you are the sole holder of rights to your code (standard copyright), and it is not allowed to contribute and share your code with other people without your permission.

If you want, you can choose a different license on https://choosealicense.com/

### Why do I need this folder structure?

You do not need this exact folder structure, but for larger projects it is highly recommended that you subdivide your code into submodules. It takes people very long to read through an entire file to find the specific code they are interested in editing, so collating your code by category into different files and functions is important.

If you are working with just a few functions, it is also OK to have a few python files in the root directory without any subdirectories.

### Why do I need a requirements file?

A requirements file makes it easy for people to automatically install the same dependencies you used to develop and run your application. You can also fix your requirements to specific version numbers to ensure that people can use the exact same dependencies and re-produce your work.

### Why do I need pre-commit

The pre-commit hooks added to this repository ensure a basic level of code style and prevent some minor issues. Since you (hopefully) commit early and often, pre-commit ensures that your code remains nicely stylized and readable.

### Why do I need black?

Any code base that uses Black will have a style that is the same no matter who wrote the code. A consistent code style makes it easier to read, maintain and expand on code.

### Why does black use spaces instead of tabs?

Pretty much all of Black's choices come from adhering to the [PEP8 Style guide](https://peps.python.org/pep-0008/).

Wherever it does not they have made their own decisions and are just applying them consistently.

### Why does black limit lines to 88 characters?

PEP8 recommends 79, but black extends it to reduce average lines of code.

Additional context: 79 is a historical choice (small monitors could commonly support about 80 characters) as well as a practical one; Using a small character limit ensures that you can put multiple files next to eachother on common screen sizes, which really helps in comparing files.


