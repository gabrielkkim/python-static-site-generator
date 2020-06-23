# Build a Static Site Generator with Python

## Status

**Published**

## Overview

This project is design to be completed on [Pluralsight](https://pluralsight.com). To find out more see here: [https://www.pluralsight.com/product/projects](https://www.pluralsight.com/product/projects).

## Installation

### Local environment setup
Installing Python3 and Pip
```
> to verify Python3 was installed correctly type:
$ python3 -V
> to verify pip3 was installed correctly type:
$ pip3 -V
> to verify Python3 is running under the default command line, type:
$ export PATH="/usr/local/opt/python/libexec/bin:$PATH" >> ~/.bashrc

> to verify local environment, type:
$ cd 'project-root'
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
> finally run a tests, type:
$ pytest
```

### macOS
Open a terminal and run the following commands, replacing 'project-root' with the path to the root folder of the project.

```
$ cd 'project-root'
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
*Note: If you've installed Python 3 using a method other than Homebrew, you might need to type `python` in the second command instead of `python3`.*

### About pip
Versions pip updates frequently, but versions greater than 10.x.x should work with this project.

## Verify Setup

In order to verify that everything is setup correctly, run the following command from the project root.
```
pytest
```
You should see that all the tests are failing. This is good! We’ll be fixing these tests once we jump into the build step. Every time you want to check your work locally you can type that command, and it will report the status of every task in the project.

## Previewing Your Work
You can preview your work by running the command `python ssg.py` after the first module.
