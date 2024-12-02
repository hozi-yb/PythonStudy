'''

# if문 연습

age = 21

if age < 20:  # false
    print("미성년자 입니다.")
else:
    print("미성년자가 아닙니다.")

print(f"나이는 {age}입니다.")
age = 16

print()

if age < 20:  # True
    print("미성년자 입니다.")

print(f"나이는 {age}입니다.")





# if ~ else 실습

pw = input("비밀번호를 입력하세요: ")

if pw == "abc1234":
    print("비밀번호가 맞습니다.")
else:
    print("비밀번호가 틀렸습니다.")

# if ~ else 실습 2
num = int(input("숫자를 입력하세요: "))

if num % 2 == 0:
   print("짝수입니다.")
else:
    print("홀수입니다.")



# elif 문
age = int(input("나이를 입력하세요."))

if age < 20:
    print("10대입니다.")
elif age < 30:
    print("20대입니다.")
elif age < 40:
    print("30대입니다.")
elif age < 50:
    print("40대입니다.")
else:
    print("50대이상입니다.")
'''

'''

# elif 실습

grade = int(input("점수를 입력하세요 : "))

if grade >= 90:
    print("학점 : A")
elif grade >= 80:
    print("학점 : B")
elif grade >= 70:
    print("학점 : C")
elif grade >= 60:
    print("학점 : D")
else:
    print("학점 : F")

# 실습 중첩 조건문

age = int(input("나이를 숫자로 입력해주세요 : "))
pay = input("결제방법을 입력해주세요 (현금 또는 카드) : ")

if pay == "카드":
    if age >= 1:
        if age < 8:
            print(f"{age}세의 {pay}요금은 무료입니다.")
        elif age < 14:
            print(f"{age}세의 {pay}요금은 450원입니다.")
        elif age < 20:
            print(f"{age}세의 {pay}요금은 720원입니다.")
        elif age < 75:
            print(f"{age}세의 {pay}요금은 1200원입니다.")
        else:
            print(f"{age}세의 {pay}요금은 무료입니다.")
    else:
        print("나이를 잘못입력했습니다.")
elif pay == "현금":
    if age >= 1:
        if age < 8:
            print(f"{age}세의 {pay}요금은 무료입니다.")
        elif age < 14:
            print(f"{age}세의 {pay}요금은 450원입니다.")
        elif age < 20:
            print(f"{age}세의 {pay}요금은 1000원입니다.")
        elif age < 75:
            print(f"{age}세의 {pay}요금은 1300원입니다.")
        else:
            print(f"{age}세의 {pay}요금은 무료입니다.")
    else:
        print("나이를 잘못입력했습니다.")
'''
'''


age = input("나이를 숫자로 입력하세요. : ")

if age.isdigit() and int(age) > 0:
    method = input("결제방법을 입력해주세요(카드 또는 현금) : ")
    if method == "카드":
        age = int(age)
        if age < 8:
            price = "무료"
        elif age < 14:
            print = "450원"
        elif age < 20:
            price = "720원"
        elif age < 75:
            price = "1200원"
        else:
            price = "무료"

    elif method == "현금":
        age = int(age)
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
        print("결제방식을 카드나 현금으로 입력하시오.")

    if price:
        print(f"{age}세의 {method}요금은 {price}입니다.")

else:
    print("나이를 잘못입력했습니다.")



# 삼항연산자 / 파이썬 좀 아는구나 / 간단한 조건식에서 사용
age = int(input("나이를 입력하세요 : "))
# message = "20대입니다." if age < 30 and age >19 else" 20대가 아닙니다."
message = "20대입니다." if age < 30 and age >19 else"30대입니다." if age<40 and age >=30 else "20대도 30대도 아닙니다."
print(message)
# 삼항연산자에서 중첩도 가능하다. 좀 복잡해짐
# 참일 때 앞에 있는 게 출력된다.
# 거짓일 때마다 뒤로 가는 것.
# 2, 3개 이상가면 복잡해지기 때문에 그 이하로 사용하는게 좋다.
'''
# 조건문에서 in 연산자 활용
fruits = input("과일을 한글로 입력하세요. : ")
if fruits in ['사과', '바나나', '복숭아']:
    print(f"{fruits}은(는) 과일에 포함되어 있습니다.")
else:
    print("존재하지 않는 과일입니다.")


'''
# 실습. in 연산자 활용

cal = {
    'apple' : 95,
    'banana' : 105,
    'cherry' : 50
}
fruit = input("과일을 영문으로 입력하세요. : ")

if fruit in cal: # get메서드를 사용해도 된다.
    print(f"{fruit}의 칼로리는 {cal[fruit]}kcal입니다.")
else:
    print(f"{fruit}는 포함되지 않은 과일입니다.")
    
'''
