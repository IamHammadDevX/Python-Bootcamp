import requests


OWM_Endpoint = "http://api.openweathermap.org/data/2.5/onecall"
api_key = "18f282a7433c98e212108a590075c67d" # Open Weather API key

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key
}


respone = requests.get(url=OWM_Endpoint, params=weather_params)
respone.raise_for_status()
data = respone.json()
print(data)