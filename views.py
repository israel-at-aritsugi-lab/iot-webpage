from flask import Blueprint, render_template
views = Blueprint(__name__, "views")

import sys
sys.path.append("/Users/angeline/workspace/rice-iot-main/")  
from webpage.database_script import Database  ##
from angelinedb import database  ##

db_instance = database(host="127.0.0.1", port=27017, username="angeline", password="0000", db="my_db")  ##
db_instance.connect()  ##

@views.route('/')
def index():
    db = Database(db_instance)  
    all_sensor_data=db.get_all_sensor_data()
    #latest_sensor_data = db.get_latest_sensor_data()
    #latest_data_date_time=db.get_latest_data_date_time()
    #return render_template('index.html', latest_data=latest_sensor_data,latest_date_time=latest_data_date_time)
    return render_template('index.html', all_sensor_data=all_sensor_data)

#db_instance.disconnect()  ##


@views.route('/<string:sensor_uid>')  ##
def display_sensor_data(sensor_uid):
    db = Database(db_instance)
    sensor_data = db.get_sensor_data_by_uid(sensor_uid)
    return render_template('index.html', all_sensor_data=[sensor_data])
