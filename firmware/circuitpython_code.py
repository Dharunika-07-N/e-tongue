import time
import wifi
import socketpool
import ssl
import adafruit_requests
import analogio
import board

SSID = "YOUR_SSID"
PASSWORD = "YOUR_PASS"
ENDPOINT = "http://192.168.0.10:8000/api/v1/sensor/ingest"

channels = [
    analogio.AnalogIn(board.A0),
    analogio.AnalogIn(board.A1),
    analogio.AnalogIn(board.A2),
    analogio.AnalogIn(board.A3),
    analogio.AnalogIn(board.A4),
    analogio.AnalogIn(board.A5),
]

wifi.radio.connect(SSID, PASSWORD)
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

while True:
    values = [ch.value for ch in channels]
    payload = {"sensor_id": "cp-01", "values": values}
    try:
        requests.post(ENDPOINT, json=payload)
    except Exception as exc:
        print("post failed", exc)
    time.sleep(2)

