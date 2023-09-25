// function initialize_data(allSensorData){
//     window.onload=function(){
//         allSensorData.forEach(function(data){
//             //get_js_status(data.sensor_uid,data.timestamp);
//             get_js_status(data);
//         });
//     };
// }


function getJsStatus(data){
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
        element.innerHTML=String.fromCodePoint(0x1F4A9);
        // element.innerHTML="Bad";
        //document.getElementById(id).innerHTML="Not Working Well !!!"
        //showStatus="Not Working Well !!!"
    }
    else{
        element.innerHTML=String.fromCodePoint(0x1F44D);
        // element.innerHTML="Good";
        //showStatus="OK"
        //document.getElementById(id).innerHTML="OK"
        //showStatus="OK"
    }
}




// window.onload=function(){
//     console.log("LEARN ANGELINE!",'{{all_sensor_data_json}}');
//     // console.log('{{all_sensor_data_json |safe }}');
//     const allSensorData=JSON.parse('{{all_sensor_data_json |safe }}');
//     //allSensorData.forEach(function(data){
//     allSensorData.forEach((data) => {
//           get_js_status(data);
//     });
// };




function showJsStatus(data) {
    // data.forEach(d => console.log(d.sensor_uid));
    // data.forEach(d => console.log(d.timestamp));
    data.forEach(function(data){
        getJsStatus(data);
    });
};



// const allSensorData=JSON.parse('{{all_sensor_data_json |safe }}');
// window.onload=function(){
//     allSensorData.forEach(function(data){
//     //get_js_status(data.sensor_uid,data.timestamp);
//     get_js_status(data);
//     });
// };