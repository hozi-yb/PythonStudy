# 실습6. 함수 종합 프로그래밍 (어제거 해보기)

# 초기 날씨 데이터

# 전역변수이지만 리스트가 요소가 추가제거가 되는 이유. 리스트는 완전 재할당이 아닌이상,
# append, pop 등 요소를 추가제거하면 같은 메모리값을 참조하기때문에 값을 변경할 수 있다.
# 초반에 메모리관련 이야기를 했던것과 관련이 있다.

weather_data = [                                                                 # 전역변수 리스트가 어떻게 값을 추가/제거할 수 있을까?
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0]
    # 1. 함수를 생각하지 말고 일단 프로그램 짜기.
]


# 평균기온 계산 함수
# weather_data는 전역변수이지만 명시적으로 매개변수로 넣어주자. 매개변수로 안적어도 작동은 하지만 깔끔한 코드를 위해.
def avg_temperatures(weather_data):
    city = input("도시 이름을 입력하세요.")
    # 도시 추출
    temp = filter(lambda x: x[1] == city, weather_data)
    # 기온 추출
    temper = list(map(lambda x: x[2], temp))
    if not temper:
        return city, None
    else:
        return city, sum(temper) / len(temper)


        # avg =
        # print(f"{city}의 평균기온은 : {avg:.2f}℃")
""" for문을 이용한 방법
total = 0
count = 0
for data in weather_data:
    total += data[i]
    count += 1
return city, total / count
"""


# 최고/최저 기온 찾기함수
def max_min_temperatures(weather_data):
    city = input("도시 이름을 입력하세요.")
    temp = filter(lambda x: x[1] == city, weather_data)  # 도시 추출
    temper = list(map(lambda x: x[2], temp))  # 기온 추출
    if not temper:
        return city, None, None
    else:
        return city, max(temper), min(temper)


""" 리스트 내포를 이용한 방식
temper = [data[2] for data in weather_data if data[1] == city] 
"""

# 강수량 분석 함수


def total_rain_day(weather_data):
    city = input("도시 이름을 입력하세요.")
    temp = filter(lambda x: x[1] == city, weather_data)  # 도시 추출
    rain = list(map(lambda x: x[3], temp))  # 강수량 추출
    rainy_day = list(filter(lambda x: x > 0, rain))  # 비가 온 날
    total_rain = sum(rain)
    return city, total_rain, rainy_day

# 날씨 데이터 추가함수


def add_weather(weather_data):
    date = input("날짜를 입력하세요 (YYYY-MM-DD): ")
    city = input("도시를 입력하세요: ")
    temp = input("평균 기온을 입력하세요 (°C): ")
    rain = float(input("강수량을 입력하세요 (mm): "))
    weather_data.append([date, city, temp, rain])
    return city

# 전체 데이터 출력함수


def all_data(weather_data):
    print("\n현재 저장된 날씨 데이터 :")
    for data in weather_data:
        print(f"날짜 : {data[0]}, 도시 : {data[1]}, 평균 기온 : {
              data[2]}℃ , 강수량 : {data[3]} ")


def main_program():
    while True:
        print("\n[날씨 데이터 분석 프로그램]")
        print("1. 평균 기온 계산")
        print("2. 최고/최저 기온 찾기")
        print("3. 강수량 분석")
        print("4. 날씨데이터 추가")
        print("5. 전체 데이터 출력")
        print("6. 종료")
        choice = input("원하는 기능의 번호를 입력하세요.")

        if choice == "1":
            city, avg_result = avg_temperatures()  # 도시의 평균기온 계산 함수
            if avg_result is None:
                print(f"{city}의 정보가 존재하지 않습니다.")
            else:
                print(f"{city}의 평균기온은 : {avg_result:.2f}℃")

        elif choice == "2":
            city, max_value, min_value = max_min_temperatures()
            if max_value is None:
                print(f"{city}의 정보가 존재하지 않습니다.")
            else:
                print(f"{city}의 최고기온 : {max_value}℃ , 최저기온 : {min_value}℃")

        elif choice == "3":
            city, total_rain, rainy_day = total_rain_day()

            print(f"{city}의 총 강수량 : {total_rain}mm")
            print(f"{city}의 비가 온 날 : {len(rainy_day)}일")

        elif choice == "4":
            city = add_weather(weather_data)
            print(f"{city}의 날씨데이터가 추가되었습니다.")

        elif choice == "5":
            all_data()  # 전체 데이터 출력 함수

        elif choice == "6":
            print("프로그램을 종료합니다.")
            break


main_program()
