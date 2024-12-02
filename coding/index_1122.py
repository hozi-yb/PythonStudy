"""
# 실습. 리스트 연습문제
rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
print(rainbow[2])
sorted_rainbow = sorted(rainbow)
print(sorted_rainbow)
rainbow.append("pink")
print(rainbow)
del rainbow[3:7]
print(rainbow)

# 실습. 성적관리
students = {}
students['Alice'] = 85
students['Bob'] = 90
students['Charlie'] = 95
students['David'] = 80
students['Alice'] = 88
del students['Bob']
# print(students)

# 내장함수
sum()
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))

scores = {"국어": 90, "영어": 80, "수학": 85}
print(sum(scores.values()))


# zip()
names = ['Alice', 'Bob', 'Charlie', 'David']
scores = [85, 90, 88, 95]
zipped = list(zip(names, scores))
print(zipped)

"""
# 실습. elif
score = int(input("점수를 입려하세요: "))
if score >= 90:
    print("학점: A")
elif score >= 80:
    print("학점: B")
elif score >= 70:
    print("학점: C")
elif score >= 60:
    print("학점: D")
else:
    print("학점: F")

# 실습. 중첩 조건문
age = int(input("나이를 숫자로 입력하세요: "))

if age > 0:
    method = input("결제방법을 입력해주세요(카드 또는 현금): ")
    if method == "카드":
        if age < 8:
            price = "무료"
        elif age < 14:
            price = "450원"
        elif age < 20:
            price = "720원"
        elif age < 75:
            price = "1200원"
        else:
            price = "무료"
    elif method == "현금":
        if age < 8:
            price = "무료"
        elif age < 14:
            price = "450원"
        elif age < 20:
            price = "1000원"
        elif age < 75:
            price = "1300원"
        else:
            price = "무료"
    else:
        price = None
        print("결제방법을 카드나 현금으로 입력하세요")

    if price:
        print(f"{age}세의 {method}요금은 {price}입니다.")


else:
    print("나이는 음수가 될 수 없습니다.")


# 삼항연산자
age = int(input("나이를 입력하세요"))
# message = "20대입니다." if age < 30 and age >= 20 else "20대가 아닙니다."
message = "20대입니다." if age < 30 and age >= 20 else "30대입니다" if age < 40 and age >= 30 else "20대도 30대도 아닙니다."
print(message)

# 실습. in연산자 활용
fruits = {
    "apple": 95,
    "banana": 105,
    "cherry": 50
}

fruit = input("과일을 영문으로 입력하세요: ")

if fruit in fruits:
    print(f"{fruit}의 칼로리는 {fruits[fruit]}Kcal입니다")
else:
    print(f"{fruit}는 정보가 존재하지 않습니다.")

    # while문
i = 0
while i < 3:
    print("반복문", i)
    i += 1
print('종료')

# 합계구하기
num = 1
total = 0
while num <= 10:
    total += num  # total = total + num
    num += 1    # num = num + 1
print(f"1부터 10까지의 합은 {total}입니다.")

# 입력값 받기
user_input = ""
while user_input != "종료":
    user_input = input("원하는 값을 입력하세요. 종료하려면 '종료'를 입력하세요: ")
    print(f"입력한 값: {user_input}")
print("프로그램이 종료되었습니다.")

# break
while True:
    dinner = input("오늘 저녁 뭐먹지?")
    if dinner == "제육":
        break
    print(f"다시 골라보세요")
print("저녁 메뉴 완료")

count = 0
while True:
    print(count, end=" ")
    count += 1
    if count == 10:
        break

# continue
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count, end=" ")

# 실습. while문 사용하기
while True:
    user_input = input("양수를 입력하세요.('종료'입력시 프로그램 종료): ")
    if user_input == "종료":
        print("프로그램을 종료합니다")
        break

    if not user_input.isdigit():
        print("양수를 입력하세요")
        continue

    number = int(user_input)
    if number == 0:
        continue

    total = 0
    num = 1
    while num <= number:
        total += num
        num += 1
    print(f"1부터 {number}까지의 합은 {total}입니다.")
