import sys, os
import facebook
import pandas as pd
import numpy as np
import datetime
import itertools
import re
import time
from itertools import chain
from datetime import timedelta, date

def removeMinutes(x):
    x  = re.sub('T.*', '', x)
    return(x)

def nombrarDict(x, string):
    string = str(string)
    y = {"_".join([string, k]): v for k, v in x.items()}
    return(y)


removeMinutes(str('2016-01-01T:12'))

####Token
token = 'EAACEdEose0cBAAD8koaTc0Ua9LCVHXAF2FIVdv15ZCvO9NLXnhfXiVboFcgOPNL973LVDmC1VYfdCxK6txrta9T7VoC8DZCXNG2fhIJhrZAETWp8SohMtgeSW8PrkFURlgofYKctTgFoWYiDBRKNXGiJpW49z9FARhbqLaZBGqyj75vD0pAZCYd7Sbq1XerGL2lO8S8zVKAZDZD'
fb = facebook.GraphAPI(token)

fechaInicial = datetime.datetime(2017,5,1)
fechaFinal = datetime.datetime(2017,9,1)
fechaFinal = datetime.datetime(fechaFinal.year, fechaFinal.month,
                               fechaFinal.day)
periodo = datetime.timedelta(days=1)
formato = '%Y-%m-%d'
secuenciaFecha = []

while fechaInicial < fechaFinal:
    secuenciaFecha.append(fechaInicial.strftime(formato))
    fechaInicial += periodo

len(secuenciaFecha)

#### url de búsqueda

url = "me/insights/page_actions_post_reactions_total?since="

it = iter(secuenciaFecha)
it1 = iter(secuenciaFecha[1:])

llamadasFans = []
llamadasReacciones = []
llamadasImpresiones = []

for i in it:
    llamada = ''.join([url, i, '&until=', next(it)])
    llamadasFans.append(llamada)

for i in it1:
    llamada = ''.join([url, i, '&until=', next(it1)])
    llamadasFans.append(llamada)

len(llamadasFans)

fansReacciones = []
numeros = 0

# love, wow, haha, anger, sorry

for i in llamadasFans[0:5]:
    numeros = numeros + 1
    print(numeros)
    fan = fb.get_object(i)
    fan = fan['data']
    valor = fan[0]['values'][0]['value']
    like = fan[0]['values'][0]['value']['like']
    love = fan[0]['values'][0]['value']['love']
    wow = fan[0]['values'][0]['value']['wow']
    haha = fan[0]['values'][0]['value']['haha']
    anger = fan[0]['values'][0]['value']['anger']
    sorry = fan[0]['values'][0]['value']['sorry']
    suma = sum(valor.values())
    fecha = removeMinutes(fan[0]['values'][0]['end_time'])
    diccionario = dict(fecha = fecha)
    diccionario.update(total = suma)
    diccionario.update(me_Gusta = like)
    diccionario.update(me_Encanta = love)
    diccionario.update(me_Sorprende = wow)
    diccionario.update(me_Haha = haha)
    diccionario.update(me_Enfada = anger)
    diccionario.update(me_Lamenta = sorry)
    diccionario.update(tipo = 'actions_post_reactions_total')
    fansReacciones.append(diccionario)
    time.sleep(1.5)

reacciones = pd.DataFrame.from_dict(fansReacciones)

# obj1 = pd.DataFrame.from_dict(fansReacciones)['valor']
# for i in obj1:
#     x = i.values()
#     z = sum(x)
#     print(z)


reacciones['fecha']
