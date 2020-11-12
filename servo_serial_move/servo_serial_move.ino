#include <Servo.h>

int servoPin = 3;

Servo Servo1;
int angle = 0;
int incomingByte = 0;

char serialData;
int pin=13;

void setup()
{
  Servo1.attach(3);
  Serial.begin(9600);

  pinMode(pin, OUTPUT);
}
void loop()
{
  //servo_test.write(180);

   if (Serial.available() > 0) {
                // read the incoming byte:
                if(Serial.available() > 0) {
                  serialData = Serial.read();
                  Serial.print(serialData);
                }

                if (serialData == '1') {
                  // Make servo go to 90 degrees
                    Servo1.write(90);
                    delay(1000);
                    Servo1.write(0);
                    delay(1000);
                    Serial.write("Terminate");
                    }
                else if(serialData == '0') {

                }
        }
}
