import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager

path = "C:\\Windows\\Fonts\\NanumBarunGothicUltraLight.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)

file_name = "./1211/연령별인구현황.csv"

data = pd.read_csv(file_name, encoding="EUC-KR")


region_name = input("검색하고 싶은 지역명을 입력하세요: ")
data = data.rename(columns={"행정구역":"지역명"}) # 이름 다시 정하기
age_columns = [ col for col in data.columns if "세" in col] # 세가 들어간 컬럼만 검색 나이만 검색하기 위해서 필터링 한것.


# 콤마 없애고 숫자로 변환
for col in age_columns:
    data[col] = data[col].str.replace(",", "").astype(int) # 판다스에서 int형으로 형변환

print(data)

# 필터링
# contains() : 문자열 데이터 필터링, 특정 패턴을 찾을 때
# na : 결측값(NaN)을 포함할지 결정(기본값 True)
# case : 영문의 대소문자 구분. 기본값  True
region_data = data[data["지역명"].str.contains(region_name, na=False)]

# 예외처리
if region_data.empty:
    print(f"{region_name}의 지역은 존재하지 않습니다.")

# 데이터 추출
age_groups = [col.split("_계_")[1] for col in age_columns] 



result = region_data[age_columns].iloc[0].values # 키 밸류 형태에서 밸류값만 가져옴. iloc로 인덱스로 값 가져옴.


# 그래프 그리기
plt.figure(figsize=(10, 8))
plt.plot(age_groups, result, marker = 'o', label = region_name)
plt.title(f"{region_name}의 연령별 인구 수", fontsize=16, pad=10)
plt.xlabel("연령대")
plt.ylabel("인구수")
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(rotation=45)
plt.legend()

plt.show()