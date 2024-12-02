# 상속
# 부모클래스가 생성자가 없을 때.
"""
class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")
    
    def move(self):
        print("동물이 움직입니다.")

#자식클래스
class Cat(Animal): # 상속받을 클래스 명
    def meow(self):
        print("야옹!")

cat = Cat() # 자식클래스로 선언
cat.speak() # 부모클래스에 있는걸로 인스턴스 선언할 수 있따. 이어진다.
cat.move()
cat.meow()

# 부모클래스의 생성자가 존재할 때.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}가 소리를 냅니다.")
    
    def move(self):
        print(f"{self.name}가 움직입니다.")
    
class Cat(Animal): # 부모가 생성자가 있으니 자식도 생성자를 넣어줘야한다.
    def __init__(self, name, sound = "야옹"): # 부모가 name을 받았으니, 자식도 받아야된다,. 관례상 부모에 있는 변수가 먼저 온 뒤 자식에서 쓸 변수를 쓴다. , 매개변수 이름은 꼭 맞출필요가 없지만, 관례상 같이..
        super().__init__(name) # 부모에 있는 name을 호출한 것. 호출이 중요
        self.sound = sound

    def meow(self):
        print(f"{self.name}가 {self.sound} 소리를 냅니다..") # 가져온거니 self.name으로 불러옴

cat = Cat("장화")
cat.speak() # 기본값이 있으니 안넣어도 되지만, 값을 넣으면 값을 넣은대로 나온다.
cat.move()
cat.meow()

# 다중상속
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Wheels:
    def __init__(self, count):
        self.count = count

class Car(Engine, Wheels):
    def __init__(self, horsepower, count):
         Engine.__init__(self, horsepower) # 직접 부모(Engine)에 접근해서 값을 가져온것. 그래서 self도 써준다.
         Wheels.__init__(self, count)
# 여기도 인잇받을 때 같은 이름으로 안해도 되지만.
# 사용할 땐 self.부모에서 생성한 이름으로 해줘야된다.
    def info(self):
        print(f"이 자동차는 {self.horsepower}마력과 {self.count}개의 바퀴를 가지고 있다.")

car = Car(100, 4)
car.info()
print(Car.mro()) #이걸로 읽어들이는 순서를 출력해ㅐ줄 수 있다.

# 다중상속의 문제점.
# 변수명이 겹칠 수 있다.
# 그래서 Engine_count Wheels_count와 같은 방식으로 변수를 생성해주면 된다.


# 오버라이딩

class Parent:
    def greet(self):
        print("안녕하세요. 부모 클래스")
    

class Child(Parent):
    def greet(self): # 부모클래스와 똑같이 재생성
        super().greet() # 부모클래스에 있는 greet() 호출
        print("안녕하세요. 자식 클래스") # 자식에서 재정의

p = Parent()
c = Child()
p.greet()
print()
c.greet()


# 실습. 상속과 오버라이딩

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # 재고 업데이트 메서드
    def update_quantity(self, amount):
        self.quantity += amount
        print(f"{self.name} 재고가 {amount}만큼 {'증가' if amount > 0 else '감소'}했습니다. 현재 재고: {self.quantity}")

    # 상품 정보 출력 메서드
    def display_info(self):
        print(f"상품명: {self.name}")
        print(f"가격: {self.price}원")
        print(f"재고: {self.quantity}개")

class Electronic(Product):
    def __init__(self, name, price, quantity, warranty_period = 12):
        super().__init__(name, price, quantity)
        self.warranty_period = warranty_period  

    def extend_warranty(self, months):
        self.warranty_period += months
        print(f"보증기간이 {months}개월 만큼 연장되었습니다.")
        print(f"보증기간 : {self.warranty_period}개월")
    
    def display_info(self):
        super().display_info()
        print(f"보증기간 : {self.warranty_period}개월")

class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date
    
    def is_expired(self, current_date):
        
        if current_date < self.expiration_date: # 문자열 비교연산이 가능하다.
            print("유통기한이 지나지 않았습니다.")
        else:
            print("유통기한이 지났습니다.")

    def display_info(self):
        super().display_info()
        print(f"유통기한 : {self.expiration_date}")


e1 = Electronic("스마트 TV", 1500000, 5, 10)
e1.display_info()
e1.extend_warranty(3)
e1.display_info()

f1 = Food("사과", 3000, 50, "2024-12-27")
f1.is_expired("2024-11-28")
f1.display_info()


#추상화
# 추상클래스
from abc import ABC, abstractmethod # abc라는 곳에서 ABC를 가져왔구나라고 이해.

class PaymentSystem(ABC): # ABC를 꼭 상속받아야 추상메서드가 되는것.

    # 추상메서드가 된 것.
    # 어떤것을 할 지 정의
    @abstractmethod 
    def authenticate(self): # 이 밑에 코드를 작성하면 안된다.
        pass # 인증은 꼭 들어가야하고,
     
    @abstractmethod
    def process_payment(self, amount):
        pass # 결제가 진행되어야한다고, 자식메서드한테 알려주는 것.

    def payment_info(self, amount):
        print(f"{amount}원 결제가 완료되었습니다.")

class KakaoPay(PaymentSystem): # 상속받아서 오버라이딩 한 것.
    # 여기서 구현

    def authenticate(self): # 여기서 구현을 안하면 오류남.
        print("카카오페이 인증완료되었습니다.")

    def process_payment(self, amount):
        print(f"카카오페이로 {amount}원을 결제합니다.")

pay = 50000
kakao = KakaoPay()
kakao.authenticate()
kakao.process_payment(pay)
kakao.payment_info(pay)

"""