
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("./1216/test_image.jpg")

'''
HSV -> 색상범위설정 -> 마스크생성 -> 원본이미지에 마스크적용

빨간색을 검출해서 그 부위를 빼고 마스크를 생성(까맣게)
그리고 원본에 덮어씌워서 빨간색만 보이게 함.
'''

# BGR -> HSV 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 색상범위 설정 (빨간색)
lower = np.array([0, 120, 70])
upper = np.array([10, 255, 255])

# 마스크 생성
mask = cv2.inRange(hsv_image, lower, upper) #lower과 upper사이에 마스크생성

# 원본이미지에 마스크 적용
result = cv2.bitwise_and(image, image, mask=mask)

plt.subplot(1, 3, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1,3,2)
plt.title('mask')
plt.imshow(mask, cmap='gray')
plt.axis('off')

plt.subplot(1,3,3)
plt.title('result')
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
"""

###--------------------실시간 피부색 검출
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 크기 변경
    frame = cv2.resize(frame, (640, 480))

    # HSV로 변경
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 피부색 범위 (HSV)
    lower = np.array([0, 20, 70])
    upper = np.array([20, 255, 255])

    # 마스크
    mask = cv2.inRange(hsv, lower, upper)

    # 노이즈 제거(모폴로지 연산)
    mask = cv2.erode(mask, None, iterations=3) # (입력이미지, 커널, 몇번반복할건지)
    mask = cv2.dilate(mask, None, iterations=3) # (입력이미지, 커널, 몇번반복할건지)

    # 컨투어 찾기
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 윤곽선 그리기
    for con in contours:
        area = cv2.contourArea(con)

        cv2.drawContours(frame, [con], -1, (0, 255, 0), 2)
    
    cv2.imshow("skin", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""


####-------------------얼굴인식
"""
import cv2

# haar cascade 불러오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("웹캠안됨")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # 그레이스케일로 변환
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴탐지
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor= 1.1, minNeighbors=5, minSize=(30, 30))

    # 탐지된 얼굴에 사각형 그리기
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+y, y+h), (255, 0, 0), 2)

    cv2.imshow('face', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""

###__-------------얼굴, 눈 인식
"""
import cv2

# 얼굴
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# 눈
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("웹캠이 인식되지 않았씁니다.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+y, y+h), (255, 0, 0), 2)

        # 눈탐지
        eyes = eye_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=15, minSize=(15, 15))

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    
    cv2.imshow('eyes', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""

#---------------YOLO 객체 탐지
"""
import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt') # YOLO모델 v8, n : nano버전

image = cv2.imread("./1216/test.jpg") 
# image = ./1216/test.jpg 이렇게 해도 된다.

# 객체 탐지
results = model.predict(source=image, save = False, save_txt = False, conf = 0.5)

# 결과 시각화
frame = results[0].plot() # plot() : 탐지된 객체를 시각화한 이미지를 반환해줌.

cv2.imshow('YOLO', frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""

#------------ocr
"""

import cv2
import pytesseract

# 테서렉트 경로 설정
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'

image = cv2.imread("./1216/receipt.png")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray_image, lang='kor')

print("추출된 이미지", text)
"""


#------------ocr 보완

"""
import cv2
import pytesseract

# 테서렉트 경로 설정
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'

image = cv2.imread("./1216/plate1.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gaussian = cv2.GaussianBlur(gray_image, (5, 5), 0)
# roi = gaussian[70:120, 50:245] # image
roi = gaussian[140:300, 90:530] # image1

# 이진화
# _, binary_img = cv2.threshold(roi, 60, 255, cv2.THRESH_BINARY)

# adaptiveThreshold() : 조명에 대응이 쉽다.
# 적응형 이진화
binary_img = cv2.adaptiveThreshold(roi, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 5)


cv2.imshow("binary", binary_img)

text = pytesseract.image_to_string(binary_img, lang='kor')

print("추출된 이미지", text)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""


## 실습문제

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("./1216/apple.jpg")

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 색상범위 설정 (초록색)
lower = np.array([40, 60, 60])
upper = np.array([85, 255, 255]) 

mask = cv2.inRange(hsv_image, lower, upper)

mask = cv2.erode(mask, None, iterations=5) 
mask = cv2.dilate(mask, None, iterations=2)

contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour_image = image.copy()
count = 0
# 윤곽선 그리기
for contour in contours:
    area = cv2.contourArea(contour)

    if area > 2000: # 작은 노이즈 제거
        # 윤곽선의 경계 사각형을 가져오기
        x, y, w, h = cv2.boundingRect(contour) # 객체를 감싸는 가장 작은 축에 정렬된 사각형
        cv2.rectangle(contour_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        count += 1

cv2.imshow("apple", contour_image)
print(f"검출된 초록색 물체 개수 : {count}")

cv2.waitKey(0)
cv2.destroyAllWindows()
