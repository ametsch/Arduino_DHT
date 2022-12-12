/*
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at https://mozilla.org/MPL/2.0/.
 */

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
