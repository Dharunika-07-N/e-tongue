#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "YOUR_SSID";
const char* pass = "YOUR_PASS";
const char* endpoint = "http://192.168.0.10:8000/api/v1/sensor/ingest";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

void loop() {
  int sweet = analogRead(34);
  int sour  = analogRead(35);
  int salty = analogRead(32);
  int bitter= analogRead(33);
  int pung  = analogRead(25);
  int astr  = analogRead(26);

  String payload = "{\"sensor_id\":\"esp32-01\",\"values\":[" +
    String(sweet)+","+String(sour)+","+String(salty)+","+String(bitter)+","+String(pung)+","+String(astr)+"]}";

  HTTPClient http;
  http.begin(endpoint);
  http.addHeader("Content-Type", "application/json");
  http.POST(payload);
  http.end();
  delay(2000);
}

