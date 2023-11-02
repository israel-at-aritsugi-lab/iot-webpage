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
    ranges=[
            range(10101,10109),
            range(20101,20109),
            range(10201,10211),
            range(40101,40109)
        ]
    
    for x in range(num_entries):        
        random_sensor_uid=random.choice(random.choice(ranges))  #random element in a given range
        random_value=round(random.uniform(0,99),2)   #float in a given range
        random_timestamp=datetime.datetime(2023,11,random.randint(1,2),random.randint(0,23),random.randint(0,59),random.randint(0,59))  #int in a given range
        data_insert.append(sensorData(sensor_uid=str(random_sensor_uid), value=random_value, timestamp=random_timestamp))

    return data_insert
    

# 0.14 seconds (insert one by one - pyMongo)
# def insert_dummy_data(db_instance,data_insert):  
#     db_instance.insert(data_insert)


# 0.12 seconds (input multiple rows of data by using bulk insert - mongoengine)
def insert_dummy_data(db_instance, data_insert):
    sensorData.objects.insert(data_insert)


if __name__ == "__main__":
    db_instance = database(host= "127.0.0.1", port=27017, username= "angeline", password= "0000",db= "my_db")
    db_instance.connect()

    clean_database()

    number_entries = 90000
    bulk_size = 100
    # number_entries = 90
    parts = int(number_entries / bulk_size)
    remaining_parts = number_entries % bulk_size

    for p in range(parts):
        new_data = generate_dummy_data(bulk_size)
        insert_dummy_data(db_instance,new_data)
    
    if remaining_parts > 0:
        new_data = generate_dummy_data(remaining_parts)
        insert_dummy_data(db_instance,new_data)

    db_instance.disconnect()