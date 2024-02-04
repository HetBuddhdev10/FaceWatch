import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
'databaseURL':"https://facerecognition-bb913-default-rtdb.firebaseio.com/"
})

ref = db.reference('Persons')

data={
    "32145":{
        "name": "Eiqan",
        "location": "White House",
        "time": "3:23 EST"},

    "32146":{
        "name": "Virat Kohli",
        "location": "Lord's Stadium",
        "time": "2:21 EST"},

    "32147":{
        "name": "Viren Tated",
        "location": "Mitchell Hall",
        "time": "4:31 EST"},
"Eiqan":{
        "name": "Eiqan",
        "location": "Mitchell Hall",
        "time": "3:23 EST"},
}

for key,value in data.items():
    ref.child(key).set(value)
