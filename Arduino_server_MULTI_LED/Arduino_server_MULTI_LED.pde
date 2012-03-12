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
  
  //Pins for LEDs
  pinMode(2, OUTPUT); 
  digitalWrite(2, LOW);
  pinMode(3, OUTPUT); 
  digitalWrite(3, LOW);
  pinMode(4, OUTPUT); 
  digitalWrite(4, LOW);
  pinMode(5, OUTPUT); 
  digitalWrite(5, LOW);
  pinMode(6, OUTPUT); 
  digitalWrite(6, LOW);
  pinMode(9, OUTPUT); 
  digitalWrite(9, LOW);
  pinMode(10, OUTPUT); 
  digitalWrite(10, LOW);
  
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

     if (msg == '1'){
       if (state == 0){
         digitalWrite(2, HIGH);
         state = 1;
       } else {
         digitalWrite(2,LOW);
         state = 0;
       }
     }else if (msg == '9'){
       if (state == 0){
         digitalWrite(3, HIGH);
         state = 1;
       } else {
         digitalWrite(3,LOW);
         state = 0;
       }
    }else if (msg == '3'){
       if (state == 0){
         digitalWrite(4, HIGH);
         state = 1;
       } else {
         digitalWrite(4,LOW);
         state = 0;
       }
    }else if (msg == '4'){
       if (state == 0){
         digitalWrite(5, HIGH);
         state = 1;
       } else {
         digitalWrite(5,LOW);
         state = 0;
       }
    }else if (msg == '8'){
       if (state == 0){
         digitalWrite(6, HIGH);
         state = 1;
       } else {
         digitalWrite(6,LOW);
         state = 0;
       }
    }else if (msg == '6'){
       if (state == 0){
         digitalWrite(9, HIGH);
         state = 1;
       } else {
         digitalWrite(9,LOW);
         state = 0;
       }
    }else if (msg == '7'){
       if (state == 0){
         digitalWrite(10, HIGH);
         state = 1;
       } else {
         digitalWrite(10,LOW);
         state = 0;
       }
    }
     else if (msg == 'E'){
       digitalWrite(2,LOW);
       digitalWrite(3,LOW);
       digitalWrite(4,LOW);
       digitalWrite(5,LOW);
       digitalWrite(6,LOW);
       digitalWrite(9,LOW);
       digitalWrite(10,LOW);
     }
    Serial.println("Reply sent.");
  }
}
