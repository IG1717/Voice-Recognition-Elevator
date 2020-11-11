#include <Servo.h>

Servo servo_test;

int angle = 0;
int incomingByte = 0;

void setup()
{
  servo_test.attach(9);
  Serial.begin(9600);
}
void loop()
{
  //servo_test.write(180);

   if (Serial.available() > 0) {
                // read the incoming byte:
                incomingByte = Serial.read();

                // say what you got:
                Serial.print("I received: ");
                Serial.println(incomingByte, DEC);
        }
}
