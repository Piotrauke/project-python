from storage import *
import time
import sys
from apiclient import get_new_data
import threading
from dash_app import app, create_layout


stop_collector = False

class DataCollectorThread(threading.Thread):
    def run(self):
        store = get_storage()
        #for i in range(200000):
        while True:
            #for i in range(6):
            #add_measurments(str(i), get_new_data(str(i))) # for all the patietns
            add_measurments("2", get_new_data("2"))
            print(get_storage())
            expire_data(15) # should be 10*60
            time.sleep(1)

            if stop_collector:
                print("stopping on request")
                break

        

if __name__ == "__main__":

    #print(get_new_data("2"))
    #sys.exit(0)

    init_storage()
    create_layout()

    collector = DataCollectorThread()
    collector.start()

    #print("waiting...")
    #time.sleep(7)
    try:

        app.run_server(debug=True)
    finally:
        stop_collector = True
        collector.join()
        print("Finished.")