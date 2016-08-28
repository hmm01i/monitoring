#include <ESP8266WiFi>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>

const int INPIN = 1
const int OUTPIN = 2

void setup(/* arguments */) {
  //set up stuff
  //we definitly want a REST API
}

void loop(/* arguments */) {
  /* code */
  /*do the actual thing
  continually probe the pin?
  digitalRead(INPIN)
  maybe listen for queries, probe then
  server.handleClient();
  but might be good to do routine checks.
  which could trigger output to pin2
  */
}
