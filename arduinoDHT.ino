#include "DHT.h"
#include "DHT_U.h"
#include "string.h"

#define DHTTYPE DHT11   // DHT 11
#define DHTPIN 5     // Digital pin connected to the DHT sensor

const int analogInPin = A0;
DHT dht(DHTPIN, DHTTYPE);


void setup() {
  Serial.begin(115200);
  dht.begin();
}

void loop() {
  double f = dht.readTemperature(true);
  double h = dht.readHumidity();
  double l = double(analogRead(analogInPin)) / 5.0;

  String str = String("");
  str.concat(String(f));
  str.concat(", ");
  str.concat(String(h));
  str.concat(", ");
  str.concat(String(l));

  Serial.println(str);
}
