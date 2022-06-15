#Utiliza-se a api 'openWeather', para obter os dados climáticos.
import os

import requests

def getWeather(cidade, api_key): 
    resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric")

    if resp.status_code == 404:
        #se retornar not_found, retorna-se o status_code em vez de resp em si. 
        return resp.status_code

    return resp.json()