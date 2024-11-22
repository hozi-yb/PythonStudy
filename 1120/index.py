#print 함수
'''
print("안녕하세요")
print("Hello", "Python")
print("Hello", "Python", sep='')
print("안녕하세요", end='~ ')
print("저는 임유빈입니다.")
print(111111) 
'''
# singer = input("좋아하는 가수는? ") # 여기서 입력을 기다린다.
# print("좋아하는 가수는 ", singer, "입니다.")

# 한 줄 주석에 사용한다. 코드뒤에서도 사용가능


x = 10 # x라는 변수에 값 10을 할당한 것
print("before x", x, id(x))
y, z = 3.14, "안녕하세요"
print("y", y)
print("z", z)
x = "반갑습니다." # x에 값을 재할당하여 이후에는 바뀐값으로 나온다.
print("after x", x, id(x))

a = [1,2,3]
print("before x",a, id(a))
a.append(4)
print("after a",a,id(a))


# import keyword

# print(keyword.kwlist)


x= (100-2)/7+(9*3)
print("x",x)

# 연산자
num = 5
print("num",num)
num += 5 # += 5 ===> num = num + 5
print("+=", num)
num -= 2 # num = num - 2
print("-=", num)
num *= 6 # num = num * 6
print("*=", num)
num /= 2 # num = num / 2
print("/=", num) # 나누는 순간 소숫점이 들어간다.
num //= 5 # num = num // 5
print("//=",num)
num %= 3 # num = num % 3
print("%=",num)
num = 4
num **= 4 # num = num ** 4
print("**=",num)

#비교연산자
num1 = 10
num2 = 20
num3 = "10"
print(num1 > num2) # False
print(num1 < num2) # True
print(num1 == num3) # False
print(num1 >= 10) # True
print(num2 <= 19) #False
print(num1 != num3) # True

#논리연산자
a = 2 > 1 #True
b = 1 > 2 #False
c = 1 == 1 # True
d = 3 >= 4 # False

print(a and c)
print(a and d)

print(b or c) 
print(b or d)

print(not a)
print(not d) 

# in 연산자
# 안에 있는지 찾는 것~
a = "hello world"
print("H" in a) # False
print("h"in a) # True

print("a" not in a) # True
print("w"not in a) # False

# 연산자 연습. 실습

num = 4
a = num % 2 == 0

print("True면 짝수, False면 홀수:", a)