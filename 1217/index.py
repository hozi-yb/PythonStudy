import folium
import pandas as pd
from geojson import Feature, FeatureCollection, Point, Polygon

#---------- 일반적 스타일 (OpenStreetMap)
# 지도 열기
# my_map = folium.Map(location=[37.565120, 126.980468], zoom_start=12) # location=[위도경도], 줌
# my_map.save("./1217/my_map.html")


#---- 지도 스타일 추가 (Positron, DarkMatter)
# my_map = folium.Map(location=[37.565120, 126.980468], zoom_start=12, tiles="CartoDB Positron")
# my_map.save("./1217/my_map.html")

# my_map = folium.Map(location=[37.565120, 126.980468], zoom_start=12, tiles="CartoDB DarkMatter")
# my_map.save("./1217/my_map.html")


#---- 지도에 마커추가
# my_map = folium.Map(location=[37.565120, 126.980468], zoom_start=12, tiles="CartoDB Positron")
# my_map = folium.Map(
#     location=[37.565120, 126.980468],
#     zoom_start=12,
#     tiles="https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
#     attr="Google"
#     )

# folium.Marker([37.580089, 126.976824], popup="경복궁").add_to(my_map) # 지도에 추가한다 # 기본마커
# folium.Marker([37.537903, 126.976803], popup="전쟁기념관", icon=folium.Icon(color="green", icon="flag")).add_to(my_map) # 마커 커스텀


#---- 영역표시
# my_map = folium.Map(location=[37.565120, 126.980468], zoom_start=13, tiles="CartoDB Positron")

# 원형영역
# folium.Circle(
    # location=[37.561268, 126.899738],
    # radius=300,
    # color='blue',
    # popup="집",
    # fill=True,
    # fill_color='green'
    # ).add_to(my_map)


#---- 딕셔너리 형태로 여러개 추가

#----- 실습 . 지하철역 데이터프레임으로 만들고 csv파일로 만들기
# 
# my_map = folium.Map(location=[37.565120, 126.980468], zoom_start=13, tiles="CartoDB Positron")
# 
# 서울 지하철 위도 경도
# map_info = [
    # {"location":[37.563389, 126.903397], "popup":"마포구청역"},
    # {"location":[37.556061, 126.910167], "popup":"망원역"},
    # {"location":[37.549634, 126.913955], "popup":"합정역"},
    # {"location":[37.559822, 126.942144], "popup":"신촌역"},
    # {"location":[37.598490, 126.915613], "popup":"응암역"}
# ]
# subway_df = pd.DataFrame(map_info)
# print(subway_df)
# 
# for _, info in subway_df.iterrows():
    # folium.Circle(
    # location=info['location'],
    # radius=300,
    # color='blue',
    # popup=info['popup'],
    # fill=True,
    # fill_color='yellow'
    # ).add_to(my_map)
# 
# 
# 
# subway_df.to_csv("./1217/subway.csv", index=False, encoding='utf-8')
# my_map.save("./1217/my_map.html")

#----- 실습 . 지하철역 데이터프레임으로 만들고 csv파일로 만들기
# 서울 지하철 위도 경도
"""
data = {
    "Station" : ["마포구청역", "망원역", "합정역", "신촌역", "응암역"],
    "Latitude" : [37.563389, 37.556061, 37.549634, 37.559822, 37.598490],
    "Longitude" : [126.903397, 126.910167, 126.913955, 126.942144, 126.915613]
}

subway_df = pd.DataFrame(data)

# csv파일 저장
subway_df.to_csv("./1217/subway.csv", index=False, encoding="utf-8")

# folium지도 제작

my_map = folium.Map(location=[37.577155, 126.915685], zoom_start=10, tiles="CartoDB Positron")

subway_df.apply(lambda x : folium.Marker(
    location=[x["Latitude"], x["Longitude"]],
    popup=x["Station"],
    icon=folium.Icon(color='blue', icon="star")
    ).add_to(my_map),
    axis=1 # 행단위로 적용할 것이다. 라고 적용해야한다.
)

# iterrows : 데이터프레임에서 행 단위로 반복하면서 인덱스와 행의 쌍을 반환하는 함수

my_map.save("./1217/my_map.html")
"""

############---------------------geojson

# #geojson 데이터 생성
# feature1 = Feature(geometry=Point((126.983021, 37.559688)), properties={"name" : "서울", "population": "970만"})
# feature2 = Feature(geometry=Point((129.080321, 35.161775)), properties={"name" : "부산", "population": "340만"})
# feature3 = Feature(geometry=Point((127.461439, 36.341470)), properties={"name" : "대전", "population": "150만"})
# feature4 = Feature(geometry=Point((128.634670, 35.820541)), properties={"name" : "대구", "population": "240만"})


# # geojson 여러개 하나로 묶기
# geojson_data = FeatureCollection([feature1, feature2, feature3, feature4])


# # 지도생성
# my_map = folium.Map(location=[36.650703, 127.959131], zoom_start=7)


# # geojson 콜렉션을 지도에 추가
# folium.GeoJson(
#     geojson_data,
#     name="GeoJSON Data",
#     tooltip=folium.GeoJsonTooltip(
#         fields=["name", "population"],  # 표시할 속성
#         aliases=["도시이름: ", "인구: "]  # 속성의 별칭
#     )
# ).add_to(my_map)

# my_map.save("./1217/my_map.html")



# 실습. GeoJSON
my_map = folium.Map(location=[36.650703, 127.959131], zoom_start=7)
polygon = [[[126.330240, 37.787648],
           [126.669443, 37.127039],
           [126.916635, 36.907738],
           [127.460459, 37.070081],
           [127.779062, 37.389364],
           [127.312143, 38.233435],
           [126.644724, 37.776794],
           [126.330240, 37.787648]]]

polygon_geo = Feature(geometry = Polygon(polygon), properties={"name" : "수도권"})

geojson_data = FeatureCollection([polygon_geo])

# 지도에 그리기
folium.GeoJson(
    geojson_data,
    name = "Korea Capital Area",
    tooltip=folium.GeoJsonTooltip(
        fields=["name"],  # 표시할 속성
        aliases=["영역이름: "]  # 속성의 별칭
    ),
    style_function=lambda x : {
        'fillColor': "yellow", # 다각형 내부색상
        'color' : 'black', # 테두리 색상
        'weight' : 2, # 테두리 두께
        'fillOpacity' : 0.5 # 내부 투명도
    }
).add_to(my_map)



my_map.save("./1217/my_map.html")