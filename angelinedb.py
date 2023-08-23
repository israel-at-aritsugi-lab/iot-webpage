import mongoengine
# Some changes 2
class database():
    def __init__(self,host="127.0.0.1",db="my_db",username= "angeline",password= "0000",port=27017):
        self.host = host
        self.db = db
        self.username = username
        self.password = password
        self.port = port
        self.connection = None
        self.database = mongoengine

    def connect(self):
        self.connection = self.database.connect(self.db, host=self.host, port=self.port, username=self.username, password=self.password)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def insert(self, data_insert):
        if self.connection:
            self.insert_dummy_data(data_insert)

    def find(self):
        if self.connection:
            return self.retrieve_dummy_data()
        
    def insert_dummy_data(self, data_insert): ##
        if self.connection:
            for data in data_insert:
                #existing_data =sensorData.objects(sensor=data.sensor_uid, value=data.value, timestamp=data.timestamp)
                #if not existing_data:
                    sensor_data = sensorData(sensor_uid=data.sensor_uid, value=data.value, timestamp=data.timestamp)
                    sensor_data.save()

    def retrieve_dummy_data(self):
        if self.connection:
            return sensorData.objects()

class sensorData(mongoengine.Document):  
    sensor_uid = mongoengine.StringField()  
    value = mongoengine.FloatField()  
    timestamp = mongoengine.DateTimeField() 

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 27017
    username = "angeline"
    password = "0000"
    db = "my_db"
    
    #db_instance = database(ip, port, user, pw, db)
    #db_instance.connect()
    #db_instance.disconnect()
