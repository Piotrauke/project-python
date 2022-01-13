'''
URL : tesla.iem.pw.edu.pl:9080/v2/monitor/{1-6}
            test: tesla.iem.pw.edu.pl:9080/v2/monitor/2
Must be connected to school VPN to access this website
1-6 Different people
'''
'''
VPN domain: vpn.ee.pw.edu.pl
VPN credentials: ISOD login
'''
import requests
from storage import *
import apiclient
import dash_app
# import json
import time
from apiclient import *
import sys


# store = get_storage()
# print(store)

if __name__ == "__main__":
    print(get_new_data("2"))
    sys.exit(0)


    init_storage()
    store = get_storage()
    print(store)

    for i in range(20):
        add_measurements("ania", {
            "timestamp": 1111+i,
            "values": [1,2,3,4,5,8+i],
            "anomalies":[True,False,False,False,True,True]

        } )

    expire_data(5) #10*60 == 10 mins
    print(get_storage())
    time.sleep(1)



    print("Finished") 



# d = requests.get('tesla.iem.pw.edu.pl:9080/v2/monitor/2')
# d.json()
# print(d)