from angelinedb import database
import mongoengine
import datetime
import random
#from datetime import timedelta

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
        random_timestamp=datetime.datetime(2023,9,random.randint(1,12),random.randint(0,23),random.randint(0,59),random.randint(0,59))  #int in a given range
        data_insert.append(sensorData(sensor_uid=str(random_sensor_uid), value=random_value, timestamp=random_timestamp))
    return data_insert

"""
def generate_random_timestamp(start_date,end_date):
    time_diff = (end_date - start_date).total_seconds()
    random_time_diff = random.uniform(0, time_diff)  # Random number of seconds within the time range
    #random_time_diff=math.floor(random_time_diff)
    random_timestamp = start_date + datetime.timedelta(seconds=random_time_diff)
    return random_timestamp

def generate_dummy_data(num_entries):
    data_insert=[]
    end_date = datetime.datetime.now()  # Current date and time
    start_date = end_date - datetime.timedelta(days=30)  # 30 days before the current date

    ranges={
        "sensor1":list(range(10101,10109)),
        "sensor2":list(range(20101,20109)),
        "sensor3":list(range(10201,10211)),
        "sensor4":list(range(40101,40109))
    }

    for x in range(num_entries):
        sensor_type=random.choice(list(ranges.keys()))
        if ranges[sensor_type]:
            random_sensor_uid=random.choice(ranges[sensor_type])  #random element in a given range
            random_value=round(random.uniform(0,99),2)  #float in a given range
            random_timestamp = generate_random_timestamp(start_date, end_date)
            data_insert.append(sensorData(sensor_uid=str(random_sensor_uid), value=random_value, timestamp=random_timestamp))

    return data_insert
"""
"""
        current_date = datetime.datetime.now()
        start_date = current_date - datetime.timedelta(days=30)

        random_timestamp = datetime.datetime(       #generate 30-days range from the current date
            random.randint(start_date.year, current_date.year),
            random.randint(start_date.month, current_date.month),
            random.randint(start_date.day, current_date.day),
            random.randint(0, 23),
            random.randint(0, 59),
            random.randint(0, 59)
        )


        #random_timestamp=datetime.datetime(2023,8,random.randint(1,31),random.randint(0,23),random.randint(0,59),random.randint(0,59))  #int in a given range
            
"""
    

def insert_dummy_data(db_instance,data_insert):
    db_instance.insert(data_insert)

if __name__ == "__main__":
    db_instance = database(host= "127.0.0.1", port=27017, username= "angeline", password= "0000",db= "my_db")
    db_instance.connect()

    clean_database()
    new_data=generate_dummy_data(300)
    insert_dummy_data(db_instance,new_data)

    db_instance.disconnect()