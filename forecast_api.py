#!/usr/bin/env/ python3

from urllib.request import urlopen
import json
import pandas as pd
from datetime import datetime
import time

campus_url = "http://www.laundryview.com/api/c_room?loc=1921&rdm=815963"
room_url = "http://www.laundryview.com/api/currentRoomData?school_desc_key=1921&location="
campus_data = json.load(urlopen(campus_url))

laundry_to_id = {}
 
for room in campus_data['room_data']:
    laundry_to_id[room['laundry_room_name']] = room['laundry_room_location']
    # print(room['laundry_room_name'], room['online'])

def call_laundry_api():
    while(True):
        time.sleep(60)
        machines = []
        for key in laundry_to_id:
            unique_room_url = room_url + laundry_to_id[key]
            room_data = json.load(urlopen(unique_room_url))
            room_objects = room_data['objects']
            for machine in room_objects:
                if ('appliance_type' in machine):
                    machine_info = {}
                    machine_info['id'] = machine['appliance_desc_key']
                    machine_info['room'] = key
                    machine_info['machine_no'] = machine['appliance_desc']
                    machine_info['type'] = machine['appliance_type']
                    machine_info['avail'] = machine['time_left_lite']
                    if (machine['time_left_lite'] != 'Available'):
                        machine_info['offline'] = True
                    else:
                        machine_info['offline'] = False
                    machine_info['time_remaining'] = machine['time_remaining']
                    machine_info['avg_runtime'] = machine['average_run_time']
                    machine_info['datetime'] = datetime.now()
                    machines.append(machine_info)
        df = pd.DataFrame(machines)
        with open('laundry_data.csv', 'a') as file:
            df.to_csv(file, header=False, index=False)

call_laundry_api()