#!/usr/bin/env python3

from google.cloud import firestore
from faker import Faker
from numpy import random
COLLECTION='demorecords'
STATE='NY'

db = firestore.Client()
collection = db.collection(COLLECTION)

print("Get All Results")
results = collection.stream()
for doc in results: 
    print(doc.id)

print("Get All Results with Order")
results = collection.order_by('lastname').stream()
for doc in results:
    print(doc.id)

print("Get Top 3 Results by Order")
results = collection.order_by('lastname').limit(3).stream()
for doc in results:
    print(doc.id)

print("Query (String Match):")
results = collection.where('state','==',STATE).stream()
for doc in results:
    print(doc.id)

print("Query with Numeric Greater Than:")
results = collection.where('personid','>=',50).stream()
for doc in results:
    print(doc.id)

print("Query between ranges:")
results = collection.where('state','>=','NY').where('state','<=','O').stream()
for doc in results:
    print(doc.id)

print("Query using in:")
results = collection.where('state','in',['NY','NJ','IL']).stream()
counter = 0
for doc in results:
    print(doc.id)


