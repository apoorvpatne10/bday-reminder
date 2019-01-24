Birthday Reminder
=================

This simple module is used to send a birthday reminder via email.

Setup:
------

```shell
$ git clone git-repo
$ cd bdayreminder
```

Configuration
-------------

In-order to setup all the email service of this module, you need to update config.ini with your gmail credentials.


Install Requirements
--------------------
```
- Create your separate virtual env and activate it
- Install requirements: pip install -r requirements.txt
```

Usage
-----

```shell
$ python3 bdayreminder/manage.py --help

usage: Birthday Reminder [-h]

optional arguments:
  -h, --help            show this help message and exit

        Choices supports the following:
        syncdb              - Creates new sqlite DB with person table
        loadsampledata      - Loads sample data from db/loader.py
        runemailreminder    - Run reminder with only email
        cleardata           - Clear all reminders
        clearperson         - Delete a reminder given a person\'s name
        viewdata            - View all the birthday reminders
```

Init DB
-------
Use the below command to create sqlite DB with `Person`.

```shell
$ python bdayreminder/manage.py syncdb
```

Load Sample Data
----------------

```shell
$ python3 bdayreminder/manage.py loadsampledata
```

Send Email Reminder
-------------------

Run the below command to send Email reminder

```shell
$ python3 bdayreminder/manage.py runemailreminder
```
# bday-reminder
