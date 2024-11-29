# 어제 실습 같이해보기
# 실습. 클래스 종합 프로그래밍

from abc import ABC, abstractmethod

electricity_usage = [
    {"date" : "2024-11-01", "usage" : 12.5},
    {"date" : "2024-11-02", "usage" : 15.3},
    {"date" : "2024-11-03", "usage" : 10.8},
    {"date" : "2024-11-04", "usage" : 14.2},
    {"date" : "2024-11-05", "usage" : 13.6}
]

#추상클래스
class ElectricityData(ABC):
    def __init__(self, usage_data, total_usage = 0):
        self._usage_data = usage_data
        self._total_usage = total_usage
        
    # 게터세터를 쓰는 이유는 위 생성자에 데이터를 넣고싶기때문에.
    @property
    def usage_data(self):
        return self._usage_data
    
    @usage_data.setter
    def usage_data(self, new_data):
        self._usage_data = new_data
    
    @property
    def total_usage(self):
        return self._total_usage
    
    @total_usage.setter
    def total_usage(self, new_total):
        self._total_usage = new_total
# 추상 메서드
    @abstractmethod
    def calculate_total_usage(self):
        pass

    @abstractmethod
    def get_usage_on_date(self, date):
        pass

# 일반 메서드
    def add_usage(self, date, usage):
        self._usage_data.append({"date" : date, "usage" : usage})
        #부모니까 이렇게 써도 된다.

    def remove_usage(self, date):
        self.usage_data = [ i for i in self._usage_data if i["date"] != date]

# 자식클래스
class HomeElectricityData(ElectricityData):

    # 정정. 자식클래스에 생성자 만드는 것 필요 없음.!!!! 그냥 명시적으로 만드는 것 뿐
    # 자동으로 부모클래스에서 값 받아와서 씀

    # 추상메서드 구현
    def calculate_total_usage(self): # super써도 되고, 게터세터방식사용해도 된다.
        self.total_usage = sum( i["usage"] for i in self.usage_data )

    def get_usage_on_date(self, date):
        for i in self.usage_data:
            if i["date"] == date:
                return i["usage"]
            
    # 클래스메서드

    @classmethod
    def filter_date(cls,usage_data , start_date, end_date):
        filtered_data = [ i for i in usage_data if start_date <= i["date"] <= end_date]
        return cls(filtered_data)
    
    @staticmethod
    def max_usage(usage_data):
        return max(usage_data, key=lambda x : x["usage"]) # 키 값
            
home = HomeElectricityData(electricity_usage)
home.calculate_total_usage()
print("총 전력 사용량", home.total_usage)
print("특정날짜 ", home.get_usage_on_date("2024-11-05"))
home.add_usage("2024-11-29", 11.0)
home.remove_usage("2024-11-02")
print(home.usage_data)

result = HomeElectricityData.filter_date(home.usage_data, "2024-11-01", "2024-11-05")
print(result.usage_data) # usage_data를 받아서 result로 가서 필터한다음 가져옴

max_result = HomeElectricityData.max_usage(electricity_usage)
print(max_result)

