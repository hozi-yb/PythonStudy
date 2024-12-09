import matplotlib.pyplot as plt
from matplotlib import font_manager
# 폰트 경로 찾기
# font_list = font_manager.findSystemFonts(fontpaths=None, fontext="ttf") 
# print(font_list)
# 폰트 설정
path = "C:\\Windows\\Fonts\\NanumBarunGothicUltraLight.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)

#----------------------------
# 선그래프, 막대그래프 모두 배열 개수는 똑같아야 한다.
"""
# 기본 그리기
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]


# plt.plot(x,y, color = "red", linestyle="--", linewidth=3, label="샘플그래프")
plt.plot(x,y, marker="h", markersize=14, markerfacecolor="yellow", markeredgecolor = "green")

font ={
    "size":20,
    "color":"white",
    "backgroundcolor":"black",
    "weight":"bold"
}

# plt.title("맷플롯립", pad=30, fontsize=20, color="#ff0000", backgroundcolor="green", fontweight= "bold")
plt.legend(title="범례명", fontsize=13, loc="upper center") # upper, lower, right, center, left

plt.grid(True, axis="both", linestyle=":", color="blue", alpha=0.3) # alpha 연하게

plt.title("맷플롯립", pad=10, fontdict=font)
plt.xlabel("x축", fontdict=font, labelpad=10)
plt.ylabel("y축", fontdict=font)

# plt.xlim([0, 10])
# plt.ylim([0, 15])
# plt.axis("equal") # x축과 y축을 동일하게 유지
# plt.axis("scaled") # 비율에 맞춰서 생성이된다,.
# plt.axis("tight")
plt.axis("auto")
plt.axis([0, 10, 0, 15]) # 수동으로 넣을 수 있다. 위에 xlim과 ylim과 같다.



plt.show()
"""
# 그래프 선 여러개 그리기
# x = [1, 2, 3, 4]
# y1 = [1, 2, 3, 4]
# y2 = [2, 4, 6, 8]
# y3 = [3, 6, 9, 12]
# y4 = [4, 8, 12, 16]
# plt.plot(x,y1, label='y=x', color='red', marker= 'o')
# plt.plot(x,y2, label='y=2x', color='orange', marker='+')
# plt.plot(x,y3, label='y=3x', color='green', marker = '>')
# plt.plot(x,y4, label='y=4x', color='blue', marker="<")

# plt.legend(loc='upper center', title = '4개 연습', ncol=2) # ncol 범례에서 몇 줄로 보여줄건지.
# plt.title("그래프 그리기 연습")
# plt.xlabel("x값")
# plt.ylabel("y값")
# plt.show()

# 그래프 여러개
"""
x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [2, 4, 6, 8]
y3 = [3, 6, 9, 12]
y4 = [4, 8, 12, 16]
plt.subplot(2, 2, 1) # 2*2배열 중 첫번째.
plt.plot(x, y1)
plt.title("x=y")

plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.title("y=2x")

plt.subplot(2, 2, 3)
plt.plot(x, y3)
plt.title("y=3x")

plt.subplot(2, 2, 4)
plt.plot(x, y4)
plt.title("y=4x")

plt.suptitle("그래프 그리기 연습")
plt.tight_layout()

plt.show()
"""

#-------------------------------------------
'''
# 막대그래프
categories = ['A', 'B', 'C']
values = [10, 15, 7]

# plt.bar(categories,values, width=0.3, color=["r", "g", "b"], alpha = 0.5, edgecolor='red', linewidth = 5)
bars = plt.bar(categories, values, color='orange', label='막대 샘플')
plt.legend()

plt.xticks(categories, ['2023', '2024', '2025']) # 눈금을 원하는대로 바꿀 수 있다.

for bar in bars: # 약간 공식처럼 쓰인다. 바에 글씨넣기
    plt.text(bar.get_x() + bar.get_width() / 2, # x좌표 (막대의 중심)
             bar.get_height() + 0.6,            # y좌표
             str(bar.get_height()),
                 ha='center', va='top', color='black')

plt.title("막대그래프 연습", pad=20)
plt.xlabel("카테고리")
plt.ylabel("수치")
plt.show()
'''
#-----------------------------------------------------------
# 수평막대

categories = ['A', 'B', 'C']
values = [10, 15, 7]

bars = plt.barh(categories, values, color='skyblue', edgecolor='red')

for bar in bars:
    plt.text(bar.get_width() + 0.5,# x좌표
             bar.get_y() + bar.get_height()/2,
             str(bar.get_width()),
             ha = 'right', va = 'center', color = 'green') # y좌표(막대중심)

plt.title('막대그래프 연습', pad=20)
plt.xlabel('카테고리')
plt.ylabel('수치')
plt.show()