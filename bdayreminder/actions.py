from bdayreminder.db.makedb import init_db
from bdayreminder.db.loader import sampledata
from bdayreminder.db.loader import cleardata
from bdayreminder.db.loader import clearperson
from bdayreminder.db.loader import viewdata

from bdayreminder.services.emails import SendEmail
from bdayreminder.helpers import birthdays


syncdb = init_db
loadsampledata = sampledata
cleardata = cleardata
clearperson = clearperson
viewdata = viewdata

def runreminder(service):

    services = {
        'email': SendEmail,
    }

    birthday_members = birthdays()

    for member in birthday_members:
        services[service](member)()

    print('Email sent successfully!')


def runemailreminder():
    return runreminder('email')
