var b = true;

function getLocalTime() {
    var date = new Date();

    var day = date.getDate();
    var month = twoDigitNumber(date.getMonth() + 1);
    var year = date.getFullYear();

    document.getElementById("day").innerText = day;
    document.getElementById("month").innerText = month;
    document.getElementById("year").innerText = year;

    var hours = twoDigitNumber(date.getHours());
    var minutes = twoDigitNumber(date.getMinutes());
    var seconds = twoDigitNumber(date.getSeconds());

    document.getElementById("hours").innerText = hours;
    document.getElementById("minutes").innerText = minutes;
    document.getElementById("seconds").innerText = seconds;

    if (b == true || minutes === "00" || minutes === "30") {
        getWeather();
        b = false;
    }
    var time = setTimeout(function(){ getLocalTime() }, 500);
}

function twoDigitNumber(number) {
    var len = number.toString().length;

    if (len == 1) {
        return "0" + number.toString();
    }
    else if (len == 2) {
        return number.toString();
    }
    else if (len == 0) {
        return "00";
    }
}

function getWeather() {
    const url = "http://api.openweathermap.org/data/2.5/weather?q=Talcahuano,cl&appid=fbadc7c2c99dd8826cd2a7b7cc83b54a"
    
    var http = new XMLHttpRequest();
    http.open("GET", url, false);
    http.send();

    var myJSON = JSON.parse(http.responseText);
    var temp = parseFloat(myJSON["main"]["temp"]) - 273.15;
    var main = myJSON["weather"]["0"]["main"];

    if (main === "Clouds") {
        document.getElementById("weatherImg").src = "../images/cloudy.png";
        document.getElementById("weatherImg").width = 40;
    }

    document.getElementById("weather").innerText = temp.toString()+"º";

}
