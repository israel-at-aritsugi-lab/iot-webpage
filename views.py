from flask import Blueprint, render_template

import json ##
import sys
sys.path.append("/Users/angeline/workspace/rice-iot-main/")  
from webpage.database_script import Database, sensorData ##
from angelinedb import database  
from datetime import date, datetime ##

db_instance = database(host="127.0.0.1", port=27017, username="angeline", password="0000", db="my_db")  
db_instance.connect()  

views = Blueprint(__name__, "views",
                  static_folder='static')

"""
#display all latest data for each sensor
@views.route('/')
def index():
    db = Database(db_instance)  
    all_sensor_data=db.get_all_sensor_data()
    #latest_sensor_data = db.get_latest_sensor_data()
    #latest_data_date_time=db.get_latest_data_date_time()
    #return render_template('index.html', latest_data=latest_sensor_data,latest_date_time=latest_data_date_time)

    #return render_template('index.html', all_sensor_data=all_sensor_data)


    all_sensor_data_with_status = []
    for data in all_sensor_data:
        status = db.check_sensor_status(data.sensor_uid)
        #all_sensor_data_with_status.append({"data": data, "status": status})
        data_dict = {
        "sensor_uid": data.sensor_uid,
        "value": data.value,
        "timestamp": data.timestamp,
        "status": status
        }   
    all_sensor_data_with_status.append(data_dict)
    return render_template('index.html', all_sensor_data_with_status=all_sensor_data_with_status)
"""

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

    # all_sensor_data_json=json.dumps([{  #convert all_sensor_data to a JSON string
    #     "sensor_uid":data.sensor_uid,
    #     "value":data.value,
    #     "timestamp":data.timestamp,
    # }for data in all_sensor_data])

    all_sensor_data_json = json.dumps(all_sensor_data, default=datetime_serializer)
    
    
    return render_template('homePage.html', all_sensor_data=all_sensor_data, sensor_status=sensor_status,all_sensor_data_json=all_sensor_data_json)
    #return render_template('index.html', all_sensor_data=all_sensor_data, sensor_status=sensor_status)

#db_instance.disconnect()  



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
    return render_template('allDataPage.html',all_sensor_data=all_data_for_sensor)
   
