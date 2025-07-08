import requests
from datetime import datetime
import time

LAT = 12.884330
LNG = 77.604362
parameters = {
    "lat":LAT,
    "lng":LNG,
    "formatted":0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise = sunrise.split("T")
sunrise = sunrise[1].split(":")

sunset = sunset.split("T")
sunset = sunset[1].split(":")

# now time
now = str(datetime.now())
now = now.split(" ")
now = now[1].split(":")
# print(now[0])
# print(sunrise[0])
# print(sunset[0])

response = requests.get(url = "http://api.open-notify.org/iss-now.json")
data = response.json()
iss_latitude = data["iss_position"]["latitude"]
iss_longitude = data["iss_position"]["longitude"]
print(iss_latitude)
print(iss_longitude)

def check_iss():
    lat_difference = abs(float(iss_latitude) - LAT)
    lng_difference = abs(float(iss_longitude) - LNG)

    # If it is dark
    if lat_difference <= 10 and lng_difference <= 10:
        print("Look Up")
    if  now[0] > sunset[0]:
        print("Dark")
    else:
        print("Light")

while True:
    check_iss()
    time.sleep(60000)