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
    


    #To aggregrate the sensors as device
    def aggregate_sensor_data(self):
        aggregated_data = {}
        distinct_sensor_uids = sensorData.objects().distinct("sensor_uid")
        
        for sensor_uid in distinct_sensor_uids:
            device_id = "Device " + sensor_uid[:3]  # Assuming the first 3 characters are common for each device
            sensor_data = self.get_all_data_for_sensor(sensor_uid)
            
            if device_id not in aggregated_data:
                aggregated_data[device_id] = []
            
            aggregated_data[device_id].extend(sensor_data)
        
        return aggregated_data
    


    def get_latest_timestamps(self, aggregated_data):
        latest_timestamps = {}  

        for device_id, sensor_data in aggregated_data.items():
            if sensor_data:
                latest_sensor_timestamp = max(sensor_data, key=lambda x: x.timestamp).timestamp
                latest_timestamps[device_id] = latest_sensor_timestamp

            else:
                latest_timestamps[device_id]=None

        return latest_timestamps
    


    def get_device_status_code(self, sensor_uids, max_days_no_data=1.5):
        working_sensors = 0
        total_sensors = len(sensor_uids)
        
        for sensor_uid in sensor_uids:
            sensor_status = self.check_sensor_status(sensor_uid, max_days_no_data)
            if sensor_status == 'OK':
                working_sensors += 1
        
        return self.calculate_device_status(working_sensors, total_sensors)



    def calculate_device_status(self,working_sensors, total_sensors):        
        if total_sensors == 0:
            return 'no-sensors'
        elif working_sensors == total_sensors:
            return 'green'
        elif working_sensors == 0:
            return 'red'
        elif working_sensors / total_sensors < 0.5:
            return 'orange'
        else:
            return 'yellow'
        

    



         


if __name__ == "__main__":
    db_instance = database(host= "127.0.0.1", port=27017, username= "angeline", password= "0000",db= "my_db")
    db_instance.connect()

    db=Database(db_instance)  

    print("I am running!")
    retrieve_dummy_data(db_instance) 

    db_instance.disconnect()
