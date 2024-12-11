import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager
import pandas as pd

# 폰트 설정
path = "C:\\Windows\\Fonts\\NanumBarunGothicUltraLight.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)

# print(sns.get_dataset_names())
import matplotlib.pyplot as plt

# 예제 데이터
tips = sns.load_dataset('tips')
# print(tips.head())

# 산점도
'''
sns.scatterplot(
    x = "total_bill",
    y = 'tip',
    hue = 'size',
    style = 'time',
    size = 'size',
    data = tips
)
'''
'''
sns.stripplot( # 점들이 한줄로 나열, 데이터가 겹칠 수 있음
    x = 'day',
    y = 'total_bill',
    data = tip,
    jitter=True, # 점들을 수평으로 좀 흩어서 겹침을 줄임
    hue='size',
    dodge=True # 여러 카테고리를 나란히 배치
)
sns.swarmplot( # 점들이 겹치지 않도록 배치
    x = 'day',
    y = 'total_bill',
    data = tip,
    hue='size',
    dodge=True # 여러 카테고리를 나란히 배치
)
# 관계형 플롯
sns.relplot(
    x='total_bill',
    y = 'tip',
    data=tips,
    style='time',
    hue = 'sex'
)

# 카테고리형 데이터의 분포를 시각화
sns.catplot(
    x = 'day',
    y = 'total_bill',
    data=tips,
    hue = 'sex',
    kind='point'
)
'''
# 데이터의 분포를 시각화
# sns.displot(tips['total_bill'], bins=30, kde=True) # kde= True면 바와 곡선이 같이 나온다.

# 히트맵
# import numpy as np

# data = np.random.rand(10, 10)
# sns.heatmap(data, annot=True, fmt='.2f')

# 한번에 시각화
# sns.pairplot(tips, hue='sex')

# 회귀선이 포함된 산점도
# sns.regplot(x = 'total_bill', y='tip', data=tips)

# 실습
# penguins = sns.load_dataset('penguins')
# flights = sns.load_dataset('flights')
titanic = sns.load_dataset('titanic')

# 펭귄
# print(penguins.head())
# sns.barplot(data=penguins, hue='species', y='body_mass_g', width = 0.7)

# sns.scatterplot(
#     data=penguins,
#     x = 'bill_length_mm',
#     y = 'bill_depth_mm',
#     hue='species'
#     )

# sns.catplot(
#     x = 'island',
#     y = 'body_mass_g',
#     data=penguins,
#     kind='violin'
# )

# 비행
# passengers = flights.groupby('year')['passengers'].mean().reset_index()

#reset_index() : 인덱스를 초기화, 기존 인덱스를 데이터프레임의 열로 변환해준다.

# plt.plot(passengers, marker='o')
# plt.title("연도별 평균 승객 수")
# plt.xlabel("year")
# plt.ylabel("passengers")

# plt.show()

# print(flights.head())


# flights_pivot = flights.pivot(index='month', columns='year', values='passengers')


# sns.heatmap(flights_pivot, annot=True, fmt='d')
# flights_year = flights[flights['year'] == 1958]

# sns.barplot(flights_year, x='month', y='passengers')
# plt.title("1958년 월별 승객 수")

# print(titanic.head())
# sns.catplot(
#     x = 'class',
#     y = 'survived',
#     data=titanic,
#     kind='bar'
# )

sns.kdeplot(
    data=titanic,
    x = 'age',
    y = 'survived',
    fill= True
)
plt.title("생존여부에 따른 나이 분포")
plt.show()