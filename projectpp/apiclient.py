###apicilient

import requests



def get_new_data(patient_id):
    res = requests.get(f"http://tesla.iem.pw.edu.pl:9080/v2/monitor/{patient_id}")
    js = res.json()
    
    return {
        "timestamp":js["trace"]["id"],
        "values": [x["value"] for x in js["trace"]["sensors"]],
        "anomalies":[x["anomaly"] for x in js["trace"]["sensors"]]
        }