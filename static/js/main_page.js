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





//try1

// window.onload=function(){
//     console.log("LEARN ANGELINE!",'{{all_sensor_data_json}}');
//     // console.log('{{all_sensor_data_json |safe }}');
//     const allSensorData=JSON.parse('{{all_sensor_data_json |safe }}');
//     //allSensorData.forEach(function(data){
//     allSensorData.forEach((data) => {
//           get_js_status(data);
//     });
// };



//try2

// window.onload = function () {
//     const xhr = new XMLHttpRequest();
    
//     xhr.onreadystatechange = function () {
//         if (xhr.readyState === 4){
//             if(xhr.status === 200) {
//                 try{
//                     const allSensorData = JSON.parse(xhr.responseText);
//                     allSensorData.forEach(function (data) {
//                         get_js_status(data);
//                     });
//                 }
//                 catch(error){
//                     console.error("JSON Parse error:", error);
//                     console.log("Response Text:", xhr.responseText); 
//                 }
//             }
//             else{
//                 console.error("HTTP request error:",xhr.status);
//                 console.log("Response Text:", xhr.responseText);
//             }
//         }
//     };
    
//     xhr.open('GET', '/iot', true); 
//     xhr.send();
// };



//try3

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



//try4

// window.onload = function () {
//     const jsonScript = document.getElementById('all_sensor_data_json');
    
//     if (jsonScript) {
//         const jsonStr = jsonScript.textContent;
//         console.log("JSON Data:", jsonStr);
//         try {
//             const allSensorData = JSON.parse(jsonStr);

//             if (Array.isArray(allSensorData)) {
//                 allSensorData.forEach(function (data) {
//                     get_js_status(data);
//                 });
//             } else {
//                 console.error("The JSON data is not an array.");
//             }
//         } catch (error) {
//             console.error("Error parsing JSON:", error);
//         }
//     } else {
//         console.error("The script tag with ID 'all_sensor_data_json' was not found.");
//     }
// };


function show_js_status(data) {
    // data.forEach(d => console.log(d.sensor_uid));
    // data.forEach(d => console.log(d.timestamp));
    data.forEach(function(data){
        get_js_status(data);
    });
};



// const allSensorData=JSON.parse('{{all_sensor_data_json |safe }}');
// window.onload=function(){
//     allSensorData.forEach(function(data){
//     //get_js_status(data.sensor_uid,data.timestamp);
//     get_js_status(data);
//     });
// };