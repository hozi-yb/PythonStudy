import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager

path = "C:\\Windows\\Fonts\\NanumBarunGothicUltraLight.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)

file_name = "./1211/남녀연령별인구현황_월간.csv"

data = pd.read_csv(file_name, encoding="EUC-KR")


region_name = input("검색하고 싶은 지역명을 입력하세요: ")
data = data.rename(columns={"행정구역":"지역명"}) # 이름 다시 정하기

age_columns = [ col for col in data.columns if "세" in col] 

for col in age_columns:
    data[col] = data[col].astype(str)
    data[col] = data[col].str.replace(",", "").astype(int)

region_data = data[data["지역명"].str.contains(region_name, na=False)]

# 예외처리
if region_data.empty:
    print(f"{region_name}의 지역은 존재하지 않습니다.")

# 데이터 추출

man_columns = [ col for col in age_columns if "남" in col] # 새로추가
woman_columns = [ col for col in age_columns if "여" in col] # 새로추가

"""필터를 사용해서 데이터추출
man_columns = [col for col in data.columns.filter(like='남').columns if "총인구수" not in col and "연령구간인구수" not in nol]

filter() items = ["2024년11월__남_40~49세", "2024년11월_남_70~79세"]
"""


man_groups = [col.split("_남_")[1] for col in man_columns] # 새로추가
woman_groups = [col.split("_여_")[1] for col in woman_columns] # 새로추가

man_result = region_data[man_columns].iloc[0].values # 새로추가
woman_result = region_data[woman_columns].iloc[0].values# 새로추가

""" 조금 더 pandas 식 같은 함수이다.
woman_result = region_data[woman_columns].iloc[0].apply(lambda x : int(str(x).replace(","), ""))
"""

# 그래프 그리기
plt.figure(figsize=(10,5))

plt.plot(man_groups , man_result, marker="o", color = 'blue')
plt.plot(woman_groups , woman_result, marker="o", color = 'lightgrey')


plt.title(f"{region_name}의 연령대별 남성 및 여성 인구 비교")
plt.xlabel("연령대")
plt.xticks(rotation=45)
plt.ylabel("인구수")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(['남성', '여성'])
plt.show()




## pandas 벡터계산 
#위에서 반복문으로 했는데 그렇게 할 필요없이 바로 나온다..
'''
male_result = region_data[man_columns].iloc[0].astype(str).str.replace(",", "").astype(int)
'''

### apply() : 사용자 함수 정의 어플라이 안에 람다함수쓰면 된다.