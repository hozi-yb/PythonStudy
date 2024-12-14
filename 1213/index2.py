import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

path = "C:\\Windows\\Fonts\\NanumBarunGothicUltraLight.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)

cap = cv2.VideoCapture(0) # 0번 = 내 웹캠

# # 예외처리
if not cap.isOpened():
    print("영상이 열리지 않습니다.")
    exit()

    # exit() 와 break의 차이



#---------------------------------------------------------------------------
    # 샤프닝 커널
kernel = np.array([[0, -1, 0],
                   [-1, 5.3, -1],
                   [0, -1, 0]])
# 필터 적용


plt.ion()

fig, axes = plt.subplots(2, 2, figsize=(8, 6))

while True:
    ret, frame = cap.read()

    if not ret:
        print("프레임을 열 수 없습니다.")
        break

    # 원본
    original = frame.copy()
#---------------------------------------------------------------------------
    # 블러
    # 가우시안블러
    gaussian = cv2.GaussianBlur(frame, (5, 5), 0)


    
#---------------------------------------------------------------------------
    # 그레이 스케일
    gray = cv2.cvtColor(gaussian, cv2.COLOR_BGR2GRAY)

    # 이진화처리 
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # 컨투어 감지
    contours , _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 컨투어 원본에 그리기
    result_frame = frame.copy()
    cv2.drawContours(result_frame, contours, -1, (0, 255, 0), 2)


    sharped = cv2.filter2D(result_frame, -1, kernel)

    # 원본
    axes[0,0].imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    axes[0,0].set_title("원본")
    axes[0,0].axis('off')

    # 컨투어
    axes[0,1].imshow(cv2.cvtColor(result_frame, cv2.COLOR_BGR2RGB))
    axes[0,1].set_title("컨투어 감지")
    axes[0,1].axis('off')

    # 샤프닝 필터
    axes[1,0].imshow(cv2.cvtColor(sharped, cv2.COLOR_BGR2RGB))
    axes[1,0].set_title("윤각선 강조")
    axes[1,0].axis('off')

    plt.pause(0.001)
    plt.clf() 

    key = cv2.waitKey(1) 
    if key == ord('q'):    
        break

# 리소스 해제
cap.release()
cv2.destroyAllWindows()

plt.ioff() # 인터렉티브 모드 종료
plt.close()