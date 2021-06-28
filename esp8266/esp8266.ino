#include "ESP8266WiFi.h"
#include "ESP8266HTTPClient.h"

int outputA = D1;
int outputB = D2;
int switchPin = D5; // choose the input pin (for a pushbutton)
 
const char* ssid = "Alkatonso"; //Enter SSID
const char* password = "internet$"; //Enter Password

HTTPClient http;

// Variables will change:

//SWITCH
int lastState =LOW;      
int currentState;

//ROTARY ENCODER
int counter = 0;
int a_state;
int a_last_state;

void setup()
{
  // initialize the Arduino's pin as aninput
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) 
  {
     delay(500);
  }
  
  pinMode(switchPin, INPUT); // declare pushbutton as input
  pinMode(outputA, INPUT);
  pinMode(outputB, INPUT);

  a_last_state = digitalRead(outputA);
}

void loop()
{

  //SWITCH SECTION
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

  //ROTARY ENCODER SECTION
  a_state = digitalRead(outputA);
  if (a_state != a_last_state) 
  {
    if (digitalRead(outputB) != a_state) 
    {
      if (counter > 1)
      {
        counter --;
        http.begin("http://192.168.17.223:8000/api/brillo/central/"+String(counter));
        int httpResponseCode = http.GET();
      }
    } else 
    {
      if (counter < 100) 
      {
        counter ++;
        http.begin("http://192.168.17.223:8000/api/brillo/central/"+String(counter));
        int httpResponseCode = http.GET();
      }
    }
  }
  a_last_state = a_state;

  
}
