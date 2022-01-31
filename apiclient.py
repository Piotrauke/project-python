import requests
from datetime import datetime

def get_new_data(patient_id):
    res = requests.get(f"http://tesla.iem.pw.edu.pl:9080/v2/monitor/{patient_id}")
    js = res.json()


    return {
        "firstname":   js['firstname'],
        "lastname":    js["lastname"],
        "fullname":    js["firstname"] + " " + js["lastname"],
        "timestamp":   datetime.now(),
        "values":      [ x["value"] for x in js["trace"]["sensors"] ],
        "anomalies":   [ x["anomaly"] for x in js["trace"]["sensors"] ],
        "birthdate":   js["birthdate"],
        "disabled":    js["disabled"]
    }


