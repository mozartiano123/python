import requests
import time
city = "Jundiai"
api_key = "2929d0923092270785fec33e82af44d4"
api_endpoint = "http://api.openweathermap.org/data/2.5/onecall"

wheather_params = {
    "lat":-23.208770,
    "lon":-46.881430,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(api_endpoint, params=wheather_params)
response.raise_for_status()
weather_data = response.json()
# l1 = [item for i in range(0,12) for item in weather_data["hourly"][i]["weather"]]
first_list = [item for item in weather_data["hourly"]]
hourly_list = first_list[0:12]
print(len(hourly_list))
print(hourly_list)
#
# for i in range(0,12):
#      l1.append(weather_data["hourly"][i]["weather"])
#
for (i,weather_dict) in enumerate(hourly_list, start=0):
    weather_sub_list = weather_dict["weather"]
    for j in range(0,len(weather_sub_list)):
        # print(i)
        # print(weather_sub_list[j]["id"])
        if weather_sub_list[j]["id"] < 700:
            print(f"Vai chover daqui a {i} horas")
