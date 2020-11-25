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
with open('singaporeMuseums.json', 'r', encoding="utf-8") as output:
    data = json.load(output)
    for museum in data:
        # 圖片
        photos = museum['PHOTOURL']
        name = museum['NAME']
        website = museum['HYPERLINK']
        long = museum['longitude']
        lat = museum['latitude']
        address = museum['Address']
        introduce = museum['Description']

        unit = Museum()
        unit.website = website
        unit.address = address
        unit.img = photos
        unit.city = City.objects.get(cid=112)
        unit.nation = Nation.objects.get(nid=65)
        unit.introduce = introduce
        unit.longitude = long
        unit.latitude = lat
        unit.mname = name
        unit.save()
