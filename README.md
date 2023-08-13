# Django - Learning
This project is running on django version 4.2.4 and python version 3.10.12

# Introduction
The goal of this project is to learn django professional and everyone can use this project. 

_Also_ want to cover up this things
* Project Setup
* Project Structure
* Database Configuration
* User Authentication and Authorization
* Templates and Static Files
* Models and Database Interactions
* Forms
* Testing
* Security
* Deployment
* Logging and Monitoring
* Documentation
* Version Control and Collaboration


# Installation

To use this project to your own machine follow this steps

### Clone repository from github

First of all, clone this repository using this command

    git clone https://github.com/mehedishovon01/django-learning.git

### Create a virtualenv

Make a virtual environment to your project directory. Let's do this,

If you have already an existing python3 virtualenv then run this

    virtualenv venv

Or if virtualenv is not install in you machine then run this

    python3 -m venv venv
    
Activate the virtual environment and verify it

    . venv/bin/activate

### Install the dependencies

Most of the projects have dependency name like requirements.txt file which specifies the requirements of that project, so let’s install the requirements of it from the file.

    pip install -r requirements.txt

### Create database

We have already sqlite3 setup in our project.

So, simply apply the migrations:

    python3 manage.py migrate
    
Boooooom! Your project setup is done.

### Run this project

Let's run the development server:

    python3 manage.py runserver

That’s it! Now you’re project is already run into a development server. 

Just click this link, [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Thanks for reading.