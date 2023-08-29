from angelinedb import database
import mongoengine
import datetime

class sensorData(mongoengine.Document):
    sensor_uid = mongoengine.StringField()
    value = mongoengine.FloatField()
    timestamp = mongoengine.DateTimeField()

def clean_database():
    sensorData.objects().delete()

def generate_dummy_data():
    data_insert = [
        sensorData(sensor_uid="10103", value=20.75, timestamp=datetime.datetime(2023, 8, 23, 18, 0)),  #10103-> 20.75
        sensorData(sensor_uid="10103", value=44.44, timestamp=datetime.datetime(2022, 6, 11, 12, 0)),  

        sensorData(sensor_uid="30201", value=19.13, timestamp=datetime.datetime(2023, 8, 23, 14, 0)),  #30201-> 19.13
        sensorData(sensor_uid="30201", value=4.75, timestamp=datetime.datetime(2023, 8, 23, 12, 0)),

        sensorData(sensor_uid="40104", value=4.35, timestamp=datetime.datetime(2023, 8, 23, 15, 0)),  #40104-> 4.35
        sensorData(sensor_uid="40104", value=3.50, timestamp=datetime.datetime(2022, 8, 23, 12, 0)),

        sensorData(sensor_uid="10102", value=15.95, timestamp=datetime.datetime(2023, 8, 23, 16, 0)),  #10102-> 15.95
        sensorData(sensor_uid="10102", value=18.71, timestamp=datetime.datetime(2023, 8, 23, 10, 0)),

        sensorData(sensor_uid="40101", value=30.15, timestamp=datetime.datetime(2023, 8, 23, 17, 0)),  #40101-> 30.15
        sensorData(sensor_uid="40101", value=29.52, timestamp=datetime.datetime(2023, 8, 22, 12, 0)),
        sensorData(sensor_uid="40101", value=41.25, timestamp=datetime.datetime(2022, 3, 13, 11, 0)),

        sensorData(sensor_uid="10101", value=3.75, timestamp=datetime.datetime(2023, 8, 28, 13, 0)),  #10101-> 3.75
        sensorData(sensor_uid="10101", value=2.92, timestamp=datetime.datetime(2023, 8, 20, 10, 0)),
        sensorData(sensor_uid="10101", value=1.05, timestamp=datetime.datetime(2022, 3, 19, 12, 0)),

        sensorData(sensor_uid="20104", value=10.25, timestamp=datetime.datetime(2023, 7, 23, 11, 0)),  #20104-> 10.25
        sensorData(sensor_uid="20104", value=21.55, timestamp=datetime.datetime(2022, 5, 31, 13, 0)),
        sensorData(sensor_uid="20104", value=19.33, timestamp=datetime.datetime(2022, 8, 20, 10, 0))
    ]
    return data_insert

def insert_dummy_data(db_instance,data_insert):
    db_instance.insert(data_insert)

if __name__ == "__main__":
    db_instance = database(host= "127.0.0.1", port=27017, username= "angeline", password= "0000",db= "my_db")
    db_instance.connect()

    clean_database()
    new_data=generate_dummy_data()
    insert_dummy_data(db_instance,new_data)

    db_instance.disconnect()