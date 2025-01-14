#1. Monthly Precipitation
# 1) GHCND:US1WAKG0038
# 2)
import json
with open ('precipitation.json') as file:
    rain = json.load(file)
#print(rain)

seattle_data = [] 
for element in rain:
    if element['station'] == 'GHCND:US1WAKG0038':
        seattle_data.append(element)
#print(seattle_data)

# 3)

total_monthly_precipitation = 0

months = [] 
for element in seattle_data:
    month = int(element['date'].split('-')[1]) 
    if month not in months:
        months.append(month)

print(months)

sum_of_month = [] 
for month in months:
    for element in seattle_data:
        if int(element['date'].split('-')[1]) == month:
            total_monthly_precipitation += element['value'] 
    sum_of_month.append(total_monthly_precipitation)
print(sum_of_month)


with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(months, file)
    json.dump(sum_of_month, file)