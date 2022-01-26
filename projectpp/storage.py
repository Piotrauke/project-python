import time


def init_storage():


    global _storage
    _storage = {}
    return _storage

def get_storage():
    global _storage
    return _storage



def add_measurments(patient_id, data):
    st = get_storage()
    if patient_id not in st:
        pd = {
            "patient_id": patient_id,
            "timestamps": [],
            "values":[],
            "anomalies":[],
            "_expire_ts":[]

        }
        st[patient_id] = pd
    else:
        pd = st[patient_id]

    pd["timestamps"].append(data["timestamp"])
    pd["values"].append(data["values"])
    pd["anomalies"].append(data["anomalies"])
    pd["_expire_ts"].append(time.time())
    
    
def expire_data(secs):
    st = get_storage()
    for pid, pd in st.items():
        ts = time.time()
        while len(pd["_expire_ts"]) > 0 and pd["_expire_ts"][0] < (ts-secs):
            pd["timestamps"].pop(0)
            pd["values"].pop(0)
            pd["anomalies"].pop(0)  
            pd["_expire_ts"].pop(0)

          