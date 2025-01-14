#1. Monthly Precipitation
# 1) GHCND:US1WAKG0038
# 2)
import json
import csv

with open ('precipitation.json') as file:
    rain = json.load(file)
#print(rain)

with open ('stations.csv') as file:
    stations = list(csv.DictReader(file))


codes = [] 
for code in stations:
    codes.append(code['Station'])
#print(codes)
data_city = [] 
for code in codes:
    for element in rain:
        if element['station'] == code:
            data_city.append(element)
    total_monthly_precipitation = 0
    months = [] 
    for element in data_city:
        month = int(element['date'].split('-')[1]) 
        if month not in months:
            months.append(month)
    #print(months)
    sum_of_month = [] 
    for month in months:
        total_monthly_precipitation = 0
        for element in data_city:
            if int(element['date'].split('-')[1]) == month:
                total_monthly_precipitation += element['value'] 
                sum_of_month.append(total_monthly_precipitation)
 print
