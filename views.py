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

    sensor_uids=[]
    for data in all_sensor_data:
        sensor_uids.append(data.sensor_uid)

    aggregated_data=db.aggregate_sensor_data()
    latest_timestamps=db.get_latest_timestamps(aggregated_data)
    device_status_code=db.get_device_status_code(sensor_uids)

    print(f"all_sensor_data: {all_sensor_data}")
    print(f"sensor_uids: {sensor_uids}")
    print(f"aggregated_data: {aggregated_data}")
    print(f"latest_timestamps: {latest_timestamps}")
    print(f"device_status_code: {device_status_code}")


    return render_template('device_viewer.html',aggregated_data=aggregated_data, latest_timestamps=latest_timestamps, device_status_code=device_status_code)


#display list of sensors of the specific device
#@views.route('/device_sensor/<string:device_id>')

   
