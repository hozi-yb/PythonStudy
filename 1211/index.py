from pydataset import data
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager

path = "C:\\Windows\\Fonts\\NanumBarunGothicUltraLight.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)


# print(data())
# 상관관계 메서드 corr()

# mtcars = data('mtcars')


# print(mtcars.head()) # 상위 5개 데이터 뽑음

# mpg = mtcars.groupby('cyl')['mpg'].mean().reset_index() # 데이터프레임 평균값을 내려면 그룹바이. 인덱스값을 새로 만들어줌

# # print(mpg)
# sns.barplot(
#     data=mpg,
#     x = 'cyl',
#     y='mpg'
# )
# plt.title('실린더수에 따른 평균연비')

# hp = mtcars.groupby('am')['hp'].mean().reset_index()
# # print(hp)
# sns.barplot(
#     data=hp,
#     x='am',
#     y='hp'
# )
# plt.title('변속기 유형별 평균 마력')



# mpg_pivot = mtcars.pivot_table(index='gear', columns='cyl', values='mpg', fill_value=0) ## 피벗테이블. 중복된 데이터도 가능함.

# print(mpg_pivot)
# sns.heatmap(mpg_pivot, annot=True, fmt='.1f')
# mtcars_data = mtcars[['mpg', 'hp', 'wt']] # 데이터 컬럼 필터링,,


# mtcars_corr=mtcars_data.corr()
# sns.heatmap(data=mtcars_corr, annot=True, fmt='.1f', cmap = 'coolwarm')
# plt.show()
'''

# 리더님 코드

mtcars = data('mtcars')
#1번예제
#방법1
cyl_mpg = mtcars.groupby('cyl')['mpg'].mean()
plt.bar(cyl_mpg['cyl'], cyl_mpg['mpg'])
#방법2
cyl_mpg.plot(kind='bar')
plt.xticks(rotation=0)

#2번예제
am_hp = mtcars.groupby('am')['hp'].mean()
am_hp.plot(kind='bar', color='green')

#3번예제
cyl_gear = mtcars.pivot_table(index='cyl', columns= 'gear', values= 'mpg')
# pivot()은 중복된 조합이 있을경우 오류가 발생한다. 고유한 값이 보장될 때 사용
# pivot_table() 중복된 조합이 있을 경우에도 동작한다. 실무에 더 적합하다.
sns.heatmap(cyl_gear, annot=True, fmt='.2f')

'''