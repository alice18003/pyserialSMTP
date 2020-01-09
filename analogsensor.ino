const int SENSOR = A5;
const int SPEAKER = 13;
const int LED = 14;

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  while(!Serial);
}

void loop() {
  byte var = "2";
  int value = analogRead(SENSOR);
  if(value > 100){
      Serial.print(1);
  }else{
      Serial.print(0);
  }
  delay(500);
  var = Serial.read();
  if (var == '1'){
    play_speaker();
    delay(500);
  }else{
    digitalWrite(LED, HIGH);
    delay(500);
    digitalWrite(LED, LOW);
  }
  delay(2000);
}

void play_speaker(){
    int j;
    for(j = 0; j < 8; j++){
        tone(SPEAKER, 500, 100);
        delay(150);
        tone(SPEAKER, 250, 100);
        delay(150);
    }
}
