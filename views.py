from flask import Blueprint, render_template

import json 
import sys
sys.path.append("/Users/angeline/workspace/rice-iot-main/")  
from webpage.database_script import Database, sensorData 
from store_data import database  
from datetime import date, datetime 


db_instance = database(host="127.0.0.1", port=27017, username="angeline", password="0000", db="my_db")  
db_instance.connect()  

views = Blueprint(__name__, "views",
                  static_folder='static')

#convert datetime.datetime & datetime.date objects to strings
def datetime_serializer(obj):
    if isinstance(obj, (datetime,date)):
        return obj.isoformat()  
    if isinstance(obj,sensorData):
        return{
            "sensor_uid":obj.sensor_uid,
            "value":obj.value,
            "timestamp":obj.timestamp.isoformat()
        }
    raise TypeError(f"Type {type(obj)} not serializable")

    
@views.route('/')
def index():
    db = Database(db_instance)
    all_sensor_data = db.get_all_sensor_data()
    
    sensor_status = {}  # Create a dictionary to store sensor statuses
    
    for data in all_sensor_data:
        sensor_uid = data.sensor_uid
        status = db.check_sensor_status(sensor_uid)
        sensor_status[sensor_uid] = status

    all_sensor_data_json = json.dumps(all_sensor_data, default=datetime_serializer)
    
    
    return render_template('latest_sensor_reading.html', all_sensor_data=all_sensor_data, sensor_status=sensor_status,all_sensor_data_json=all_sensor_data_json)


#display the latest data for specific sensor
"""
@views.route('/<string:sensor_uid>')  ##
def display_sensor_data(sensor_uid):
    db = Database(db_instance)
    sensor_data = db.get_sensor_data_by_uid(sensor_uid)
    return render_template('index2.html', all_sensor_data=[sensor_data])
"""

#display all data for specifc sensor
@views.route('/all/<string:sensor_uid>')  
def display_all_data(sensor_uid):
    db=Database(db_instance)
    all_data_for_sensor=db.get_all_data_for_sensor(sensor_uid)
    return render_template('sensor_data_viewer.html',all_sensor_data=all_data_for_sensor)


#display all the devices
@views.route('/devices')
def display_devices():
    db=Database(db_instance)
    all_sensor_data=db.get_all_sensor_data()

    sensor_uids_by_device={}
    for data in all_sensor_data:
        device_id=data.sensor_uid[:3]
        if device_id not in sensor_uids_by_device:
            sensor_uids_by_device[device_id]=[]
        sensor_uids_by_device[device_id].append(data.sensor_uid)

    device_info = []


    

    for device_id, sensor_uids in sensor_uids_by_device.items():
        device_status = db.get_device_status_code(sensor_uids)
        aggregated_data=db.aggregate_sensor_data(device_id)
        latest_timestamps = db.get_latest_timestamps(aggregated_data).get(device_id)
        
        device_info.append({
            'device_id': device_id,
            'latest_timestamps': latest_timestamps,
            'device_status_code': device_status
        })

    context = {
        'device_info': device_info
    }

    return render_template('device_viewer.html', **context)



#display list of sensors of the specific device
@views.route('/devices/<string:device_id>')
def display_sensors_for_devices(device_id):
    db=Database(db_instance)
    #all_sensor_data=db.get_all_sensor_data()
    sensors_for_device = db.get_device_sensors(device_id)

    sensor_info=[]
    for sensor_data in sensors_for_device:
        if sensor_data is None or sensor_data =="NOt Working Well !!!":
            print(f"Skippping non-object value: {sensor_data}")
            continue

        #print(f"sensor type: {type(sensor_data)}")
        if isinstance(sensor_data, sensorData):
        #if sensor_data:
            status=db.check_sensor_status(sensor_data.sensor_uid)
            sensor_info.append({
                'sensor_uid': sensor_data.sensor_uid,
                'value': sensor_data.value,
                'latest_timestamp': sensor_data.timestamp,
                'status': status
            })

        else:
            print(f"skipping non-object value: {sensor_data}")
            #print(f"No data found for device {device_id}")


    context = {
        'device_id': device_id,
        'sensor_info': sensor_info,
    }

    print(f"device id: {device_id}")
    print(f"sensor info:{sensor_info}")

    return render_template('sensors_for_device_viewer.html', **context)

    # sensor_uids_by_device={}
    # for data in all_sensor_data:
    #     #device_id=data.sensor_uid[:3]
    #     if device_id not in sensor_uids_by_device:
    #         sensor_uids_by_device[device_id]=[]
    #     sensor_uids_by_device[device_id].append(data.sensor_uid)

    # for sensor_uids in sensor_uids_by_device.items():
    #     sensor_list=db.get_device_sensors(sensor_uids)

    # sensors_for_device=[data for data in all_sensor_data if data.sensor_uid.startswith(device.id)]