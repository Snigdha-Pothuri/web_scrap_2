from scraper_project import Star_names
from bs4 import BeautifulSoup
import requests 
import pandas as pd 
url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs" 
page=requests.get(url) 
soup=BeautifulSoup(page.text,"html.parser")
Star_table=soup.find_all("table")
print(len(Star_table)) 
temp_list=[]
table_rows=Star_table[7].find_all("tr")
for i in table_rows:
    td=i.find_all("td")
    row=[j.text.rstrip() for j in td]  
    temp_list.append(row) 
star_names=[]
distance=[]
mass=[]
radius=[] 
for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][0])
    distance.append(temp_list[i][5]) 
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8]) 
df=pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns=["star_names","distance","mass","radius"])
df.to_csv("stars.csv")
