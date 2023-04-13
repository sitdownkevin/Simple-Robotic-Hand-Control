#define A1 1
#define A2 2
#define B1 3
#define B2 4
#define C1 5
#define C2 6
#define D1 7
#define D2 8
#define E1 9
#define E2 10

void setup() {
  for (int i=0; i<10; i++) {
    pinMode(i, OUTPUT); 
  }
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  Serial.println("Connected@UNO");
}

void loop() {
  if (Serial.available()) {
    String msg = Serial.readStringUntil('\n');

    if (isCMDLegal(msg)) {
      Serial.println("MSGReceived@UNO CMDLegal@UNO " + msg);
      blink(msg);
    }
    else {
      Serial.println("MSGReceived@UNO CMDILLegal@UNO " + msg);
    }
    delay(1000);
  }
}

void blink(String msg) {
  for (int i=0; i<10; i++) {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(50);
    digitalWrite(LED_BUILTIN, LOW);
    delay(50);
  }
}

// 判断信息是否合法
bool isCMDLegal(String msg) {
  if (msg.length() != 10) {return false;}
  for (int i=0; i<10; i++) {
    if (!(msg[i] == '0' || msg[i] == '1')) {
      return false;
    }
  }
  return true;
}
