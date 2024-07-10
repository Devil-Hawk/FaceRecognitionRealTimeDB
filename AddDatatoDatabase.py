import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("#filename for service account key")
firebase_admin.initialize_app(cred,{
    'databaseURL': "Your database URL"
})

ref = db.reference('Student')

data = {
    "321654":
        {
            "name": "Ankit Punjabi",
            "major": "CSE AI",
            "starting_year" : 2019,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "Last_attendance_time": "2023-04-21 18:37:00"
        },
"852741":
        {
            "name": "Akshat Mandwani",
            "major": "BBA",
            "starting_year" : 2020,
            "total_attendance": 2,
            "standing": "B",
            "year": 3,
            "Last_attendance_time": "2023-04-20 18:50:00"
        },
"963852":
        {
            "name": "Mahesh Punjabi",
            "major": "Architecture",
            "starting_year" : 2018,
            "total_attendance": 10,
            "standing": "G",
            "year": 5,
            "Last_attendance_time": "2023-04-20 14:57:00"
        },

}

for key,value in data.items():
    ref.child(key).set(value)