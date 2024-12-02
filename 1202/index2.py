# 예외처리

# try:
#     x = int(input("숫자를 입력하세요"))
#     result = 10/x
# except ZeroDivisionError as e: # e : 변수 / error
#     print("예외메세지", e)
# except ValueError as e:
#     print("예외메세지", e)
# else:
#     print(f"result : {result}")
# finally: # 무조건 나오는 것
#     print("프로그램이 종료됩니다.")

# try:
#     x = int(input("숫자를 입력하세요"))
#     result = 10/x
# except (ZeroDivisionError, ValueError) as e: # e : 변수 / error
#     print("예외메세지", e)
# else:
#     print(f"result : {result}")
# finally: # 무조건 나오는 것
#     print("프로그램이 종료됩니다.")

# 강제오류
# raise Exception("예외처리") # 강제로 오류를 발생시켜서 막는것.

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a/b

try: # try는 무조건 except를 써줘야한다.
    result = divide(10, 2)
except ZeroDivisionError as e:
    print("예외발생!", e)
else:
    with open("result.txt", "w", encoding="utf-8") as file:
        file.write(f"결과 : {result}")