import requests
from datetime import datetime
import time

MY_LAT = -23.208770 # Your latitude
MY_LONG = -46.881430 # Your longitude

def send_mail():
    print("Sorte DA PORRA")

def iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return (iss_latitude, iss_longitude)

    #Your position is within +5 or -5 degrees of the ISS position.

def is_iss_nearby():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])-3
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])-3
    iss = iss_position()
    time_now = datetime.now()
    if time_now.hour <= sunset or time_now.hour >= sunrise:
        if MY_LAT - 5 <= iss[0] <= MY_LAT + 5:
            if MY_LONG - 5 <= iss[0] <= MY_LONG + 5:
                send_mail()
                return True
    return False


while not is_iss_nearby():
    time.sleep(60)


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




