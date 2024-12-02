# 실습. 건강상태 클래스 만들기
class Health:
    def __init__(self, name):
        self._hp = 100
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def set_hp(self, value):
        self._hp = value
        if self._hp >= 100:
            self._hp = 100
        else:
            self._hp = value

    def get_hp(self):
        return self._hp

    def exersise(self, hour):
        self.set_hp(self._hp + hour)
        print(f"{hour}시간 운동하다")

    def drink(self, cups):
        self.set_hp(self._hp - cups)
        print(f"술을 {cups}잔 마셨다")

    def info(self):
        print(f"{self.get_name()} - hp: {self.get_hp()}")


p1 = Health("나몸짱")
# p1.set_hp(70)
p1.exersise(5)
p1.drink(2)
p1.info()

p2 = Health("나약해")
p2.set_hp(20)
p2.exersise(1)
p2.drink(10)
p2.info()


# getter, setter 데코레이터
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # getter
    @property
    def name(self):
        return self.__name

    # setter
    @name.setter
    def name(self, value):
        self.__name = value

    # getter
    @property
    def age(self):
        return self.__age

    # setter
    @age.setter
    def age(self, value):
        self.__age = value


p1 = Person("홍길동", 20)
print(p1.name)
print(p1.age)

p1.name = "이몽룡"
p1.age = 25
print(p1.name)
print(p1.age)

# 실습. 상속과 오버라이딩


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # 재고 업데이트 메서드
    def update_quantity(self, amount):
        self.quantity += amount
        print(f"{self.name} 재고가 {amount}만큼 {'증가' if amount >
              0 else '감소'}했습니다. 현재 재고: {self.quantity}")

    # 상품 정보 출력 메서드
    def display_info(self):
        print(f"상품명: {self.name}")
        print(f"가격: {self.price}원")
        print(f"재고: {self.quantity}개")

# 자식 클래스


class Electronic(Product):
    def __init__(self, name, price, quantity, warranty_period=12):
        super().__init__(name, price, quantity)
        self.warranty_period = warranty_period

    # 보증기간 연장
    def extend_warranty(self, months):
        self.warranty_period += months
        print(f"보증기간이 {months}개월 연장. 현재 보증기간{self.warranty_period}개월")

    # 오버라이딩
    def display_info(self):
        super().display_info()
        print(f"보증기간: {self.warranty_period}개월")


class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    # 유통기한 확인
    def is_expired(self, current_date):
        if current_date > self.expiration_date:
            print(f"{self.name}은/는 유통기한이 지났습니다.")
        else:
            print(f"{self.name}은/는 유통기한이 지나지 않았습니다")

    def display_info(self):
        super().display_info()
        print(f"유통기한 : {self.expiration_date}")


tv = Electronic("삼성스마트TV", 1500000, 2, 24)
# tv.display_info()
# tv.extend_warranty(12)
# tv.display_info()

milk = Food("서울우유", 3000, 30, "2024-12-10")
milk.is_expired("2024-11-28")
milk.is_expired("2024-12-28")
milk.display_info()
