weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0]
]

city = input("도시 이름을 입력하세요: ")


filter_city = list(filter(lambda x: x[1] == city, weather_data))
temp_list = []
for i in range(len(filter_city)):
    temp_list.append(filter_city[i][2])
max_temp = max(temp_list)
print(max_temp)