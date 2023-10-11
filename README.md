# IoT for agriculture
This project aims to create the user interface for displaying the data.


### Project Guidelines
To create webpage using frontend (CSS + JS + HTML) and backend (Python + mongoengine).


### Folder Structure
[frontend]

**static:** Mainly focus on the CSS and JavaScript.

**templates:** Mainly focus on the HTML.
- **device_viewer:** display the list of devices with the latest data.
- **latest_sensor_reading:** display the latest data for all sensors.
- **sensor_data_viewer:** display all the data for the specific sensor.
- **sensors_for_device_viewer:** display the list of sensors for the specific device with the latest data.

[backend]
- **insert_data:** Insert data and send to the server.
- **store_data:** To retrieve data and store data. (server)
- **database_script:** Import the database from store_data.
- **views:** Import from the database_script and store_data, connect server and the frontend.
- **app:** Main file to run everything.

