import argparse
import sys
import datetime
sys.path.insert(0, "/home/apoorv/Desktop/test/bday-reminder")

from bdayreminder.actions import (
    syncdb,
    loadsampledata,
    runemailreminder,
    cleardata,
    clearperson,
    viewdata
)

ACTIONS = {
    'syncdb': syncdb,
    'loadsampledata': loadsampledata,
    'cleardata': cleardata,
    'clearperson': clearperson,
    'runemailreminder': runemailreminder,
    'viewdata': viewdata,
}


def choicesDescriptions():
    return """
        Choices supports the following:
        syncdb              - Creates new sqlite DB with person table
        loadsampledata      - Loads sample data from db/loader.py
        runemailreminder    - Run reminder with only email
        cleardata           - Clear all reminders
        clearperson         - Delete a reminder given a person's name
        viewdata            - View all the birthday reminders
    """


def main():
    parser = argparse.ArgumentParser(
        "Birthday Reminder",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=choicesDescriptions()
    )
    parser.add_argument('action', choices=ACTIONS.keys())

    args = parser.parse_args()
    action = ACTIONS[args.action]

    if action == loadsampledata:
        print('Enter person\'s name who\'s bday reminder you\'d like to get')
        p_name = input()

        print('Enter his/her birth date in YYYY-MM-DD format')
        date_entry = input()
        year, month, day = map(int, date_entry.split('-'))

        try:
            date1 = datetime.date(year, month, day)
        except ValueError:
            raise ValueError("Incorrect date format. Qutting..")
            sys.exit()

        print('Enter email. This will be the email where a reminder will be '
            + 'sent.')
        email = input()

        action(p_name, date_entry, email)

    elif action == clearperson:
        print('Enter person\'s name who\'s bday reminder you\'d like to delete')
        p_name = input()
        action(p_name)

    else:
        action()

if __name__ == "__main__":
    main()
