# 클래스~
"""
# 클래스 정의
class Car: 
    model = "" # 멤버변수
    cc = 0  

    # 함수추가
    def info(self): # 항상 self라고 적어주면 된다. 첫번째 매개변수는. 이후로는 다른걸로해도됨.
        print(f"모델명 : {self.model} 배기량 : {self.cc}cc") # 이것때문에 self를 적은 것. 클래스 안에서 자기자신을 불러와서 접근한다.


# 사용
car1 = Car() # 인스턴스 생성
car1.model = "싼타페" # 멤버변수에 접근하기 위해서 인스턴스.멤버변수 이렇게 해준다.
car1.cc = 2000  # 점연산자 사용

# print(f"모델명 : {car1.model}")
# print(f"배기량 : {car1.cc}cc")

car1.info() # info라는 메서드가 생긴 것. 우리가 만든 메서드

# 생성자가 존재할 때.

class Car:
    # 생성할 때 값을 넣었다. 해서 생성자
    def __init__(self, model, cc): # 싼타페를 받을 model을 선언
        self.model = model # 클래스 안에서 싼타페를 받을 수 있는 것. 
        self.cc = cc
    def __str__(self):
        return f"모델명 : {self.model} 배기량 : {self.cc}" 
    def info(self): # 메서드를 생성해줬다.
        print(f"모델명 : {self.model} 배기량 : {self.cc}")

car1 = Car("싼타페", 2000) # print()도 되고, print("산타페")도 되는 것과 같다.
car2 = Car("BMW", 5000)
car1.info() # 메서드를 생성해준건 이렇게 출력
print(car2) # __str__은 이런식으로 출력
print("========== 승용차 리스트 ==========")
#객체이기 떄문에 리스트를 만들 수 있다.
cars = [
    Car("소나타", 2000),
    Car("쏘렌토", 3000),
    Car("아반떼", 1999)
]
# print(cars[0])
for car in cars:
    print(car)


# 실습1. 사칙연산 클래스 만들기

class Calc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def plus(self, num):
        print(f"{self.num1} + {self.num2} + {num} = {self.num1 + self.num2 + num}")
    def sub(self):
        print(f"{self.num1} - {self.num2} = {self.num1 - self.num2}")
    def mul(self):
        print(f"{self.num1} * {self.num2} = {self.num1 * self.num2}")
    def div(self):
        if self.num2 == 0:
            return "분모가 0이될 수 없습니다."
        # 꿀팁. 오류조건은 항상 위쪽에 만들어주는게 좋다.
        # if에 걸려서 return된다면 어차피 밑에는 처리 안해도되니까.
        # else도 안써도 된다.
        num = self.num1 / self.num2
        print(f"{self.num1} / {self.num2} = {num:.2f}")

numbers = Calc(5,3)
numbers.plus(5) # 이렇게도 쓸 수 있다.
numbers.sub()
numbers.mul()
numbers.div()

# 클래스 변수와 인스턴스 변수

class Dog:
    kind = "진돗개" # 클래스 변수.
    def __init__(self, name):
        self.name = name # 인스턴스 변수

# 인스턴스 변수 접근
dog1 = Dog("백구")
dog2 = Dog("초코")
print(dog1.name)
print(dog2.name)

# 클래스 변수 접근
print(dog1.kind) # 이렇게는 안쓴다. 인스턴스변수인지 클래스점수인지 잘 안보이니까.
print(Dog.kind) # 클래스이름.변수명 이렇게 접근하는게 일반적이다.



class Example:
    shared = "공유변수" # 클래스변수

    def __init__(self, name):
        self.name = name # 인스턴스 변수

e1 = Example("A")
e2 = Example("B")
Example.shared = "변경된 공유 변수"
print(e1.shared)
print(e2.shared)

e1.name = "C"
print(e1.name)
print(e2.name)


# 인스턴스변수들을 공유되지 않는다.
# 클래스변수만 공유된다.


# 사번 자동 발급

class Employee:
    serial_num = 1000 # 클래스변수
# 클래스변수는 사용할 떄 self안써도 된다.
    def __init__(self, name):
        Employee.serial_num += 1 # 생성자가 만들어질 때마다 1씩 증가
        self.id = Employee.serial_num # 사번
        self.name = name
    
    def __str__(self):
        return f"사번 : {self.id}, 이름 : {self.name}"

e1 = Employee("홍길동")

e2 = Employee("임꺽정")
print(e1)
print(e2)

employees = [Employee("이몽룡"), Employee("심청이"), Employee("토끼"), Employee("거북이")]
for employee in employees:
    print(employee)

# 인스턴스변수로 한다면 1001로 나오고 끝날것.
# 클래스는 그 클래스가 변하면서 
# 인스턴스는 그 안에서 끝


# 실습2. Supermarket 클래스

class Supermarket:

    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer     

    def print_location(self):
        print(f"위치 : {self.location}")
    
    def change_category(self, new_product):
        self.product = new_product
    
    
    def show_list(self):
        print(f"상품 : {self.product}")
    
    def enter_customer(self):
        self.customer += 1
    
    def show_info(self):
        print(f"위치 : {self.location}, 이름 : {self.name}, 상품 : {self.product}, 고객수 : {self.customer}")
    

super = Supermarket("마포구 염리동", "마켓온", "음료", 12 )

super.print_location()
super.show_list()
super.show_info()


# 정보은닉
class person:
    def __init__(self):
        self._name = ""
        self._age = 0

    # 이름을 설정
    def setname(self, name):
        self._name = name
    def getname(self): # set이 있다면 get이 꼭 따라온다고 생각.
        return self._name
    
    #나이를 출력
    def setage(self, age):
        self._age = age
    
    def getage(self):
        return self._age

p1 = person()
p1.setname("홍길동") # 정보은닉을 위해서 set으로 정보 설정
print(p1.getname()) # get으로 정보 가져오기.
"""

# 실습3. 건강상태 클래스 만들기
# 정보 은닉을 이용해서.

class Health():
    def __init__(self, name):
        self._name = name
        self._hp = 100
        
    def setname(self,name):
        self._name = name

    def getname(self):
        return self._name
    
    def sethp(self, hp):
        self._hp = hp



    def gethp(self):
        return self._hp
    
    def hp_sys(self, workout, drink):
        self._hp += workout
        self._hp -= drink

        if self._hp >= 100:
            self._hp = 100

        print(f"{workout}시간 운동하다.") # 오류 가능성 있으니, 따로 def설정하는것이 좋다.
        print(f"술을 {drink}잔 마시다.")

    def status(self,user):
        print(f"{user.getname()} - hp : {user.gethp()}")
        print("=====================================")                

p1 = Health("나몸짱")

p1.sethp(100)
p1.hp_sys(5,2)
p1.status(p1)

p2 = Health("나약해")

p2.sethp(55)
p2.hp_sys(1,15)
p2.status(p2)


