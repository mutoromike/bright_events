[![Build Status](https://travis-ci.org/Chris-Maina/Shoppinglist.svg?branch=develop)](https://travis-ci.org/Chris-Maina/Shoppinglist)     [![Coverage Status](https://coveralls.io/repos/github/Chris-Maina/Shoppinglist/badge.svg)](https://coveralls.io/github/Chris-Maina/Shoppinglist)  [![Codacy Badge](https://api.codacy.com/project/badge/Grade/b56fc12f98e546138ca01a8775e9aec1)](https://www.codacy.com/app/Chris-Maina/Shoppinglist?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Chris-Maina/Shoppinglist&amp;utm_campaign=Badge_Grade)  [![Code Health](https://landscape.io/github/Chris-Maina/Shoppinglist/develop/landscape.svg?style=flat)](https://landscape.io/github/Chris-Maina/Shoppinglist/develop)

# Shoppinglist Application
This repository contains an application helps you record all items you wish to buy. It allows you to record and share things you want to spend money on, meeting your needs and keeping track of your shopping lists. It is 
developed to use data structures only i.e. 
  
  * List
  * Dictionaries
  ## Installation procedure
 Clone this repository:
   * https://github.com/Chris-Maina/Shoppinglist.git
   
 Navigate to the downloaded repository:
   * $ cd project_folder
   
 Install a virtual environment: 
   * $ pip install virtualenv
   
 (Optional)Test your virtualenv:
   * $ vitualenv --version
   
 Create your virtual environment:
   * $ cd project_folder
   * $ virtualenv yourenvname
   
 Activate your virtual environment:
   * $ source yourenvname/bin/activate
   
 Install requirements:
   * $ (yourenvname) pip install -r requirements.txt
    
## Running the application
    $  (yourenvname) python run.py
    
## Testing the application
cd into project_folder folder, RUN the following command
   * $ nosetests --with-coverage --cover-package=tests && coverage report

## How to use application
* Register an account
* Login with the credentials used during registration
* Add shopping list(s)
* Add shopping items
