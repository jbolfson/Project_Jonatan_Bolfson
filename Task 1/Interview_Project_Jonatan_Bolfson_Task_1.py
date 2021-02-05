# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# OBTIENE LOS TIPOS DE CAMBIO PARA LA FECHA 3 DE ABRIL DE 2017

import http.client

conn = http.client.HTTPSConnection("fixer-fixer-currency-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "be0d3d0e8dmsh5ae218bbc123ce0p15bb8djsn68c5738e4831",
    'x-rapidapi-host': "fixer-fixer-currency-v1.p.rapidapi.com"
    }

conn.request("GET", "/2017-04-03?base=USD&symbols=AUD%2CBRL%2CGBP", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


#EL OUTPUT DA AUD: 1.314897, BRL:3.113974, GBP: 0.80057 EN FORMATO JSON. 
# AHORA IMPORTO  DONDE ESTAN LAS MONEDAS Y LAS CONVIERTO PARA QUE QUEDE TODO HOMOGENEO EN DOLARES


#importo librerias que voy a usar

import pandas as pd
import numpy as np

#importo el dataframe

df = pd.read_excel (r'C:\Users\ros_r\Desktop\RGA\datasources\Employee_Roster_Data.xlsx')

#convierto todo a usd dados los distintos tipos de cambio

df['Salary'] = np.where(df['Currency'] == 'GBP',
                                           df['Salary'] *(1/0.80057)  ,
                                           df['Salary'])

df['Salary'] = np.where(df['Currency'] == 'BRL',
                                           df['Salary'] * (1/3.113974) ,
                                           df['Salary'])

df['Salary'] = np.where(df['Currency'] == 'AUD',
                                           df['Salary'] * (1/1.314897),
                                           df['Salary'])

#dejo todas las monedas expresadas en USD
df['Currency'] = 'USD'

#export el excel para despues subirlo a sql
df.to_excel(r'C:\Users\ros_r\Desktop\RGA\datasources\Employee_Roster_Data_USD.xlsx')