# IoT for agriculture
This project aims to create the user interface for displaying the data.


## Project Guidelines
To create webpage using frontend (CSS + JS + HTML) and backend (Python + mongoengine).

## Pre-requisites
- You need to have mongodb installed and have the database populated.
- You need to install the required python packages. To do so run `pip3 install -r requirements.txt`

### Populating the Database
To populate the database, you need to start mongodb, and then run the following code **inside the mongosh shell**:

#### Create a user (limited to the database)
```
use my_db
db.createUser(
  {
    user: "angeline",
    pwd:  "0000", 
    roles: [ { role: "readWrite", db: "my_db" } ]
  }
)
```

#### Run the code to add dummy data in the DB
```
python3 populate_db_dummy_data.py
```

### How to run the code
In the main folder run:
```
python app.py
```

### Folder Structure
[frontend]

**static:** Mainly focus on the CSS and JavaScript.

**templates:** Mainly focus on the HTML.
- **device_viewer:** display the list of devices with the latest data.
- **latest_sensor_reading:** display the latest data for all sensors.
- **sensor_data_viewer:** display all the data for the specific sensor.
- **sensors_for_device_viewer:** display the list of sensors for the specific device with the latest data.

[backend]
- **populate_db_dummy_data:** Insert dummy data in the database.
- **store_data:** To retrieve data and store data. (server)
- **import_data:** Import the database from store_data.
- **views:** Import from the database_script and store_data, connect server and the frontend.
- **app:** Main file to run the backend server.

hello