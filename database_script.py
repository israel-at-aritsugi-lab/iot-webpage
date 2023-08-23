from angelinedb import database
import mongoengine
import datetime

class sensorData(mongoengine.Document):
    sensor_uid = mongoengine.StringField()
    value = mongoengine.FloatField()
    timestamp = mongoengine.DateTimeField()

def insert_dummy_data(db):
    data_insert = [
        sensorData(sensor_uid="10103", value=20.75, timestamp=datetime.datetime(2023, 8, 23, 18, 0)),  #10103-> 20.75
        sensorData(sensor_uid="10103", value=44.44, timestamp=datetime.datetime(2022, 6, 11, 12, 0)),  

        sensorData(sensor_uid="20102", value=10.25, timestamp=datetime.datetime(2023, 7, 23, 11, 0)),  #20102-> 10.25
        sensorData(sensor_uid="20102", value=21.55, timestamp=datetime.datetime(2022, 5, 31, 13, 0)),
        sensorData(sensor_uid="20102", value=19.33, timestamp=datetime.datetime(2022, 8, 20, 10, 0)),

        sensorData(sensor_uid="10201", value=19.13, timestamp=datetime.datetime(2023, 8, 23, 14, 0)),  #10201-> 19.13
        sensorData(sensor_uid="10201", value=4.75, timestamp=datetime.datetime(2023, 8, 23, 12, 0)),

        sensorData(sensor_uid="40104", value=4.35, timestamp=datetime.datetime(2023, 8, 23, 15, 0)),  #40104-> 4.35
        sensorData(sensor_uid="40104", value=3.50, timestamp=datetime.datetime(2022, 8, 23, 12, 0)),

        sensorData(sensor_uid="10102", value=15.95, timestamp=datetime.datetime(2023, 8, 23, 16, 0)),  #10102-> 15.95
        sensorData(sensor_uid="10102", value=18.71, timestamp=datetime.datetime(2023, 8, 23, 10, 0)),

        sensorData(sensor_uid="40101", value=30.15, timestamp=datetime.datetime(2023, 8, 23, 17, 0)),  #40101-> 30.15
        sensorData(sensor_uid="40101", value=29.52, timestamp=datetime.datetime(2023, 8, 22, 12, 0)),
        sensorData(sensor_uid="40101", value=41.25, timestamp=datetime.datetime(2022, 3, 13, 11, 0))
    ]
    db.insert(data_insert)

def retrieve_dummy_data(db): ##
    data_retrieved = db.find()
    #unique_data=set() ##
    for data in data_retrieved:
        #record_tuple=(data.sensor_uid, data.value, data.timestamp)  ##
        #if record_tuple not in unique_data:  ##
            #unique_data.add(record_tuple)  ##
            #formatted_timestamp=data.timestamp.strftime('%Y-%m-%d %H:%M:%S')  ##
            print("uid:", data.sensor_uid)
            print("value:", data.value)
            print("timestamp:", data.timestamp)
            #print("timestamp:",formatted_timestamp)  ##
            print()

class Database:  ##
    def __init__(self,db_instance):
        self.db_instance=db_instance

    def get_all_sensor_data(self):
        all_sensor_data = sensorData.objects().order_by('-timestamp').limit(6)
        return all_sensor_data
    
    def get_sensor_data_by_uid(self,sensor_uid):  ##
         sensor_data=sensorData.objects(sensor_uid=sensor_uid).order_by('-timestamp').first()
         return sensor_data

    #def get_latest_sensor_data(self):
    #    latest_sensor_data=self.db_instance.retrieve_dummy_data()
    #    return latest_sensor_data

    #def get_latest_data_date_time(self):
    #    latest_data_date_time=datetime.datetime.now()
    #    return latest_data_date_time

if __name__ == "__main__":
    db_instance = database(host= "127.0.0.1", port=27017, username= "angeline", password= "0000",db= "my_db")
    db_instance.connect()

    db=Database(db_instance)  ##

    print("I am running!")
    insert_dummy_data(db_instance) 
    retrieve_dummy_data(db_instance)  

    db_instance.disconnect()
