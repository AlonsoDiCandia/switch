#include "ESP8266WiFi.h"
#include "ESP8266HTTPClient.h"

#define ledPin 2 // choose the pin for the LED 
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
     Serial.print("*");
  }
  
  Serial.println("");
  Serial.println("WiFi connection Successful");
  Serial.print("The IP Address of ESP8266 Module is: ");
  Serial.print(WiFi.localIP());// Print the IP address
  
  pinMode(ledPin, OUTPUT); // declare LED as output
  pinMode(switchPin, INPUT); // declare pushbutton as input
}

void loop()
{
  if (WiFi.status() == WL_CONNECTED) {
    currentState = digitalRead(switchPin); // read input value
  
    if (lastState == LOW && currentState == HIGH)
    { // check if the input is HIGH (button released)
      digitalWrite(ledPin, LOW); // turn LED OFF
      http.begin("http://192.168.17.228:8000/api/apagar/oficina"); 
      int httpResponseCode = http.GET();
    } 
    if (lastState == HIGH && currentState == LOW)
    {
      digitalWrite(ledPin, HIGH); // turn LED ON } }
      http.begin("http://192.168.17.228:8000/api/encender/oficina");
      int httpResponseCode = http.GET();
    }
  
    http.end();  
    // save the the last state
    lastState = currentState;
  }
}
