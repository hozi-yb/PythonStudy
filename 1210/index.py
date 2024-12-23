import matplotlib.pyplot as plt
from matplotlib import font_manager

# 폰트 설정
path = "C:\\Windows\\Fonts\\NanumBarunGothicUltraLight.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)

#=--------------------
# 기본 히스토그램

"""
data = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 5, 6]

plt.hist(data, bins=5, color='green', histtype='barstacked')

#bins = 5 -> [1, 2], [2, 3], [3, 4], [4, 5], [5, 6] 이런식으로 x축 칸을 나눠준다.

plt.title('히스토그램')
plt.xlabel("값")
plt.ylabel('빈도수')
plt.show()
"""
# 여러개 데이터 히스토그램
"""
data1 = [1, 2, 2, 3, 3, 3, 4]
data2 = [2, 3, 3, 4, 4, 5, 6]

plt.hist([data1, data2], bins=5, color=['green', 'purple'], alpha=0.5, label=['data1', 'data2'])

plt.title("여러개 히스토그램")
plt.xlabel("값")
plt.ylabel('빈도수')
plt.legend()
plt.show()
"""

# 산점도
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]
# sizes = [20, 50, 80, 100, 200]
# colors = [10, 20, 30, 40, 50]

# plt.scatter(x, y, s=sizes, c=colors, cmap='viridis') # cmap -> 배열로 넣고자 하면 꼭 넣어줘야 한다.
# plt.colorbar(label = 'color bar')

# plt.show()

# 산점도 여러개 넣기. 난수를 사용하여
import numpy as np
'''

n = 50
x = np.random.rand(n) # 0과 1사이 난수 np.random.rand
y = np.random.rand(n)

area = (30 * np.random.rand(n)) ** 2 # 0 과 30 사이 난수 생성하고 제곱하여 크기 생성
colors = np.random.rand(n)

plt.scatter(x, y, s = area, c=colors, cmap='Spectral', alpha=0.5)
plt.show()
'''

# 파이차트
# sizes = [25, 25, 20, 20]
# lables = ['A', 'B', 'C', 'D']
"""
# 강조 파이차트
sizes = [15, 30, 45, 10]
labels = ['사과', '바나나', '포도', '체리']
explode = [0, 0.1, 0, 0] # 특정 요소 강조


plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, startangle= 140)

"""

# 색상꾸미기
# sizes = [ 10, 20 ,30 ,40]
# labels = ['A', 'B','C', 'D']
# colors = ['green', 'lightblue', 'purple', 'pink']

# plt.pie(sizes, labels=labels,
#         colors=colors,
#         autopct='%1.1f%%',
#         textprops={'fontsize' : 20, 'color' : 'darkblue'},
#         wedgeprops={'edgecolor':'black'})


# 도넛
'''
sizes = [40, 30, 20, 10]
labels = ['X', "Y", 'Z', 'W']
plt.pie(sizes, labels=labels, wedgeprops={'width' : 0.4})

plt.show()
'''

# 실습 1
'''
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sale_2019 = [100, 120, 140, 110, 130, 150, 160, 170, 180, 200, 190, 210]
sale_2020 = [ 90, 110, 130, 120, 140, 160, 170, 160, 150, 180, 200, 190]
labels = ['2019', '2020']

plt.figure(figsize=(10, 6)) # 그래프의 크기 창 크기를 키울 수 있다.
plt.plot(months, sale_2019)
plt.plot(months, sale_2020)

plt.legend(['2019', '2020'])
plt.title("Monthly Sales Comparison (2019-2020)")
plt.xlabel('Month')
plt.ylabel('Sale')

plt.show()

# 실습 2
categories = ['Categoty 1', 'Categoty 2', 'Categoty 3', 'Categoty 4', 'Categoty 5']
data = [20, 35, 15, 27, 45]

plt.bar(categories, data)

plt.grid(True, axis="both", linestyle="-", color="lightgrey")

plt.title("Bar Chart")
plt.ylim([0, 50])
plt.xlabel("Categories")
plt.xticks(rotation=45)
plt.ylabel("Values")
plt.axis("auto")
plt.show()
'''

'''
# 실습 3
sizes = [34, 32, 16, 18]
labels = ['Apple', "Banana", 'Melon', 'Grapes']
colors = ['red', 'yellow', 'green', 'purple']
explode = [0, 0.07, 0, 0.07]
plt.pie(sizes,
        labels=labels,
        colors=colors,
        explode=explode,
        autopct='%1.1f%%',
        wedgeprops={'width' : 0.7, 'edgecolor':'black'})

plt.show()
'''