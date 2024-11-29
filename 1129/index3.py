# 파일입출력

# 파일쓰기 w 는 삭제하고 추가하는것.
'''
with open("test.txt","w",encoding="utf=8") as file:
    file.write("안녕하세요\n")
    file.write("파이썬쓰기연습\n")
    
# 파일추가
with open("test.txt","a",encoding="utf-8") as file:
    file.write("내용추가\n")
    file.write("323") # int자료형으로 데이터를 넣을 수 없다. 무조건 문자열로 들어간다.

lines = ["첫번째\n", "두번째\n", "세번째\n"]

with open("test2.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

# 파일 쓰기
with open("user.txt", "w", encoding = "utf-8") as file:
    while True:
        line = input("파일에 넣을 문자열 입력(종료하려면 '종료'입력): ")
        if line == "종료":
            print("입력을 종료합니다.")
            break
        file.write(line + "\n")

# 파일읽기
with open("user.txt", "r", encoding= "utf8") as file:
    print(file.read())

with open("user.txt", "r", encoding= "utf-8") as file:
    print(file.readline()) # 다음줄에 공백이 생기고 한줄씩 가져온다.
    print(file.readline())

with open("user.txt", "r", encoding="utf-8") as file:
    print(file.readlines()) # 각 줄을 읽고 리스트로 반환

with open("user.txt", "r", encoding="utf-8") as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()
'''

with open("user.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for idx, value in enumerate(lines):
        print(f"{idx}인덱스값은 {value.strip()}입니다.")