# Blog


## Contents
1. [Main Information](#📜-Main-Information)
2. [Features](#Features)
3. [Stack](#Stack)
4. [Installation and Usage](#Installation-and-Usage)
5. [Examples](#Examples)
    1. [Homepage](#Homepage)
    2. [Review details](#Review-details)
    3. [Create and Edit review](#Create-and-Edit-review)
    4. [Registration-and-Login](#Registration-and-Login)
    5. [Profile](#Profile)
    6. [Password recovery and Password change](#Password-recovery-and-Password-change)

____

## 📜 Main Information

This web application is a blog where users 
can share their reviews and opinions on films and books.

____

## Features

- **User Authentication:** 
    The user must be registered to start writing reviews. To start publishing
    the user needs to confirm his/her email. All instructions will be in 
    the letter which will be sent to his/her email.
  1. Register
  2. Log in
  3. Change password, reset password
  
  Each user can also change their personal information and add a personal photo.
  
- **Create and Edit Reviews:** Users can create new reviews or edit the existing ones.
- **Filter Functionality:** It's possible to find a review by category or tag.

____

## Stack

✅ HTML, CSS, SCSS

✅ Python

✅ Django

✅ Pytest

____

## Installation and Usage

**Installation:**

* Clone the repository: git clone https://github.com/reyand8/Blog.git

**Usage:**

* Application
    - Navigate to the project directory: cd app
    - Install dependencies: pipenv sync
    - Add EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER and 
  EMAIL_HOST_PASSWORD to settings.py
        - Run the project: python3 manage.py runserver
        - Open a browser and navigate to: http://127.0.0.1:8000/
      
____

## Examples


### Homepage

![homepage.png](readmeScr%2Fhomepage.png)

![homepage2.png](readmeScr%2Fhomepage2.png)

____
____

### Review details

![review_details.png](readmeScr%2Freview_details.png)

____
____

### Create and Edit review

![review_add.png](readmeScr%2Freview_add.png)

![review_edit.png](readmeScr%2Freview_edit.png)

____
____

### Registration and Login

![registration.png](readmeScr%2Fregistration.png)

![login.png](readmeScr%2Flogin.png)

____
____

### Profile

![user_edit.png](readmeScr%2Fuser_edit.png)

____
____

### Password recovery and Password change

![password_recovery.png](readmeScr%2Fpassword_recovery.png)

![change_password.png](readmeScr%2Fchange_password.png)

____
____