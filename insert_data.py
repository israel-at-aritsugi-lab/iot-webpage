from store_data import database
import mongoengine
import datetime
import random

class sensorData(mongoengine.Document):
    sensor_uid = mongoengine.StringField()
    value = mongoengine.FloatField()
    timestamp = mongoengine.DateTimeField()

#to keep the data updated
def clean_database():
    sensorData.objects().delete()

def generate_dummy_data(num_entries):
    data_insert=[]
    for x in range(num_entries):
        ranges=[
            range(10101,10109),
            range(20101,20109),
            range(10201,10211),
            range(40101,40109)
        ]
        random_sensor_uid=random.choice(random.choice(ranges))  #random element in a given range
        random_value=round(random.uniform(0,99),2)   #float in a given range
        random_timestamp=datetime.datetime(2023,9,random.randint(1,29),random.randint(0,23),random.randint(0,59),random.randint(0,59))  #int in a given range
        data_insert.append(sensorData(sensor_uid=str(random_sensor_uid), value=random_value, timestamp=random_timestamp))
    return data_insert
    

def insert_dummy_data(db_instance,data_insert):
    db_instance.insert(data_insert)

if __name__ == "__main__":
    db_instance = database(host= "127.0.0.1", port=27017, username= "angeline", password= "0000",db= "my_db")
    db_instance.connect()

    clean_database()
    new_data=generate_dummy_data(300)
    insert_dummy_data(db_instance,new_data)

    db_instance.disconnect()