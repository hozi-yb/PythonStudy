"""
# while 문

i=0
while i < 3:
    print("반복문", i+1)
    i += 1
print("종료")


#합계 구하기
num = 1
total = 0
while num <= 10:
    total += num # tatal = total + num
    num += 1 # num = num + 1
print(f"1부터 10까지의 합은 {total}입니다.")

# 입력값 받기 무한반복
user_input = "" # "" = 빈문자
while user_input != "종료":
    user_input = input("원하는 값을 입력하세요. 종료하려면 '종료'를 입력하세요 :")
    print(f"입력한 값 : {user_input}")
print("프로그램이 종료되었습니다.")


# break
while True:
    dinner = input("오늘 저녁 뭐먹지?")
    if dinner == '제육':
        break
    print(f"다시 골라보세요. {dinner} 이거 말고")
print("저녁 메뉴 완료")


count = 0

while True:
    print(count + 1, end=" ")
    count += 1
    if count == 10:
        break


# continue

count = 0

while count < 10:
    count += 1
    if count % 2 ==0:
        continue # 짝수는 건너뜀
    print(count, end = " ")
"""

# 실습. while문 사용하기
""" 내가 한 것.
while True:
    user_input = input("양수를 입력하세요. ('종료'입력시 종료) : ")
    num_sum = 0
    num_up = 0
    if user_input.isdigit():
        if int(user_input) == 0:
            continue
        elif int(user_input) < 0:
            print("양수만 입력하세요.")
        elif int(user_input) > 0:
            while num_up <= int(user_input):

                num_sum += num_up
                num_up += 1
            
            print(f"1부터 {user_input}까지의 합은 {num_sum}입니다.")            
    elif user_input == "종료":
        print("프로그램을 종료합니다.")
        break
    else:
        print("양수만 입력하세요.")
"""
"""리더님이 작성한 프로그램
while True:
    # 먼저 종료조건과 돌아가야하는 조건을 작성한다.
    user_input = input("양수를 입력하세요. ('종료'입력시 프로그램 종료) : ")
    if user_input == "종료":
        print("프로그램을 종료합니다.")
        break
    if not user_input.isdigit():
        print("양수를 입력하세요.")
        continue
    
    # 이제 숫자로 바꾼다.
    number = int(user_input)
    if number == 0:
        continue

    total = 0
    num = 0
    while num <= number:
        total += num
        num += 1
    print(f"1부터 {number}까지의 합은 {total}입니다.")
"""
"""for 문
for i in range(10):
    print(i, end = " ")

print() # 줄바꿈 \n 안해도됨.
for i in range(3,9):
    print(i, end = " ")

print()
for i in range(1, 100, 12):
    print(i, end = " ")
"""
# 이름 작성 팁!
# 리스트는 주로 복수로 쓴다. 내용물이 여러개니까.
# 후에 하나씩 나오는 걸 단수로 표현
fruits = ["사과", "바나나", "포도", "체리"]
for fruit in fruits:
    print(fruit, end="|")

print()
# 합계구하기
numbers = [1,2,3,4,5,6,7,8,9,10]
total = 0
for num in numbers:
    total += num # 리스트에 있는 값을 쓰기에 증가조건이 필요 없다.
print(f"합계는 {total}입니다.")

print()

# 조건문 사용
numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    if num % 2 != 0:
        print(num, end = "")

# 테스트