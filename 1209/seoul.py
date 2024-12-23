import pandas as pd

file_name = r"C:\Users\jerry\Documents\workspace\python\1209\서울특별시_공원 내 운동기구 설치 현황_20201231.csv"
df = pd.read_csv(file_name, encoding="cp949")
# 판다스 데이터를 문자열 형식으로 변환 to_string()

# 데이터 확인
# print(df.info())
# print(df.isnull().sum())

# 컬럼 공백제거
df.columns = df.columns.str.strip()
df['구분'] = df['구분'].str.strip()
df['운동기구 기종명'] = df['운동기구 기종명'].str.strip()

# 공원별 총 운동기구 설치 수
print("공원별 총 운동기구 설치 수")
print(df.groupby('구분')['운동기구 수량'].sum().head())
# df.to_csv('C:\\Users\\jerry\\Documents\\workspace\\python\\1209\\공원별 총 운동기구 설치 수.txt')

# with open("./1209/park_counts.txt", 'w', encoding='utf-8') as file:
#     file.write("공원 별 총 운동기구 설치 수\n")
#     file.write(df.to_string())

print()
# 운동기구 종류별 설치 개수
print("운동기구 종류별 설치 개수")
equipments_counts = df['운동기구 기종명'].value_counts()
print(equipments_counts)
df.to_csv('C:\\Users\\jerry\\Documents\\workspace\\python\\1209\\운동기구 종류별 설치 개수.txt')
print()
# 관리기관별 총 운동기구 설치 수
print("관리기관별 총 운동기구 설치 수")
print(df.groupby('관리기관')['운동기구 수량'].sum().head())
# df.to_csv('C:\\Users\\jerry\\Documents\\workspace\\python\\1209\\관리기관별 총 운동기구 설치 수.txt')
print()
# 특정 공원 데이터 필터링
print("특정 공원 데이터 필터링")
filter_park = df[df['구분'] == '남산공원(회현)']
print(filter_park.head())
# filter_park.to_csv('C:\\Users\\jerry\\Documents\\workspace\\python\\1209\\특정 공원 데이터 필터링.txt')
print()
# 특정 운동기구 종류 데이터 필터링
print("특정 운동기구 종류 데이터 필터링")
filter_machine = df[df['운동기구 기종명'] == ('스텝사이클')]
print(filter_machine.head())
# filter_machine.to_csv('C:\\Users\\jerry\\Documents\\workspace\\python\\1209\\특정 운동기구 종류 데이터 필터링.txt')
print()
# 운동기구 수량 기준 내림차순 정렬
print("운동기구 수량 별")
desc = df.sort_values(by='운동기구 수량', ascending=[False])
print(desc.head())
# asc.to_csv('C:\\Users\\jerry\\Documents\\workspace\\python\\1209\\운동기구 수량 기준 내림차순 정렬.txt')