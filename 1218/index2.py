import requests
import numpy as np
import pandas as pd
import folium
import cv2
from folium.plugins import HeatMap, MarkerCluster
from geojson import Feature, FeatureCollection, Point


# fire 데이터
def get_fire_data():

    features = []

    API_url = "https://eonet.gsfc.nasa.gov/api/v3/events"
    params = {
        "category": "wildfires",
        "status": "open",
        # "limit" : 5
    }

    res = requests.get(API_url, params=params)
    api_data = res.json()

    # events = api_data['events']

    # 딕셔너리 일때
    ## get()  메서드
    # 딕셔너리.get(키값, 반환될 값의 타입 or 값)
    # data = {"events" : ["이벤트1", "이벤트2"]}
    # print(data.get("geometry", [{}]))  # 리스트안에 들어있는 객체라든지 다 가져올 수 있다. get


    for event in api_data.get("events", []):
        title = event["title"]
        geometry = event['geometry']
        date = geometry[0]['date']
        magnitude = geometry[0]["magnitudeValue"] is not None

        features.append(
            Feature(
                geometry = Point([geometry[0]['coordinates'][0], geometry[0]['coordinates'][1]]),
                properties = {"name" : title, "magnitude" : magnitude, "date" : date}
            )
        )
        geojson_data = FeatureCollection(features)
        return geojson_data


# 시각화
def fire_map():
    m = folium.Map(location=[41.025961, 68.299290], zoom_start=5)

    # geo_json 데이터 가져오기
    fire_data = get_fire_data()

    folium.GeoJson(
        fire_data,
        name = "화재 데이터",
        tooltip=folium.GeoJsonTooltip(
            fields=["name", "magnitude", "date"],
            aliases=["지역명", "면적", "날짜"]
        )
    ).add_to(m)

    heat_data = [

        [ feature["geometry"]["coordinates"][1], feature["geometry"]["coordinates"][0] ] 
        for feature in fire_data["features"]
        if feature["properties"]["magnitude"] != None

    ]
    HeatMap(heat_data).add_to(m)

    m.save("./1218/map.html")


#============이미지 다운로드
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
    




# download_image()




'''
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
            "latitude" : data['geometry'][0]['coordinates'][1],
            "longitude" :  data['geometry'][0]['coordinates'][0]
        })

fire_data_df = pd.DataFrame(fire_data)
    
# my_map = folium.Map(location=[36.841375, 127.930471], zoom_start=3)


# # 마커추가

# heatmap_data = [] 

# markers = MarkerCluster().add_to(my_map)

# for _, row in fire_data_df.iterrows():
#     popup_info = f"""
#     <b>지역</b> {row["title"]}<br/>
#     <b>특징</b> {row["categories"]}<br/>
#     <b>날짜</b> {row["date"]}
#     """

#     # 마커 생성
#     folium.Marker(
#         location=[row["latitude"], row['longitude']],
#         popup = folium.Popup(popup_info, max_width=300),
#         icon= folium.Icon(color="red", icon="fire")
#     ).add_to(markers)

#     # 히트맵 데이터 추가
#     heatmap_data.append([row["latitude"], row['longitude']])



# HeatMap(heatmap_data).add_to(my_map)


# my_map.save("./1218/Fire.html")




url = "https://wvs.earthdata.nasa.gov/api/v1/snapshot?REQUEST=GetSnapshot&LAYERS=VIIRS_NOAA21_CorrectedReflectance_TrueColor,VIIRS_NOAA21_Thermal_Anomalies_375m_Day&CRS=EPSG:4326&TIME=2024-12-16&WRAP=DAY,&BBOX=-90,-180,90,180&FORMAT=image/jpeg&WIDTH=4096&HEIGHT=2048&AUTOSCALE=FALSE&ts=1734518467335"


image_ndarray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
img = cv2.imdecode(image_ndarray, cv2.IMREAD_COLOR)





img = cv2.resize(img, (1280, 1080))

cv2.imshow("Earth Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''