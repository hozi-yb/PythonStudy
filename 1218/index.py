import requests
import pandas as pd
import folium
import cv2
from folium.plugins import HeatMap, MarkerCluster

def MountainFireData():
    API_url = "https://eonet.gsfc.nasa.gov/api/v3/events?category=severeStorms,wildfires"
    params = {
        "category": "wildfires",
        "status": "open",
    }
    res = requests.get(API_url, params=params)
    if res.status_code == 200:
        return res.json()
    else:
        return None  

datas = MountainFireData()

fire_data = []
if datas:  
    for data in datas['events']: 
        fire_data.append({
            "title": data['title'], 
            "categories": [cat['title'] for cat in data['categories']],
            "date": data['geometry'][0]['date'],
            "magnitudeValue" : data['geometry'][0]['magnitudeValue'],
            "latitude" : data['geometry'][0]['coordinates'][1],
            "longitude" :  data['geometry'][0]['coordinates'][0]
        })

fire_data_df = pd.DataFrame(fire_data)
print(fire_data_df)
    
my_map = folium.Map(location=[36.841375, 127.930471], zoom_start=3)


# 마커추가

heatmap_data = [] 

markers = MarkerCluster().add_to(my_map)

for _, row in fire_data_df.iterrows():
    popup_info = f"""
    <b>지역</b> {row["title"]}<br/>
    <b>특징</b> {row["categories"]}<br/>
    <b>면적</b> {row["magnitudeValue"]}<br/>
    <b>날짜</b> {row["date"]}
    """

    # 마커 생성
    folium.Marker(
        location=[row["latitude"], row['longitude']],
        popup = folium.Popup(popup_info, max_width=300),
        icon= folium.Icon(color="red", icon="fire")
    ).add_to(markers)

    # 히트맵 데이터 추가
    heatmap_data.append([row["latitude"], row['longitude']])



HeatMap(heatmap_data).add_to(my_map)


my_map.save("./1218/Fire.html")


#============위성 이미지 다운로드
def download_image():
    url = "https://wvs.earthdata.nasa.gov/api/v1/snapshot"
    params = {
        "REQUEST" : "GetSnapshot",
        "BBOX" : "-90, -180, 90, 180",
        "LAYERS" : "VIIRS_SNPP_CorrectedReflectance_TrueColor",
        "CRS" : "EPSG:4326",
        "FORMAT" : "image/png",
        "WIDTH" : "1920",
        "HEIGHT" : "1080",
        "TIME" : "2024-11-01"
    }
    
    res = requests.get(url, params=params, stream=True)
    with open("./1218/test.png", "wb") as file:
        for chunk in res.iter_content(1024):
            file.write(chunk)
    
#--------------opencv
def fire_result():
    image = cv2.imread("./1218/test.png")
    if image is None:
        return


