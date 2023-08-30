from angelinedb import database
import mongoengine
import datetime

class sensorData(mongoengine.Document):
    sensor_uid = mongoengine.StringField()
    value = mongoengine.FloatField()
    timestamp = mongoengine.DateTimeField()

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
        #all_sensor_data = sensorData.objects().order_by('-timestamp').limit(7)
        #return all_sensor_data
        all_sensor_data = []
        distinct_sensor_uids = sensorData.objects().distinct("sensor_uid")
        for sensor_uid in distinct_sensor_uids:
            latest_data = self.get_sensor_data_by_uid(sensor_uid)
            if latest_data:
                all_sensor_data.append(latest_data)
        return all_sensor_data
        
    
    def get_sensor_data_by_uid(self,sensor_uid):  ##
         sensor_data=sensorData.objects(sensor_uid=sensor_uid).order_by('-timestamp').first()
         return sensor_data
    

    def get_all_data_for_sensor(self,sensor_uid):  ##
         all_data_for_sensor=sensorData.objects(sensor_uid=sensor_uid).order_by('-timestamp')
         return all_data_for_sensor


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
    #insert_dummy_data(db_instance) 
    retrieve_dummy_data(db_instance)  

    db_instance.disconnect()
