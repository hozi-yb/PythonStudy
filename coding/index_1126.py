# 실습4. 함수만들기
# 방법1
def count(num):
    lists = [i for i in range(1, 31) if i % num == 0]
    counts = len(lists)
    return lists, counts


num = 4
lists, counts = count(num)
print(f"{num}의 배수: {lists}")
print(f"{num}의 개수: {counts}")

# 방법2 - 중첩함수


def count(num):
    # 중첩함수 - 이 함수 내에서만 사용이 가능
    def check(x):
        return x % num == 0

    lists = list(filter(check, range(1, 31)))
    return lists, len(lists)


num = 5
lists, counts = count(num)
print(f"{num}의 배수: {lists}")
print(f"{num}의 개수: {counts}")

# 재귀함수


def sos(i):
    print("help me!", i)
    if i == 1:
        return ""
    else:
        return sos(i-1)


sos(10)

# 팩토리얼


def factorial(n):
    print("n의 값", n)
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))

# 실습5. 피보나치 수열


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(6))

# 실습4. 함수만들기 - 람다식


def count(num):
    lists = list(filter(lambda x: x % num == 0, range(1, 31)))
    return lists, len(lists)


num = 5
lists, counts = count(num)
print(f"{num}의 배수: {lists}")
print(f"{num}의 개수: {counts}")

# 실습6. hint:도시필터링, 숫자추출
city = "서울"
x = [
    ["서울", 10],
    ["서울", 20],
    ["부산", 30]
]
a = filter(lambda x: x[0] == city, x)
print(list(map(lambda x: x[1], a)))
