# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 20:48:11 2020

@author: sauga
"""

import requests
import pandas as pd

url = "https://covid-19india-api.herokuapp.com/all"



#response = requests.request("GET", url, headers=headers, data = payload)
response=requests.get(url)

covid_data=response.json()
#print(covid_data[1]['state_data'])#List of Dict

covid_data_states=covid_data[1]['state_data']
covid_data_total=covid_data[0]#dict

df_states=pd.DataFrame(covid_data_states)
df_total=pd.DataFrame(covid_data_total,index=['details'])
print(df_states)
print(df_total)




