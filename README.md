# NOTEIT-NOW

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A User-Freindly Note Taking Application with some stunning features. This project is a part of Google Summer of Code- 2020 Coding Task from the organization: Global Alliance for Genomic Health.

## Table of content ##

- [Features](#features)
- [Installation & Setup](#installation)
- [Contribution](#contribution)
- [Demonstration Snaps](#demonstration-snaps)
- [Get in touch](#-get-in-touch)




### Made by [Syed Farhan Ahmad](https://www.linkedin.com/in/syedfarhanahmad/)

## Features ##

[(Back to top)](#table-of-content)

- Create new Note(s)
- Update existing Note(s)
- Delete existing Note(s)
- Dedicated View for each note
- Multiple tags support for each note
- Search for a note
- Login/Sign Up pages 
- DB schema that supports multiple users
- Powerful admin console(Django-admin)
- Simple and elegant UI


# Installation #

[(Back to top)](#table-of-content)

- Clone the repository

```bash
git clone https://github.com/born-2learn/noteitnow.git
```

It is recommended to follow further steps while in a virtual environment. To create a virtual environment, follow [this link](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

- Next, Install Dependencies

```bash
cd noteitnow
pip3 install -r requirements.txt
```

- Next, create a file names `.env` under noteitnow app directory(where `settings.py` file is present). Add a secret key to your `.env` file:

```
SECRET_KEY=<your_secret_key>
```

- Run django migrations

```bash
python3 manage.py migrate
```

- Run django server

```bash
python3 manage.py runserver
```

## Contribution ##
[(Back to top)](#table-of-content)

Refer **CONTRIBUTING.md** for further details.

# Demonstration Snaps #

[(Back to top)](#table-of-content)

### HomePage with basic information, and developer's profile links.

![HomePage](pictures/home_page.png)   

### Login Page with NavBar
![LoginPage](pictures/login.png)

### Sign Up page
![SignUpPage](pictures/signup.png)

### Notes - The HEART of the application
![Notes](pictures/notes.png)


## Get in Touch ##

[(Back to top)](#table-of-content)

[LinkedIn](https://www.linkedin.com/in/syedfarhanahmad/)

[Follow me on Github](https://github.com/born-2learn)

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)   
This project is based on the **MIT Licence**.



