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

#print(months)

sum_of_month = [] 
for month in months:
    total_monthly_precipitation = 0
    for element in seattle_data:
        if int(element['date'].split('-')[1]) == month:
            total_monthly_precipitation += element['value'] 
    sum_of_month.append(total_monthly_precipitation)
#print(sum_of_month)


#2
#1)
total_yearly_precipitation = sum(sum_of_month)
#print(total_yearly_precipitation)

#2)
relative_sums = []
for number in sum_of_month:
    relative_monthly_precipitation = (number/total_yearly_precipitation)
    relative_sums.append(relative_monthly_precipitation)

#print(relative_sums)
results = {
    "Seattle": {
        "station": "GHCND:US1WAKG0038",  
        "state": "WA",
        "total_monthly_precipitation": sum_of_month,
        "total_yearly_precipitation": total_yearly_precipitation,
        "relative_monthly_precipitation": relative_monthly_precipitation
    }
 }
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(results, file, indent=4)

