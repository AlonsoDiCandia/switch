const int SENSOR_PIN = 12; 

// Variables will change:
int lastState =LOW;      
int currentState;
         
void setup() {
  
  Serial.begin(115200);
  // initialize the Arduino's pin as aninput
  pinMode(SENSOR_PIN,  INPUT_PULLUP);
}

void loop() {
  // read the state of the the input pin:
  currentState = digitalRead(SENSOR_PIN);

  if(lastState == LOW && currentState == HIGH)
    Serial.println("Sensor is ON");
  if(lastState == HIGH && currentState == LOW)
    Serial.println("Sensor is OFF");
  // save the the last state
  lastState = currentState;
}
