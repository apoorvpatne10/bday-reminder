import os
import datetime
from bdayreminder.db.base import DBSession
from bdayreminder.db.base import engine
from bdayreminder.db.models import Person
import sqlalchemy as db

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

def sampledata(p_name, date_entry, email):
    session = DBSession()

    person1 = Person(
        name = p_name,
        dob = date_entry,
        email = email,
    )

    session.add(person1)

    session.commit()
    session.close()

def clearperson(p_name):
    session = DBSession()

    session.query(Person).filter(Person.name==p_name).delete()
    session.commit()

    session.close()

def cleardata():
    session = DBSession()

    session.query(Person).delete()
    session.commit()

    session.close()

def viewdata():
    session = DBSession()

    connection = engine.connect()
    metadata = db.MetaData()
    census = db.Table('person', metadata, autoload=True, autoload_with=engine)

    query = db.select([census])

    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()

    print(ResultSet)

    session.close()
