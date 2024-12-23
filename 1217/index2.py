import folium
import requests
import pandas as pd

API_KEY = "e07a3d8bb6c822f62e9e8a7f2dc177d7"


# 날씨 데이터를 가져오기
def get_weather_data(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=kr"
    res = requests.get(url)

    if res.status_code == 200:
        return res.json()
    else:
        return None
    
cities = [
    {"name" : "서울", "lat" : 37.559688, "lon" : 126.983021},
    {"name" : "부산", "lat" : 35.161775, "lon" : 129.080321},
    {"name" : "대전", "lat" : 36.341470, "lon" : 127.461439},
    {"name" : "대구", "lat" : 35.820541, "lon" : 128.634670},
    {"name" : "제주", "lat" : 33.412320, "lon" : 126.695784},
    {"name" : "광주", "lat" : 35.160157, "lon" : 126.972935},
    {"name" : "독도", "lat" : 37.24148481027095, "lon" : 131.86505234125974},
    {"name" : "울릉도", "lat" : 37.484655, "lon" : 130.905280}
]

# 날씨 데이터 리스트
weather_data = []

for city in cities:
    data = get_weather_data(city["lat"], city["lon"])
    if data:
        weather_data.append({
            "city" : city["name"],
            "temperature" : data['main']['temp'],
            "weather" : data['weather'][0]['description'],
            "latitude" : city["lat"],
            "longitude" : city["lon"]
        })

weather_df = pd.DataFrame(weather_data)
print(weather_df)

my_map = folium.Map(location=[36.841375, 127.930471], zoom_start=7)

# 마커추가
for _, row in weather_df.iterrows():
    popup_info = f"""
    <b>지역</b> {row["city"]}<br/>
    <b>온도</b> {row["temperature"]} ℃<br/>
    <b>날씨</b> {row["weather"]}
    """

    # 날씨에 따라서 마커 색상
    icon_color =  "blue" if row["temperature"]< 0 else "green"

    # 마커생성
    folium.Marker(
        location=[ row["latitude"], row['longitude']],
        popup = folium.Popup(popup_info, max_width=300),
        icon= folium.Icon(color=icon_color, icon="cloud")
    ).add_to(my_map)

my_map.save("./1217/my_map.html")


""" 배포
웹은 index 이름을 제일 먼저 찾는다. 그래서 html index로

깃에 올린다.
셋팅에서 페이지
브랜치 메인으로 바꾸고 세이브
"""