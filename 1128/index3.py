# 클래스 메서드
"""

# 클래스 변수에 접근


class Converter:
    conversion_rate = 1.60934

    @classmethod
    def miles_to_kilometer(cls, mile): # self가 없이 cls.
        return mile * cls.conversion_rate # cls를 통해서 클래스 속성에 접근

print(Converter.miles_to_kilometer(7))


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls,name,birth_year):
        age = 2024 - birth_year
        return cls(name, age) # cls를 씌우지 않으면 튜플로 리턴된다. 값을 메서드로 사용하고 싶으면 cls를 붙여야한다.
    
    
# 클래스 메서드를 통해서 객체 생성    
p1 = Person.from_birth_year("홍길동", 1990)
print(p1.name, p1.age)


# 클래스변수를 사용하는 법.
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

Counter.increment()
Counter.increment()
Counter.increment()
Counter.increment()
Counter.increment()
print(Counter.get_count())


# 자식클래스의 정보유지

class Animal:
    species = "동물"

    @classmethod
    def get_species(cls):
        return cls.species

class Dog(Animal): #서브클래스의 정보를 유지시켜준다.
    species = "진돗개"

print(Animal.get_species())
print(Dog.get_species())


# 정적메서드
class MathUtils:
    @staticmethod
    def add(a, b):
        return a+b
    
    @staticmethod
    def minus(a, b):
        return a-b
print(MathUtils.add(30,40))
print(MathUtils.minus(10, 20))
"""

# 실습. 클래스 종합 프로그래밍

# 날짜별 전력사용량
electricity_usage = [
    {"date" : "2024-11-01", "usage" : 12.5},
    {"date" : "2024-11-02", "usage" : 15.3},
    {"date" : "2024-11-03", "usage" : 10.8},
    {"date" : "2024-11-04", "usage" : 14.2},
    {"date" : "2024-11-05", "usage" : 13.6}
]

from abc import ABC, abstractmethod

class EletricityData(ABC):

    def __init__(self, usage_data, total_usage = 0):
        
        self._usage_data = usage_data
        self._total_usage = total_usage
    @property
    def usage_data(self):
        return self._usage_data
    
    @usage_data.setter
    def usage_data(self, new_data):
        self._usage_data = new_data

    @property
    def total_data(self):
        return self._total_usage
    
    @total_data.setter
    def total_usage(self, new_total):
        self._total_data = new_total

    @abstractmethod
    def calculate_total_usage(self):
        pass
    
    @abstractmethod
    def get_usage_on_date(self, date):
        pass

    def add_usage(self, date, usage): # 새로운 날짜의 전력 사용량을 추가
        self._usage_data.append({"date" :date , "usage" : usage})


        
    def remove_usage(self,date): # 특정 날짜의 전력 사용량 데이터 삭제

        for i in self._usage_data: # 잘 모르겠습니다....
            if i["date"] == date:
                self._usage_data.remove["date"] 
        


class HomeElectricityData(EletricityData):

    @classmethod
    def date_range_filter(cls,usage_data, min, max):
        return [data for data in usage_data if min <= (data["date"]) <= max]
    
    @staticmethod
    def highest_usage(usage_data):
        return max(list(map(lambda x : x["usage"], usage_data)))


    def calculate_total_usage(self): # 전력 사용량 데이터를 기반으로 총 사용량을 계산
        total = 0
        for data in range(len(self._usage_data)):
            total += self._usage_data[data]["usage"]
        print(f"총 전력 사용량 : {total:.1f}")
        
       
    def get_usage_on_date(self, date): # 특정 날짜의 전력사용량을 반환
        return [data["usage"] for data in self._usage_data if data["date"] == date]
    
    
        
    


        

home = HomeElectricityData(electricity_usage)
home.calculate_total_usage() 

date = "2024-11-03"
print(f"{date}의 사용량 : {home.get_usage_on_date(date)}")

add_date = "2024-11-06"
home.add_usage(add_date,16.5)
print(f"{add_date}추가 후 총 전력 사용량 : ", end ="")
home.calculate_total_usage()

# home.remove_usage("2024-11-03")


print(f"특정 날짜 범위 내 사용량 : {home.date_range_filter(electricity_usage,"2024-11-01", "2024-11-03")}")

print(f"가장 높은 사용량 : {home.highest_usage(electricity_usage):.1f}")


