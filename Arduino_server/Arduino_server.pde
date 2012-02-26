/**
 * An Mirf example which copies back the data it recives.
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
 */

#include <SPI.h>
#include <Mirf.h>
#include <nRF24L01.h>
#include <MirfHardwareSpiDriver.h>

byte state = 0;
char msg = 0;

void setup(){
  Serial.begin(9600);

  Mirf.spi = &MirfHardwareSpi;
  Mirf.init(); 
  Mirf.setRADDR((byte *)"serv1"); //Config reciving address
  Mirf.payload = sizeof(byte); // Set payload length
  Mirf.config();
  
  pinMode(6, OUTPUT); //Pin 6 is LED
  digitalWrite(6, LOW);
  
  Serial.println("Listening..."); 
}

void loop(){
  byte data[Mirf.payload]; // buffer to store the data

  if(!Mirf.isSending() && Mirf.dataReady()){
    //Serial.println("Got packet");

    Mirf.getData((byte *) &msg); // Get packet into the buffer
    Mirf.setTADDR((byte *)"clie1"); //Set the send address

    Mirf.send(data); // Send data back
    //Mirf.send((byte *) &msg);

     if (msg == '3'){
       if (state == 0)
       {
         digitalWrite(6, HIGH);
         state = 1;
       } else {
         digitalWrite(6,LOW);
         state = 0;
       }
     }else if (msg == 'E'){
       digitalWrite(6,LOW);
     }
    Serial.println("Reply sent.");
  }
}
