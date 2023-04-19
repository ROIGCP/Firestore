#!/usr/bin/env python3

from google.cloud import firestore
from faker import Faker
from numpy import random
COLLECTION = "demopeople"

db = firestore.Client()

collection = db.collection(COLLECTION)
docs = collection.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
    

