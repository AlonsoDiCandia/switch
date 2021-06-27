#include "ESP8266WiFi.h"
#include "ESP8266HTTPClient.h"

int switchPin = D5; // choose the input pin (for a pushbutton)
 
const char* ssid = "Alkatonso"; //Enter SSID
const char* password = "internet$"; //Enter Password

HTTPClient http;

// Variables will change:
int lastState =LOW;      
int currentState;

void setup()
{
  // initialize the Arduino's pin as aninput
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) 
  {
     delay(500);
  }
  
  
  pinMode(switchPin, INPUT); // declare pushbutton as input
}

void loop()
{
  if (WiFi.status() == WL_CONNECTED) {
    currentState = digitalRead(switchPin); // read input value
  
    if (lastState == LOW && currentState == HIGH)
    { // check if the input is HIGH (button released)
      http.begin("http://192.168.17.223:8000/api/apagar/central"); 
      int httpResponseCode = http.GET();
    } 
    if (lastState == HIGH && currentState == LOW)
    {
      http.begin("http://192.168.17.223:8000/api/encender/central");
      int httpResponseCode = http.GET();
    }
  
    http.end();  
    // save the the last state
    lastState = currentState;
  }
}
