# 리스트 기초
number = [1, 2, 3, "Hello", "Python"]
print(number[3])
print(number[0])

text = "Hello, Python"
text = list(text) # 리스트가 아닌것을 리스트로 만들어줌
print(text)

#리스트 슬라이싱
shop = ["반팔", "청바지", "이어폰", ["무선키보드", "기계식키보드"]]
print(shop[:2]) # 반팔, 청바지 / 0 <= shop < 2
print(shop[3]) 
print(shop[-2]) # 이어폰

# 리스트 값 수정
shop[0] = "긴팔"
print(shop)

# 리스트 지우기
del shop[1]
print(shop)
del shop[2:] # 슬라이싱도 가능
print(shop)

# 리스트 연산
a = [1,2,3]
b = ["안녕하세요", "반갑습니다."]
print(a+b) # 리스트 더하기 중요..
print(b * 2)

# 정렬함수 sorted / 숫자, 문자 다 가능
num = [3, 1, 5, 2]
num_asc = sorted(num)
print(num_asc)
num_desc = sorted(num, reverse = True)
print(num_desc)
print(num) # 원본은 바뀌지 않는다!!!!!!!

# 정렬 메서드 .sort()
num.sort() 
print(num)
# num.sort(reverse = True) 하면 내림차순
korean = ["강", "이", "박", "최", "김"]
korean.sort(reverse = True)
print(korean)

# 역순정렬 메서드 .reverse()
# 리스트 내용을 그냥 뒤집어버림
# 오름차순, 내림차순 아님.. 그냥 뒤집어버림
alphabet = ['b', 'c', 'a', 'd']
alphabet.reverse()
print(alphabet)

# 위치찾기 메서드
print(alphabet.index('c')) # 2

# 추가/삭제 메서드 *가장중요
a = ['a', 'b', 'c', "안녕", "hi"]
a.append("Good")
print(a)
a.pop()
print(a)
a.pop(2)
print(a)
a.remove('안녕')
print(a)
a.insert(2, "잘가")
print(a)
a.clear()
print(a)

# count 메서드 / 해당하는 글자가 몇개가 있냐~
x = ['q', 'w', 'e','r','w']
print(x.count('w'))

# 실습. 리스트 연습문제
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

print(rainbow[2]) # 문제를 잘 확인하자......... 2번째가 아닌 2번 인덱스였다.
rainbow_asc = sorted(rainbow)
print(rainbow_asc)
rainbow.append("green")
print(rainbow)
del rainbow[3:7]
print(rainbow)

# 이차원 리스트
# 3x3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[2][0]) # 7

# 요소 추가
matrix[1] = matrix[1] + [99]
print(matrix)

# 행 추가
matrix = matrix + [[10,11,12]] # 이차원 배열이기 때문에 대괄호로 감싸준다. 안그러면 
print(matrix)

# 요소수정
matrix[0][0] = 100
matrix[1][1] = 5000
print(matrix)

# 행 삭제
del matrix[2]
print(matrix)
del matrix[1][1]
print(matrix)

# 행 개수
rows = len(matrix)
print(rows)

# 열 개수
cols = len(matrix[0])
print(cols)



# 이차원 메서드
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 요소 추가
matrix[0].append(10)
print(matrix)

# 행 추가
matrix.append([10,11,12])
print(matrix)

matrix[1].insert(1, 100)
print(matrix)

matrix.insert(2, ["안녕하세요", "반갑습니다","어서오세요"])
print(matrix)

# extend() 메서드
matrix[0].extend([11,12])
print(matrix) # 첫번째 이차원 리스트에 11과 12가 추가된다.



# 튜플
# 추가, 삭제, 수정만 아니면 왠만해선 다 된다.

t1 = (1,) # 튜플로 하나만 넣고싶다면 이렇게 넣어야 한다.
# t1 = (1) 이건 튜플이 아니라 그냥 1이다.
t2 = (1, 2, 3, 4, 5)
t3 = 1,2,3
t4 = ('a', 'b', 'c', ('안녕', '감사'))
print(t1[0])
print(t2.count(3))
print(t3.index(2))
print(t4[3][0])
print(len(t4))
print('c'in t4) # in 연산자 이게 여기 속해있느냐? True or False

# Set
s1 = {1,1,1,1,1,1,2}
print(s1)
s2 = ['안녕', '잘가', 'HI', '안녕']
print(set(s2))


'''
오늘 배운 것..
자료형 - 변수 자료형, 자료형 형 변환

출력 - 문자열 출력, 문자열 연산, 여러줄 문자열 출력
따옴표 출력

포매팅

문자열 관련 함수 - 
문자열 인덱싱, 슬라이싱
메서드들...
문자열 판별

-----이후 ppt-----

리스트 - 슬라이싱 값수정, 삭제,, 등등
리스트 함수 - 정렬, 등등 메서드를 활용, 추가 삭제 메서드가 가장 중요
이차원 리스트 , 어펜드, 익스펜드 로우 컬럼, 메서드
튜플, 셋,, 

'''