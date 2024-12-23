import cv2
"""
# image = cv2.imread("./1212/img.png")
image = cv2.imread("./1212/img.png",cv2.IMREAD_GRAYSCALE)
image_color = cv2.imread("./1212/img.png")


print(image.shape)
print(image_color.shape)

cv2.imshow("Gray Image",image)
cv2.imshow("Color Image",image_color)

# cv2.imwrite("./1212/output-image.jpg", image)


cv2.waitKey(0) # 2초후에 창 닫힘 # 키가 들어올때까지 기다림 설정한 값까지, 설정한 값이 지나면 알아서 꺼짐 (0은 무한대기)
cv2.destroyAllWindows() # 모든 창 닫음  이 두개를 같이 써야 좋은코드다. 윈도우를 끄라고 직접적으로 지시.



# key = cv2.waitKey(0)
# if key == ord('q'): # q값이 들어왔을때만 처리한다. / q가 아닌값이 들어오면 안나온다.
    # print(chr(key))
"""

#------------------------------------
# image_color = cv2.imread("./1212/img.png")

# gray = cv2.cvtColor(image_color, cv2.COLOR_RGB2GRAY)
# hsv = cv2.cvtColor(image_color, cv2.COLOR_RGB2HSV)

# resized = cv2.resize(image_color, (400,300))
# scale = 0.5
# resized = cv2.resize(image_color, None, fx=scale, fy=scale )

# roi = image_color[ 0:600,200:900] # [y,x]이다.
# 관심영역설정, 잘 하려면 이미지의 값을 잘 알아야한다., 아예 원본 이미지를 바꾼다. / 그래서 .copy()를 해줘서 복사본으로 사용해줘야 원본데이터를 사용하지 않는다,.
# cv2.imshow("Color Image",image_color)
# cv2.imshow("Color Image",roi)

#--------------------------------------------------- x값이랑 y값 찾기
"""
def mouse_click(e, x, y, flag, param):
    if e == cv2.EVENT_LBUTTONDOWN:
        print(f"마우스 위치 : x = {x}, y = {y}")


image_color = cv2.imread("./1212/img.png")

cv2.imshow("image", image_color)

# 마우스 콜백함수
cv2.setMouseCallback("image", mouse_click) # 우리는 3개만 받지만, 5개의 변수를 받아야한다.

"""

#---------------------------------------------------roi만 표시
#글로벌변수
"""
start = None
end = None

def mouse_select(e, x, y, flag, param):
    global start, end
    if e == cv2.EVENT_LBUTTONDOWN:  # 클릭을 누르는 상태
        start = (x, y)
    elif e == cv2.EVENT_LBUTTONUP:  # 클릭을 뗀 상태
        end = (x, y)
        # 영역표시
        roi = image_color[start[1]:end[1], start[0]:end[0]]
        cv2.imshow("select", roi)


image_color = cv2.imread("./1212/img.png")
cv2.imshow("image", image_color)

# 마우스 콜백함수
cv2.setMouseCallback("image", mouse_select)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""

#------------------------------------------------------
# import numpy as np
# image_color = cv2.imread("./1212/img.png")

# # 중심좌표
# (h, w) = image_color.shape[:2]
# center = (w // 2, h // 2)

""" 회전
matrix = cv2.getRotationMatrix2D(center, 180, 1.0) # 배열은 float값
rotated = cv2.warpAffine(image_color, matrix, (w, h))
"""
""" 이동
matrix = np.float32([ [1, 0, 100], [0, 1, 50] ])
move = cv2.warpAffine(image_color, matrix, (w, h))
"""



"""
cv2.imshow("image", move)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

# 실습. 이미지처리

image_color = cv2.imread("./1212/img.png")
# 1. 크기 출력
print(image_color.shape)

# 2. 이미지 흑백 변환
grey = cv2.cvtColor(image_color, cv2.COLOR_RGB2GRAY)


# 3. 이미지 50% 축소

scale = 0.5
resized = cv2.resize(image_color, None, fx=scale, fy=scale)
cv2.imshow("image", grey)
cv2.imshow("image", resized)

# 4. 이미지 90도 회전 후 저장
(h, w) = image_color.shape[:2]
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(image_color, matrix, (w, h))

cv2.imwrite("./1212/rotated-image.jpg", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
