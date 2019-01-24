Birthday Reminder
=================

This simple module is used to send a birthday reminder via email.

Setup:
------

```shell
$ git clone https://github.com/apoorvpatne10/bday-reminder
$ cd bdayreminder
```

Configuration
-------------

In-order to setup all the email service of this module, you need to update config.ini with your gmail credentials. I've provided an example config file. Rename it to config.ini and update the credentials.

```shell
$ mv example.config.ini config.ini
```

Install Requirements
--------------------
```shell
- Create your separate virtual env and activate it
- Install requirements: pip install -r requirements.txt
```

Usage
-----

```shell
$ python bdayreminder/manage.py --help

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
$ python bdayreminder/manage.py loadsampledata
Enter person's name who's bday reminder you'd like to get
Stan
Enter his/her birth date in YYYY-MM-DD format
2000-01-24
Enter email. This will be the email where a reminder will be sent.
example.mail33@email.com
```

View all current reminders
--------------------------

```shell
$ python bdayreminder/manage.py viewdata
[(1, 'Stan', 'example.mail33@email.com', datetime.date(2000, 1, 24))]
```

Send Email Reminder
-------------------

Run the below command to send Email reminder. This will send an email if today is anyone's birthday.

```shell
$ python bdayreminder/manage.py runemailreminder
Email sent successfully!
```

