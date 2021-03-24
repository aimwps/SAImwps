import requests
from bs4 import BeautifulSoup

######## To the reviewer. This is in complete. Faced some issues and it probably doesnt make sense what i'm doiing sorry !


def rp(to_print):
    for i, line in enumerate(to_print):
        print(f"[{i}]: {line}")

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.YFsuGEP7RhE')
soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find(id="seven-day-forecast-list")
#days =  ["Today", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
c1 = list(content.children)

rp(c1)

day_report = {'day':[], 'day_tag':[], 'high_temp_tag':[], 'high_temp':[], "fore_cast":[], 'low_temp_tag':[], 'low_temp':[]}

forecast = ""
for i, day in enumerate(c1):
    if i%2 == 0:
        day_name =  day.find('p')
        day_report['day'].append(day_name.text)
        day_report['day_tag'].append('p')
        report =  day.find('img', alt=True)
        forecast += report['alt']
        high_temp_tag = day.find('p', class_="temp temp-high")
        day_report['high_temp_tag'].append("temp temp-high")
        high_temp = [int(x) for x in str(high_temp_tag).split(" ") if x.isnumeric()][0]
        day_report['high_temp'].append(high_temp)

    else:
        report =  day.find('img', alt=True)
        forecast += ". " + report['alt']
        day_report["fore_cast"].append(forecast)
        forecast = ""

        low_temp_tag = day.find('p', class_="temp temp-low")
        day_report['low_temp_tag'].append("temp temp-low")
        low_temp = [int(x) for x in str(low_temp_tag).split(" ") if x.isnumeric()][0]
        day_report['low_temp'].append(low_temp)

for item in day_report.values():
    print(item)
