#include <Servo.h>

Servo servo_test;

int angle = 0;
int incomingByte = 0;

char serialData;
int pin=13;

void setup()
{
  servo_test.attach(9);
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
                  digitalWrite(pin, HIGH);}
                else if(serialData == '0') {
                  digitalWrite(pin, LOW);
                }
        }
}
