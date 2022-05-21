import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

df = pd.read_csv('destinations_LP_crawler_Ex5.csv',encoding='latin-1')
LP_destinations = pd.DataFrame(df['city'])
LP_destinations['city'][22] = 'malopolska/krakow'
LP_destinations['city'][35] = 'dodecanese/kos'


API_KEY = ('ENTER YOUR KEY!!!!!!!')
response2 = []
for c in LP_destinations['city']:
    url2 = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (c,API_KEY)
    response2.append(requests.get(url2).json())

list2 = []
for tag2 in response2:
    list2.append(tag2['results'][0]['formatted_address'])
last_list = []
for country in list2:
    try:
        int(country.split(",")[-1])
        last_list.append(country.split(",")[-2].strip())
    except:
        last_list.append(country.split(",")[-1].strip())
LP_destinations['country'] = last_list
LP_destinations['city'][22] = 'krakow'
LP_destinations['city'][35] = 'kos'
list4 = []
htt = "https://www.lonelyplanet.com/"
for k in range(0,len(LP_destinations['city'])):
   html = requests.get(htt+LP_destinations.iloc[k]['country']+"/"+ df.iloc[k]['city_LP'])
   soup = BeautifulSoup(html.content,'html.parser')
   tags = soup("p")
   list1 = []
   for tag in tags: 
        list1.append(tag.get_text())   
   list4.append(list1[1])
LP_destinations['Description'] = list4
LP_destinations.to_csv(index=False)
LP_destinations.to_csv('C:/HW5/LP_destinations.csv',index=False)


      

      