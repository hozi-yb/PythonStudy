"""
어제질문
print 안에 sorted는 되는데
x.sort()는 안되는 이유가
sorted는 원본데이터가 안바껴서
.sort()는 원본데이터가 바뀌기 때문에 적용이 안된다.

원본데이터에 영향이 되지 않는 메서드는 print안에 사용이 가능하나
영향이 가는것은 print안에 안된다.
print만 그런가
"""
"""
# 메서드
s1 = {1, 2, 3, 3, 4}
print(s1)
s1.add(5) # 추가
print(s1)

s1.update([6,7,8,9,10])
print(s1)

s1.remove(3)
print(s1)

s1.discard(9)
print(s1)

# remove에서 없는 값을 치면 키가 없다고 뜨는데
# discard는 없는 값을 쳐도 아무 이상이 없다.

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
# 합집합
s3 = s1 | s2 
s3 =s1.union(s2) # 합집합
print(s3)

#교집합
s3 = s1 & s2 
s3 = s1.intersection(s2)
print(s3)

# 차집합 누굴 기준으로 뺄 것인지가 중요하다.
s3 = s1 - s2
s3 = s1.difference(s2)
print(s3)

# 딕셔너리 *중요
# 딕셔너리 생성 ( 빈 딕셔너리 생성 )
dict1 = {}  # 빈 딕셔너리 생성
dict1 = dict()

dict1 = {# 키값은 변수처럼 사용하기에 이름을 잘 정하자
    "name" : "홍길동",
    "age" : 20,
    "city" : "서울",
    "hobby": ["런닝", "등산", "헬스"] # 리스트도 가능
} # 이 형태를 가장 추천, 다른 언어도 이런 형태를 많이 사용하기 때문

print(dict1)
dict2 = dict(name = "홍길동", age = 20) # 이런 형태도 가능

print(dict1["name"]) # 키값을 이용해서 불러올 수 있다.
print(dict1['hobby'][2]) # 리스트 값에 접근하는 방법
print(dict1["hobby"])

# 값 수정
dict1["age"] = 21
print(dict1["age"])

# 값 추가
dict1["birthday"] = 20001011
print(dict1)

# 리스트에 값 추가
dict1['hobby'] = ["런닝", "등산", "헬스", "캠핑"]
print(dict1['hobby'])

# 값 삭제
del dict1["city"]
print(dict1)

# 딕셔너리 메서드

fruits = {
    'apple' : '사과',
    'banana' : '바나나'
}
# get 값을 가져오는 것
print(fruits.get('apple'))
print(fruits.get('peach', '복숭아'))

# 여러 요소 추가
fruits.update({
    'grape' : '포도',
    'melon' : '멜론'
})
print(fruits)

print(fruits.keys()) # 키값만 가져옴
print(fruits.values()) # 밸류값만 가져옴
print(fruits.items()) # 튜플값으로 키와 밸류값을 가져옴

fruits.clear() # fruits값 전체 삭제
"""
# 실습. 성적관리

students = {
    "Alice" : 85,
    "Bob" : 90,
    "charlie" : 95
}
students["David"] = 80 # students.update({ "David" : 80 }) 로도 가능하다.
students["Alice"] = 88
del students["Bob"]

print(students)

# 내장함수 sum()
numbers = [1,2,3,4,5]
print(sum(numbers))

scores = {
    '국어' : 90,
    '영어' : 80,
    '수학' : 85
}
print(sum(scores.values())) # 딕셔너리 안에서 밸류값을 꺼내서 썸 가능

# zip() 내장함수
names = ['Alice', 'Bob', 'Charlie', 'David']
scores = [85,90,88,95]
zipped = list(zip(names, scores)) # 리스트 함수로 리스트화 시켜줘야 나온다.
print(zipped) # 튜플형태로 반환, 변하지 말고 데이터를 쓰라고 