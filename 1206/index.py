import pandas as pd

"""
# 판다스를 리스트형식으로 생성한 것.
data = [10, 20,30,40]
# series = pd.Series(data)
series = pd.Series(data, index=["a", "b", "c", "d"])
print(series)

# 딕셔너리형식으로 생성
data = {
    "a" : 10,
    "b" : True,
    "c" : 3.14,
    "d" : "python"
}
series = pd.Series(data, name = "딕셔너리") # 문자와 같이 섞여 있으면 object값으로 온다. 이름도 설정해줄 수 있다.
# print(series)
# print(series.index)
# print(series.values)
# print(series.shape)

data = ('민지', '여', False)
member = pd.Series(data, index=['이름', '성별', '결혼여부'])
print(member)
print(member['이름'])
print(member[['성별', '결혼여부']])

data = [10, 20, 30, 40, 50]
series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print(series['a']) # print(series[0])으로 해도 되긴 하는데, 그렇게 하지 말라고 뜸
print(series[series > 20])
series['c'] = 100
print(series)

# 실습1 시리즈 만들기
data = ['4 cups', '1 cup', '2 large', '1 can']
food = pd.Series(data, index = ['밀가루', '우유', '계란', '참치캔'], name = 'Dinner')
print(food)

# 데이터 프레임
data = {
    'Name' : ["홍길동", '임꺽정', '성춘향'],
    'Age' : [25, 30, 27],
    'City' : ['서울', '부산', '인천']

}

df = pd.DataFrame(data)
print(df)

index = ['2020', '2021', '2022', '2023', '2024', '2025']

yeonghee = pd.Series([140,150,160,170,180,190], index=index)
cheolsu = pd.Series([200,210,220,230,240,250], index=index)

result = pd.DataFrame({
    '영희' : yeonghee,
    '철수' : cheolsu
})
# print(result)
# print(result.head()) # head는 상위 5개만 / 많은 데이터 중에서 데이터가 잘 들어가는지 확인하는 용도로 쓰인다.
# print(result.tail()) # 하위 5개
# print(result.shape)
# print(result.info()) # non-null 데이터가 잘 들어갔는지 확인. 
# print(result.columns)
# print(result.values)
# print(result.index)
# print(result.dtypes)
# print(result['철수'])
# print(result[['철수']]) # 키값까지 같이 오게하려면 2차원으로 부르면 된다.
data = {
    'Name' : ["홍길동", '임꺽정', '성춘향'],
    'Age' : [25, 30, 27],
    'City' : ['서울', '부산', '인천']
}

df = pd.DataFrame(data, index=['a', 'b', 'c'])
print(df)
# print(df.loc['b']) # b에 관한 값
# print(df.loc['b', 'Age']) # 30
# print(df.loc['a' : 'c', 'Name' : 'Age'])
# print(df.loc[df['Age'] >= 30])
# print(df.loc[:, ['Name']]) # : 콜론이 전부라는 뜻
# print(df.loc['a',:]) # a행에 있는 모든걸 가져와라

# 숫자로 접근
# print(df.iloc[1])
# print(df.iloc[1,1])
# print(df.iloc[0:2, 0:2]) # 끝값 포함 안됨
# print(df.iloc[[0, 2], [1, 2]]) # 열 -> 0, 2 행 -> 1, 2
# print(df.iloc[:,0])
print(df.iloc[0,:]) # a의 전체
data = {
    'Name' : ["홍길동", '임꺽정', '성춘향'],
    'Age' : [25, 30, 27],
    'City' : ['서울', '부산', '인천']
}
df = pd.DataFrame(data)

# +++++++++++++++++++++++값 수정++++++++++++++++++++++++++++

# 행추가
new_data = {'Name':'이몽룡', 'Age':31, 'City':'포항'}
result = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True) # 이그노어인덱스를 해야지 인덱스값을 따라간다.
print(result)
# 열추가
result["직업"] = ["엔지니어", "개발자", '디자이너', "기획자"]
print(result)
# 요소값수정
result.at[1, 'City'] = '천안'
result.loc[result['Name'] == '임꺽정', "Age"] = 19
# print(result)

# 칼럼변경
result.rename(columns={'Name':'이름', 'Age':'나이'}, inplace=True) # 원본데이터를 바꾸고 싶을 때 inplace
print(result)

# 데이터정렬 (내림차순)
result.sort_values(by='나이', inplace=True, ascending=False)

# 칼럼삭제
result.drop(columns=['City'], inplace=True)

print(result)
"""

# 실습 2. 데이터프레임 만들기

data = {
    '이름': ['홍길동', '임꺽정', '성춘향'],
    '수학' : [85, 88, 95],
    '영어' : [90, 76, 89],
    '과학' : [95, 89, 84]
}

df = pd.DataFrame(data)

df.rename(columns={'수학':'Math'}, inplace=True )

new_data = {'이름':'이몽룡', 'Math': 88, '영어': 85, '과학': 90}
df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

df.at[1,'영어'] = 80

df['Total'] = df['Math'] + df['영어'] + df['과학']
print(df)
