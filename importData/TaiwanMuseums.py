import json, os, sys
import django

project_dir = 'D:\\jimmy\\NCU\\5_master\\SE\\museum\\museum'
sys.path.append(project_dir)
print(sys.path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'museum.settings'
#
django.setup()

from main.models import *

# Id( 自動生成 ) 圖片(char) 名字(char)  官網(char) 經度(double) 緯度(double)
# 地址(char)intro (char)  nation (FK) 城市(FK)

with open('taiwanMuseums.json', 'r', encoding="utf-8") as output:
    data = json.load(output)
    for museum in data:
        try:
            photos = museum['Photos'][0]['FilePath']
        except:
            photo = 'No photo'
        name = museum['Name']
        try:
            website = museum['Medies'][0]['Url']
        except:
            website = ''
        long = museum['Longitude']
        lat = museum['Latitude']
        address = museum['Address']
        introduce = museum['Description']
        nation = 886
        city = museum['City']

        print(museum['Name'])
        unit = Museum()
        unit.website = website
        unit.address = address
        unit.img = photos
        unit.city = City.objects.get(cid=city)
        unit.nation = Nation.objects.get(nid=886)
        unit.introduce = introduce
        unit.longitude = long
        unit.latitude = lat
        unit.mname = name
        unit.save()
