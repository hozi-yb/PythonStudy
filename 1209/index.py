import pandas as pd
# pandas 공식홈페이지
# kaggle에서 판다스 연습할 수 있다.
# 분석할 수 있는 데이터도 주고

'''
# 결측값
data = {
    "Name":["홍길동", "임꺽정", "성춘향"],
    "Age":[25,None,20],
    "City":["서울", "부산", None]    
}

df = pd.DataFrame(data)
print(df)
# print(df.isnull()) # 값이 null값인지 찾을 때. True라고 되어있어야 null값이다.
# print(df.isnull().sum()) # 결측값 갯수를 알려준다. 
# print(df.info()) # 어디 결측값이 있다는걸 알 수 있다.
# df_drop = df.dropna() # 결측값이 있는 행 삭제
# df_drop_column = df.drop(axis = 1) # 결측값이 있는 열 삭제, axis 기본값은 행. 1로 설정하면 열 
# df_fill = df.fillna(0) #결측값을 다 채운다. 포맷을 따라감
# df_fill_f = df.fillna(method="ffill") # 이전값으로 채워줌
# df_fill_b = df.fillna(method="bfill") # 다음값으로 채움. 다음값이 없으면 그냥 none

print(df_fill_b)
#isin() 메서드
s = pd.Series(["홍길동", "임꺽정", "성춘향", "이몽룡"])
result = s.isin(["홍길동", "이몽룡"])

print(result) # True, False, False, True


data = {
    "Name":["홍길동", "임꺽정", "성춘향", "이몽룡"],
    "Age":[25,30,20,32]
}
df = pd.DataFrame(data)
result = df.isin(["성춘향", "홍길동", 20]) # TrueFalse 찾기 / 찾고싶은 값을 리스트로 쭉 넣어주면 된다.
result = df[df['Name'].isin(["성춘향", "홍길동", 20])] # True 값만 필터링 한다. Name에서만
print(result)


s = pd.Series([1,2,None])
result = s.isin([None, 2]) # 결측값은 무시한다. s에 None이 있지만 False로 뜨는걸 볼 수 있다.
print(result)

# 빈도수values_counts()

# s = pd.Series(['사과', '바나나', '사과', '오렌지', '바나나', '사과'])
# print(s.value_counts())

df = pd.DataFrame({
    "과일" : ['사과', '바나나', '사과', '오렌지', None, '사과'],
    "수량" : [1, 2, 3, 4, 5, 6]
})
# print(df['과일'].value_counts()) # 딕셔너리에서의 values_counts / 옵션을 넣을 수 있다.
# print(df['과일'].value_counts(normalize=True)) # 빈도를 비율(%)
# print(df['과일'].value_counts(ascending=True)) # 오름차순
# print(df['과일'].value_counts(dropna=False)) # 결측값도 나오게

s = pd.Series([1,2,3,4,5])
result = s.agg(['sum' 'mean', 'max'])
print(result) # 총합, 평균값, 최대값을 출력

df = pd.DataFrame({
    'A' : [1,2,3],
    'B' : [10,11,12]
})
print(df.agg(['sum', 'mean'])) # 행렬로 나온다.
print(df.agg({'A' : 'sum', 'B' : 'mean'})) # agg 많이 쓴다.


s1 = pd.Series([10,20,30])
s2 = pd.Series([5,15,25])

# print(s1 + s2)
# print(s1 - s2)
# print(s1 * s2)
# print(s1 / s2)
# print(s1 / 2) # 정수를 넣어도 된다.
# print(s1 > 15) # 비교연산도 가능

# 통계연산
print(s1.sum())
print(s1.mean()) # 평균
print(s1.max())
print(s1.min())
print(s1.std()) # 표준편자
print(s1.var()) # 분산
print(s1.median()) # 중앙값을 알려준다.

# 통계지표
print(s1.describe()) # 통계지표 요약

# 그룹
data = {
    'group' : ['A', 'A','B', 'B', 'C'],
    'value' : [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# result = df.groupby('group')['value'].sum() # 그룹에서 겹치는 애들끼리 밸류에 있는걸 더해라!
result = df.groupby('group')['value'].agg(['sum', 'mean', 'max']) # 한꺼번에 출력시킬 수 있어서 많이 쓸 것.
print(result)

data = {
    'group' : ['A', 'A','B', 'B', 'C'],
    'value1' : [10, 20, 30, 40, 50],
    'value2' : [5, 15, 25, 35, 45]
}
df = pd.DataFrame(data)
result = df.groupby('group').agg({
    'value1' : 'sum',
    'value2' : ['mean', 'sum']
})

result = df.groupby('group').filter(lambda x : x['value1'].sum() > 30) # 람다식을 쓸 수 있다....일단은
print(result)
'''

