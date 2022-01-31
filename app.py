'''
URL : tesla.iem.pw.edu.pl:9080/v2/monitor/{1-6}
            test: tesla.iem.pw.edu.pl:9080/v2/monitor/2
Must be connected to school VPN to access this website
1-6 Different people

VPN domain: vpn.ee.pw.edu.pl
VPN credentials: ISOD login
'''

import requests
from storage import *
from apiclient import *
from dash_app import *
from datetime import datetime
import time
import sys
import threading


start_time = datetime.now()
print(f" Application starting time is: {start_time}")
stop_collector = False



class DataCollectorThread(threading.Thread):
    def run(self):
        store = get_storage()
        while True:

            for i in map(str, range(1,7)):
                add_measurements(i, get_new_data(i))
                patient_id = i
                expire_data(600) 
                # print(get_storage())
                time.sleep(1)     

            if stop_collector:
                print("stopping on request")
                break


if __name__ == "__main__":
    init_storage()
    create_layout()


    for i in map(str,range(1,7)):
        add_measurements(i, get_new_data(i))

    collector = DataCollectorThread()
    collector.start()
    # print("waiting...")
    time.sleep(1)

    try:
        app.run_server(debug=True)
    finally:
        stop_collector = True
        collector.join()
        print("finished")
        


stop_time = datetime.now()
time_diff = stop_time - start_time
print(f"stop time: {stop_time}")
print(f"Time Elapsed: {time_diff}") 
