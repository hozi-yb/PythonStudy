import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

path = "C:\\Windows\\Fonts\\NanumBarunGothicUltraLight.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)

"""
# 이미지 읽기
image = cv2.imread("./1213/test_image.jpg")

# opencv = BGR -> matplotlib = RGB

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)



# cv2를 이용한 방법
cv2.imshow("title", image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt를 이용한 방법. 앞으론 이렇게.
plt.imshow(image_rgb)
plt.axis('off')  #x, y 축을 없애주는것.
plt.show()

plt.figure(figsize=(10, 7))
# 원본
plt.subplot(2, 2, 1)
plt.imshow(image_rgb)
plt.title("원본")
plt.axis('off')  #x, y 축을 없애주는것.
"""

"""블러는 노이즈제거에 효과적
이미지에서 특정 영역의 픽셀 값을 주변 픽셀들의 평균값으로 대체하여 노이즈를 줄이는 방법
"""


"""
#------------------------------------------------------------블러링
# 평균블러
blurred = cv2.blur(image_rgb, (5, 5)) # 보통 3, 3을 많이씀

plt.subplot(2, 2, 2)
plt.imshow(blurred)
plt.title('평균블러')
plt.axis('off')


# 가우시안블러
gaussian = cv2.GaussianBlur(image_rgb, (5, 5), 0)

plt.subplot(2, 2, 3)
plt.imshow(gaussian)
plt.title("가우시안블러")
plt.axis('off')


# 미디언 블러
median = cv2.medianBlur(image_rgb, 5)

plt.subplot(2, 2, 4)
plt.imshow(median)
plt.title("미디언블러")
plt.axis('off')
"""
#----------------------------------------------------샤프닝 kernel
"""

# 샤프닝 커널
kernel = np.array([[0, -1, 0],
                   [-1, 7, -1], # 중심값을 크게할수록 엣지가 강조된다
                   [0, -1, 0]])

# 필터 적용
sharped = cv2.filter2D(image_rgb, -1, kernel)


# 찐하게 엣지 강조
plt.subplot(2, 2, 2)
plt.imshow(sharped)
plt.title("엣지강조")
plt.axis('off')
"""
#-------------------------------------------------------엣지검출 Sobel

"""
#sobel 그레이 스케일로 해야한다. 

# 이미지를 그레이로 받기
image_grey = cv2.imread("./1213/test_image.jpg", cv2.IMREAD_GRAYSCALE)


sobel_x = cv2.Sobel(image_grey, cv2.CV_64F, 1, 0, ksize=3) # x 방향의 미분 ( 1, 0 )
soble_y = cv2.Sobel(image_grey, cv2.CV_64F, 0, 1, ksize=3) # y 방향 미분 ( 0, 1 )
#CV_64F : 64비트의 부동소수점.. opencv에서 사용하는 상수? 우리는 정밀해야해서 많은수를 사용해야한다.
#CV_8U : 8비트(-127 ~ 128) U - unsigned(음수를 제거하고 다 양수로 바꿔버리는거 0 ~ 255) 너무 적다.

#sobel 결과 결합
sobel_combined = cv2.magnitude(sobel_x, soble_y) # magnitude : 벡터의 절대값 계산

# 원본
plt.subplot(2, 2, 1)
plt.imshow(image_grey, cmap='grey')
plt.title("원본")
plt.axis('off')

# sobel 엣지만 검출해줌.
plt.subplot(2, 2, 2)
plt.imshow(sobel_combined, cmap='grey')
plt.title("Sobel")
plt.axis('off')


#laplacian

cat_img = cv2.imread("./1213/img.png", cv2.IMREAD_GRAYSCALE)
laplacian_cat = cv2.Laplacian(cat_img, cv2.CV_64F)

laplacian = cv2.Laplacian(image_grey,cv2.CV_64F)

plt.subplot(2, 2, 3)
plt.imshow(laplacian_cat, cmap='grey')
plt.title('laplacian')
plt.axis('off')

# canny

edges = cv2. Canny(image_grey, 100, 500) # 100 : 최소값, 200 : 최대값 ( 변동가능 ) 

plt.subplot(2, 2, 4)
plt.imshow(edges, cmap='grey')
plt.title('canny edge')
plt.axis('off')
"""

#------------------컨투어                          ## 안쓰는 변수 왜 있는지??

"""
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이진화처리 
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) # 앞에있는 값은 안쓴다.

# 컨투어 감지 얜 뒤에있는걸 안씀
contours , _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # tree방식으로 모든 컨투어를 계층적으로 탐지, 뒤에있는건 직선만 검출한다는 뜻.

# 컨투어 원본에 그리기
result_img = image.copy()
cv2.drawContours(result_img, contours, -1, (0, 255, 0), 2) # 숫자들 순서별 의미 : 모든 컨투어, 색상, 선 두께

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB))
plt.title("컨투어그리기")
plt.axis('off')
"""

#-----------------------컨투어 계산
"""
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours , _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
result_img = image.copy()

for contour in contours:
    # 면적 계산
    # print("면적 : ", cv2.contourArea(contour)) # 컨투어들의 면적을 출력해준다.

    # # 중심점 계산
    # M = cv2.moments(contour)
    # if M['m00'] != 0: # 중심점계산 (m00 = 면적)
    #     cx = int(M['m10'] / M['m00']) # circle x
    #     cy = int(M['m01'] / M['m00']) # y 중심

    #     # 중심점 표시
    #     cv2.circle(result_img, (cx, cy), 5, (0, 0, 0), -1) # 반지름, 색상, 선(-1일 때 내부 채우기)
    # else:
    #     print("컨투어 면적이 0")

    # 둘레 계산
    print("둘레 : ", cv2.arcLength(contour, True)) # 폐곡선 여부 ( 곡선도 계산되어서 나온다. ~ )
    
    cv2.drawContours(result_img, [contour], -1, (0, 255, 0), 2)

plt.imshow(cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB))
plt.show()
"""

#-------------------------------------- 웹캠 연결
"""
cap = cv2.VideoCapture(0)

codec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./1213/output.avi', codec, 20.0, (640, 480))

plt.ion() # 인터렉티드 모드 : 코드를 실행하면서 창을 표시

while cap.isOpened():
    ret, frame = cap.read()

    if not ret: # ret : True, False 값, 프레임을 읽었는지 못읽었는지
        break

    out.write(frame)
    # cv2.imshow("video", frame)

    # 원본
    original = frame.copy()

    # 가우시안 블러 노이즈 제거
    gaussian = cv2.GaussianBlur(frame, (5, 5), 0)

    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.title("원본")
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(cv2.cvtColor(gaussian, cv2.COLOR_BGR2RGB))
    plt.title("가우시안")
    plt.axis('off')   

    plt.pause(0.001) # 1밀리초동안 
    plt.clf() # 현재 플롯창에 띄어진것을 초기화 그림을 아예 메모리에서 지워버림

    # 'q' 키로 종료
    key = cv2.waitKey(1) # 키 입력 대기 (1ms)
    if key == ord('q'):
        break

cap.release()
# out.release()

cv2.destroyAllWindows()
plt.close()
"""

# 실습.

cap = cv2.VideoCapture(0) # 0번 = 내 웹캠

# # 예외처리
# if not cap.isOpened():
#     print("영상이 열리지 않습니다.")
#     exit()

#     # exit() 와 break의 차이

#---------------------------------------------------------------------------
    # 샤프닝 커널
kernel = np.array([[0, -1, 0],
                   [-1, 5.3, -1],
                   [0, -1, 0]])
# 필터 적용


plt.ion()

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
    _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    # 컨투어 감지
    contours , _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 컨투어 원본에 그리기
    result_frame = frame.copy()
    cv2.drawContours(result_frame, contours, -1, (0, 255, 0), 2)


    sharped = cv2.filter2D(result_frame, -1, kernel)

    # 원본
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.title("원본")
    plt.axis('off')

    # 컨투어
    plt.subplot(2, 2, 2)
    plt.imshow(cv2.cvtColor(result_frame, cv2.COLOR_BGR2RGB))
    plt.title("컨투어 감지")
    plt.axis('off')

    # kernel
    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(sharped, cv2.COLOR_BGR2RGB))
    plt.title("윤각선 강조")
    plt.axis('off')

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