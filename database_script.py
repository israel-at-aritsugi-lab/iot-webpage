from store_data import database
import mongoengine
from datetime import datetime

class sensorData(mongoengine.Document):
    sensor_uid = mongoengine.StringField()
    value = mongoengine.FloatField()
    timestamp = mongoengine.DateTimeField()

def retrieve_dummy_data(db): 
    data_retrieved = db.find()
    for data in data_retrieved:
        print("uid:", data.sensor_uid)
        print("value:", data.value)
        print("timestamp:", data.timestamp)
        print()

class Database:  
    def __init__(self,db_instance):
        self.db_instance=db_instance

    def get_all_sensor_data(self):
        all_sensor_data = []
        distinct_sensor_uids = sensorData.objects().distinct("sensor_uid")
        for sensor_uid in distinct_sensor_uids:
            latest_data = self.get_sensor_data_by_uid(sensor_uid)
            if latest_data:
                all_sensor_data.append(latest_data)
        return all_sensor_data
        
    
    def get_sensor_data_by_uid(self,sensor_uid):  
         sensor_data=sensorData.objects(sensor_uid=sensor_uid).order_by('-timestamp').first()
         return sensor_data

    def get_all_data_for_sensor(self,sensor_uid):  
         all_data_for_sensor=sensorData.objects(sensor_uid=sensor_uid).order_by('-timestamp')
         return all_data_for_sensor

    def check_sensor_status(self, sensor_uid, max_days_no_data=1.5):
        latest_data = self.get_sensor_data_by_uid(sensor_uid)

        if latest_data:
            current_time = datetime.now()
            if (current_time - latest_data.timestamp).days > max_days_no_data:
                status = 'Not Working Well !!!'
            else:
                status = 'OK'
        else:
            status = 'Not Working Well !!!'

        return status
         


if __name__ == "__main__":
    db_instance = database(host= "127.0.0.1", port=27017, username= "angeline", password= "0000",db= "my_db")
    db_instance.connect()

    db=Database(db_instance)  

    print("I am running!")
    retrieve_dummy_data(db_instance)  

    db_instance.disconnect()
