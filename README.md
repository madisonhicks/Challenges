# Challenges
Coding challenges

## Setup

### Python

* Don't forget to set up a virtual environment for Python
when getting started, and to activate it each time you're
working on this project:
  * `python3.6 -m venv venv --copies`
  * `source venv/bin/activate`
* If you're using PyCharm or IntelliJ, be sure to set the
virtual environment's Python interpreter as the default in
settings -> project: Challenges -> project interpreter
* Install the project in development mode:
  * `pip install -e .`
* You can update the project requirements at any time by running
  * `pip install -e . --upgrade` OR
  * `pip install -e . -U`

### Node

* run `npm install` from the root directory
* if third party packages are added to the `package.json`
requirements file, you can update your environment by running
`npm install` again

## Layout

This project is currently organized by year and month. Within
each month directory, challenges are numbered, with a lightly
descriptive name. Challenges are either designed to be completed
using Python or JavaScript. Which is to be used should be obvious
based on the file extension.

## Running files

### Python

* Ensure you have activated your virtual environment `source venv/bin/activate`
* Run `python <your_script_name>`, which will automatically test your code
* If you want to test just one method, run
`python <your_script_name> <your_method_name>`


### Node

* Run `node <your_script_path>`
