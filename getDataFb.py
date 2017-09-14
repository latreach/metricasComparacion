# encoding: utf-8
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



####Token
token = ''
fb = facebook.GraphAPI(token)

fechaInicial = datetime.datetime(2016,1,1)
fechaFinal = datetime.date.today()
fechaFinal = datetime.datetime(fechaFinal.year, fechaFinal.month,
                               fechaFinal.day)
periodo = datetime.timedelta(days=1)
formato = '%Y-%m-%d'
secuenciaFecha = []
while fechaFinal < fechaFinal:
    secuenciaFecha.append(fechaInicial.strftime(formato))
    fechaInicial += periodo

len(secuenciaFecha)

####urls de búsqueda

url1 = "me/insights/page_fan_adds?since="
url2 = "me/insights/page_engaged_users?since="
url3 = "me/insights/page_impressions?since="

it = iter(secuenciaFecha)
it1 = iter(secuenciaFecha[1:])


llamadasFans = []
llamadasEnganche = []
llamadasImpresiones = []

for i in it:
    llamada1 = ''.join([url1, i, '&until=', next(it)])
    llamadasFans.append(llamada1)

for i in it1:
    llamada1 = ''.join([url1, i, '&until=', next(it1)])
    llamadasFans.append(llamada1)

it = iter(secuenciaFecha)
it1 = iter(secuenciaFecha[1:])

for i in it:
    llamada1 = ''.join([url2, i, '&until=', next(it)])
    llamadasEnganche.append(llamada1)

for i in it1:
    llamada1 = ''.join([url2, i, '&until=', next(it1)])
    llamadasEnganche.append(llamada1)



it = iter(secuenciaFecha)
it1 = iter(secuenciaFecha[1:])

for i in it:
    llamada1 = ''.join([url3, i, '&until=', next(it)])
    llamadasImpresiones.append(llamada1)

for i in it1:
    llamada1 = ''.join([url3, i, '&until=', next(it1)])
    llamadasImpresiones.append(llamada1)

fansAdds = []
numeros = 0

for i in llamadasFans:
    numeros = numeros + 1
    print(numeros)
    fan = fb.get_object(i)
    fan = fan['data']
    valor = fan[0]['values'][0]['value']
    fecha = removeMinutes(fan[0]['values'][0]['end_time'])
    diccionario = dict(fecha = fecha)
    diccionario.update(valor = valor)
    diccionario.update(tipo = 'fan_adds')
    fansAdds.append(diccionario)
    time.sleep(1.5)

fansEnganche = []
numeros = 0

for i in llamadasEnganche:
    numeros = numeros +1
    print(numeros)
    enganche = fb.get_object(i)
    enganche = enganche['data']
    valor = enganche[0]['values'][0]['value']
    fecha = removeMinutes(enganche[0]['values'][0]['end_time'])
    diccionario = dict(fecha = fecha)
    diccionario.update(valor = valor)
    diccionario.update(tipo = 'fan_engaged_users')
    fansEnganche.append(diccionario)
    time.sleep(1.5)

fansImpresiones = []
numeros = 0

for i in llamadasImpresiones:
    numeros = numeros +1
    print(numeros)
    impresion = fb.get_object(i)
    impresion = impresion['data']
    valor = impresion[0]['values'][0]['value']
    fecha = removeMinutes(impresion[0]['values'][0]['end_time'])
    diccionario = dict(fecha = fecha)
    diccionario.update(valor = valor)
    diccionario.update(tipo = 'fan_engaged_users')
    fansEnganche.append(diccionario)
    time.sleep(1.5)


llamadasG = np.r_[llamadasFans, llamadasEnganche, llamadasImpresiones]

datosInsights = []
numeros = 0

for i in llamadasG:
    numeros = numeros +1
    data = fb.get_object(i)
    data = data['data']
    valor = data[0]['values'][0]['value']
    fecha = removeMinutes(data[0]['values'][0]['end_time'])
    tipo =  data[0]['name']
    diccionario = dict(fecha = fecha)
    diccionario.update(valor = valor)
    diccionario.update(tipo = tipo)
    datosInsights.append(diccionario)
    print(numeros)
    print(diccionario)
    time.sleep(1.5)

dataInsights = pd.DataFrame.from_dict(datosInsights)
dataInsights.to_csv('./data/datosInsightsFb.csv', header=True,
                    index=False, encoding='utf-8')

"""

PRUEBA
"""
url1G = "me/insights/page_fan_adds?since=2016-01-01&until=2017-09-05&limit=100"
url2G = "me/insights/page_engaged_users?since=2016-01-01&until=2017-09-05&limit=100"
url3G = "me/insights/page_impressions?since=2016-01-01&until=2017-09-05&limit=100"

datosFanAdd = fb.get_object(url1G)
datosFanAddLista = datosFanAdd['data']
