import cv2
import matplotlib.pyplot as plt

cat = cv2.imread("./1213/img.png")
gray_cat = cv2.cvtColor(cat, cv2.COLOR_BGR2GRAY)

# 이진화처리 
_, binary = cv2.threshold(gray_cat, 127, 255, cv2.THRESH_BINARY) # 앞에있는 값은 안쓴다.

# 컨투어 감지 얜 뒤에있는걸 안씀
contours , _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # tree방식으로 모든 컨투어를 계층적으로 탐지, 뒤에있는건 직선만 검출한다는 뜻.

# 컨투어 원본에 그리기
result_img = cat.copy()
cv2.drawContours(result_img, contours, -1, (0, 255, 0), 2) # 숫자들 순서별 의미 : 모든 컨투어, 색상, 선 두께

plt.imshow(cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB))
plt.title("contour")
plt.axis('off')
plt.show()