function getJsStatus(data){
    const id=data.sensor_uid;
    const timestamp=data.timestamp;
    const element=document.getElementById(id+'_status');
    const dataTime=new Date (timestamp);
    const currentTime=new Date();
    const timeDiff = (currentTime-dataTime) / (1000 * 60 * 60 * 24); //make sure is currentTime-dataTime to avoid negative value
        
    //for testing purpose
    console.log('Timestamp:', timestamp);
    console.log('Data Time:', dataTime);
    console.log('Current Time:', currentTime);
    console.log('Time Difference (days):', timeDiff);

    if (timeDiff>2){
        element.innerHTML=String.fromCodePoint(0x1F4A9);
    }
    else{
        element.innerHTML=String.fromCodePoint(0x1F44D);
    }
}

function showJsStatus(data) {
    data.forEach(function(data){
        getJsStatus(data);
    });
};
