// function initialize_data(allSensorData){
//     window.onload=function(){
//         allSensorData.forEach(function(data){
//             //get_js_status(data.sensor_uid,data.timestamp);
//             get_js_status(data);
//         });
//     };
// }


function get_js_status(data){
    const id=data.sensor_uid;
    const timestamp=data.timestamp;
    
    const element=document.getElementById(id+'_status');
    //const element=document.getElementById(data.sensor_uid+'_status');

    const dataTime=new Date (timestamp);
    //const dataTime=new Date (data.timestamp);
    const currentTime=new Date();
    //var timeDiff=dataTime.getDate()-currentTime.getDate();
    const timeDiff = (currentTime-dataTime) / (1000 * 60 * 60 * 24); //make sure is currentTime-dataTime to avoid negative value
    //var showStatus;      
    
    //for testing purpose
    console.log('Timestamp:', timestamp);
    console.log('Data Time:', dataTime);
    console.log('Current Time:', currentTime);
    console.log('Time Difference (days):', timeDiff);

    if (timeDiff>2){
        element.innerHTML="Not Working Well !!!";
        //document.getElementById(id).innerHTML="Not Working Well !!!"
        //showStatus="Not Working Well !!!"
    }
    else{
        element.innerHTML="OK";
        //showStatus="OK"
        //document.getElementById(id).innerHTML="OK"
        //showStatus="OK"
    }
}


// document.addEventListener('DOMContentLoaded', function () {
//     console.log("LEARN ANGELINE!", '{{ all_sensor_data_json }}');
//     const allSensorData = JSON.parse('{{ all_sensor_data_json | tojson | safe }}');
//     allSensorData.forEach(function (data) {
//         get_js_status(data);
//     });
// });




window.onload=function(){
    console.log("LEARN ANGELINE!",'{{all_sensor_data_json}}');
    // console.log('{{all_sensor_data_json |safe }}');
    const allSensorData=JSON.parse('{{all_sensor_data_json |safe }}');
    //allSensorData.forEach(function(data){
    allSensorData.forEach((data) => {
          get_js_status(data);
    });
};


// const allSensorData='{{all_sensor_data_json |safe }}';

// window.onload=function(){
//     console.log("LEARN ANGELINE!",allSensorData);
//     // console.log('{{all_sensor_data_json |safe }}');
    
//     const parsedSensorData=JSON.parse(allSensorData);

//     //allSensorData.forEach(function(data){
//     parsedSensorData.forEach((data) => {
//          get_js_status(data);
//     });
// };


// window.onload = function () {
//     const jsonScript = document.getElementById('all_sensor_data_json');

//     const jsonStr = jsonScript.textContent;
//     const allSensorData = JSON.parse(jsonStr);

//     allSensorData.forEach((data) => {
//         get_js_status(data);
//     });
// };


// window.onload = function () {
//     const jsonScript = document.getElementById('all_sensor_data_json');
    
//     if (jsonScript) {
//         const jsonStr = jsonScript.textContent;
//         const allSensorData = JSON.parse(jsonStr);

//         allSensorData.forEach(function (data) {
//             get_js_status(data);
//         });
//     } else {
//         console.error("The script tag with ID 'all_sensor_data_json' was not found.");
//     }
// };




// const allSensorData=JSON.parse('{{all_sensor_data_json |safe }}');
// window.onload=function(){
//     allSensorData.forEach(function(data){
//     //get_js_status(data.sensor_uid,data.timestamp);
//     get_js_status(data);
//     });
// };