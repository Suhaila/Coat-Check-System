/**
 * A Mirf example to test the latency between two Ardunio.
 *
 * Pins:
 * Hardware SPI:
 * MISO -> 12
 * MOSI -> 11
 * SCK -> 13
 *
 * Configurable:
 * CE -> 8
 * CSN -> 7
 *
 * Note: To see best case latency comment out all Serial.println
 * statements not displaying the result and load 
 * 'ping_server_interupt' on the server.
 */

#include <SPI.h>
#include <Mirf.h>
#include <nRF24L01.h>
#include <MirfHardwareSpiDriver.h>

char msg = 0;
char msg2 = 0;
void setup(){
  Serial.begin(9600);
  pinMode(6, OUTPUT);
  digitalWrite(6, HIGH);

  Mirf.spi = &MirfHardwareSpi;
  Mirf.init();
  Mirf.setRADDR((byte *)"clie1"); // Config recieving address
  Mirf.payload = sizeof(byte);  // set payload length   
  Mirf.config();
  
  Serial.println("Beginning ... "); 
  digitalWrite(6,LOW);
}

void loop(){
  
  unsigned long time = millis();
  
  while (Serial.available()>0){
    msg = Serial.read();
    Serial.println(msg);
  }
  

  Mirf.setTADDR((byte *)"serv1");
  
  Mirf.send((byte *) &msg);
  while(Mirf.isSending()){
  }
  
  //Serial.println("Finished sending");
  delay(10);
  while(!Mirf.dataReady()){
    //Serial.println("Waiting");
    if ( ( millis() - time ) > 1000 ) {
      Serial.println("Timeout on response from server!");
      return;
    }
  }
  
  Mirf.getData((byte *) msg2);
  Serial.println(msg2);
  //Serial.println("Got response.");
  
  delay(1000);
  
} 
  
  
  
