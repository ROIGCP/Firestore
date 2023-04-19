#!/usr/bin/env python3

from google.cloud import firestore
from faker import Faker
from numpy import random
import json

COLLECTION = "demorecords"
NUMPEOPLE = 100

db = firestore.Client()
fake = Faker()
Faker.seed(random.randint(1000))

for personid in range(1,NUMPEOPLE):
    firstname = fake.first_name()
    lastname = fake.last_name()
    middlename = fake.first_name()
    fullname = lastname + firstname
    job = fake.job()
    dictionary = {
        'firstname': firstname,
        'lastname': lastname,
        'middlename': middlename,
        'personid': personid,
        'job': job,
        'kids': [{
            'name': fake.first_name(),
            'age': random.randint(18)
            },{
            'name': fake.first_name(),
            'age': random.randint(18)
            }],
        'contactnumbers': [{
            'home': fake.phone_number()
            },{
            'cell': fake.phone_number()
            }],
        'city': fake.city(),
        'state': fake.state_abbr(),
        'zip': fake.postcode(),
        'country': "US",
        'timestamp': firestore.SERVER_TIMESTAMP
    }
    doc_ref = db.collection(COLLECTION).document(fullname)
    doc_ref.set(dictionary)
    print("Created " + str(personid))

print("Done")