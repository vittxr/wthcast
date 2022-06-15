import os
from os.path import exists

from app.main import main  
from flask import render_template, request
from app.static.py.getWeatherData import getWeather

@main.route("/")
def index(citySearched = None):
    global citySearchedData
    citySearchedData = getWeather('Campinas', os.getenv("WEATHER_API")) #cidade padrão
    if citySearched != None: 
        print(citySearched)
        citySearchedData = getWeather(citySearched, os.getenv("WEATHER_API"))

    if citySearchedData == 404:
        #se citySearched retorna um erro de requisição, aqui se trata o erro. 
        citySearchedData = getWeather('Campinas')
        error='cidade inválida!'
        return render_template("pages/weather_page.html", dataWeather=citySearchedData, error=error)

    return render_template("pages/weather_page.html", dataWeather=citySearchedData)


cidades = ''
@main.route('/cidades')
def cidades_info():
    global cidades
    if cidades == '':
        #para evitar várias requisições na api, declara-se cidades como uma variável global. A condição só será executada quando a variável for vazia, ou seja, na primeira execução do código.
        cidades = {
            'curitiba': getWeather('curitiba', os.getenv("WEATHER_API")), 
            'paranagua': getWeather('paranagua', os.getenv("WEATHER_API")),
            'londrina': getWeather('londrina', os.getenv("WEATHER_API")),
            'maringa': getWeather('maringa', os.getenv("WEATHER_API")),
            'cascavel': getWeather('cascavel', os.getenv("WEATHER_API")),
            'apucarana': getWeather('apucarana', os.getenv("WEATHER_API")),
            'sao paulo': getWeather('sao paulo', os.getenv("WEATHER_API")),
            'campinas': getWeather('campinas', os.getenv("WEATHER_API")),
            'guarulhos': getWeather('guarulhos', os.getenv("WEATHER_API")),
            'santos': getWeather('santos', os.getenv("WEATHER_API")),
        }

    return render_template("pages/cidades.html", cidades=cidades)

@main.route('/search', methods=['GET', 'POST'])
def searchCity():
    citySearched = request.form.get("search-input")
    return index(citySearched)