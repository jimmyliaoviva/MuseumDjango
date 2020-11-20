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
            print(museum['Photos'][0]['FilePath'])
        except:
            print('No photo')
        print(museum['Name'])
        try:
            print(museum['Medies'][0]['Url'])
        except:
            print('no url')
        print(museum['Longitude'])
        print(museum['Latitude'])
        print(museum['Address'])
        print(museum['Description'])
        print('Taiwan')
        print(museum[''])

# unit = Company()
# unit.company_name = data['company_name']
# unit.company_stock = data['company_stock']
# unit.industry = data['industry']
# unit.csr_topics = data['csr_topics']
# unit.save()
