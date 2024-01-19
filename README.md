Employee_Monitoring_Dashboard

Welcome to My Django Project! This project is a Employee Related one to find the status.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [Contributing](#contributing)
- [License](#license)

## Overview

My Django Project is a simplified Employee Monitoring Dashboard using Python & MySQL and HTML5,CSS3,JavaScript. The 
primary focus is on implementing user authentication, displaying an employee table with 
online/offline status, and providing basic sorting and filtering options.
Backend-Python & MySQL
Frontend-HTML5,CSS3,JavaScript


## Prerequisites

Before running the project, ensure you have the following prerequisites installed:
- Python 3.x
- Django
- MySQL server
## Configuration

Now that you've installed the necessary dependencies, let's configure your Django project to use MySQL.

1. Open the `settings.py` file located in your Django project's main folder.

2. Locate the `DATABASES` setting, and update it to use the MySQL database engine. Replace `'your_database_name'`, `'your_username'`, and `'your_password'` with your actual MySQL database details:

   ```python
   # settings.py
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306',
           'OPTIONS': {
               'charset': 'utf8mb4',
           }

## Running the Project

Now that you've configured your Django project to use MySQL, follow these steps to run the project locally:

1. **Apply Migrations:**

   Run the following command to apply migrations and set up the database:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
## Installation

To install the project dependencies, run the following command:

```bash
pip install mysqlclient
