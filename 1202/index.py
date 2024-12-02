import requests
import json

url = "https://koreanjson.com/posts"
res = requests.get(url)

# print(res) # Response [200] 200-> 성공했다는 뜻
# print(res.json())

if res.status_code == 200:
    data = res.json()
    for i in data:
        print(f"ID : {i["id"]}, 제목 : {i["title"]}")
else:
    print("요청 실패")

with open("data.json", "w", encoding="utf-8") as file: # 자주사용하게 될 코드, json
    json.dump(data, file, ensure_ascii=False, indent=4) # indent 들여쓰기 / 아스키값 안바꿔주면 아스키값으로 온다.