
import requests
#import os
from datetime import datetime


api_key = 'e2171780fb0d42d8d7d5a16b920d58e1'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
with open("weather.txt", "w") as output:
     output.write(str("\ncity name:"))
     output.write(str("ludhiana"))
     output.write(str("\ntemperature:"))
     output.write(str(temp_city))
     output.write(str("\nhumidity:"))
     output.write( str(hmdt))
     output.write(str("\nweather:"))

     output.write( str(weather_desc))
     output.write(str("\nwind speed:"))
     output.write( str(wind_spd))
     output.write(str("\ndate and time:"))
     output.write( str(date_time))


Enter the city name: ludhiana
-------------------------------------------------------------
Weather Stats for - LUDHIANA  || 23 Jun 2021 | 11:30:22 AM
-------------------------------------------------------------
Current temperature is: 44.49 deg C
Current weather desc  : clear sky
Current Humidity      : 9 %
Current wind speed    : 3.28 kmph
     
     
     
  
     
