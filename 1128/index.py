# 어제꺼 복습
# 실습. 건강상태 클래스 만들기
"""
class Health:
    def __init__(self, name):
        self._hp = 100
        self._name = name

    def get_name(self):
        return self._name
    def set_name(self,value):
        self._name = value

    def set_hp(self, value):
        self._hp = value
        if self._hp >= 100:
            self._hp = 100
        else:
            self._hp = value
    def get_hp(self):
        return self._hp
    
    def exercise(self, hour):
        self.set_hp(self._hp + hour)
        print(f"{hour}시간 운동하다.")
    def drink(self, cups):
        self.set_hp(self._hp - cups)
        print(f"술을 {cups}잔 마셨다.")
    
    def info(self):
        print(f"{self.get_name()}의 hp : {self.get_hp()}")

p1 = Health("나몸짱")
p1.set_hp(100)
p1.exercise(5)
p1.drink(2)
p1.info()
"""

# getter, setter 데코레이터
class Person:
    def __info__(self, name, age):
        self.__name = name
        self.__age = age

    #getter
    @property # 바로 밑에 붙여서 써야한다..!!! 안그러면 인식을 못함
    def name(self):
        return self.__name
    
    #setter
    @name.setter # getter에서 선언한 이름으로 @게터함수.setter해줘야한다!
    def name(self, value):
        self.__nae = value
    
    #getter
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = value

p1 = Person("홍길동", 20)
print(p1.name) # 데코레이터로 인해서 함수로 안써도 된다.
print(p1.age)

p1.name = "이몽룡"
p1.age = 25
print(p1.name)
print(p1.age)