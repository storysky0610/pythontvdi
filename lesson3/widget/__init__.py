MON = 1
TUE = 2
WED = 3
THU = 4
FRI = 5
SAT = 6
SUN = 7

class Person(object):#class工廠化
    #自動地的initial 
    def __init__(self,name:str,age:int):#型別提示
        self.__name = name#private attribute
        self.__age = age#private atteibutie
    def __repr__(self)->str:#自訂規則
        return f'我的名子:{self.name}\n我的age是{self.age}'
    @property #註冊一個founction 無法修改
    def name(self)->str:#->str 傳出值 為 文字
        return self.__name


    @name.setter#setter語法
    def name(self,n):#re
        print(f"不可以改名為{n}")

    @property
    def age(self)->int: #getter 索取
        return self.__age
    @age.setter#設置  可修改範圍
    def age(self,value):
        if value > 100 or value < 0:
            print("不合法的值")
        else:
            self.__age = value
class Student(Person):#繼承


    @classmethod#註冊
    def echo(cls):
        print("Hello,我是studentclass")
    def __init__(self,age:int,name:str,chinese:int=0,english:int=0,math:int=0):#建立
        super().__init__(name=name,age=age)
        self.chinese = chinese
        self.enlish = english
        self.math = math

    @property#屬性
    def total(self)->int:#建立總分
        return self.chinese + self.enlish + self.math
    
    #intall method 實體方法
    def average(self)->float:
        return round(self.total/3,ndigits=2)
    
def get_person(name:str,age:int)->Person:
    return Person(name=name,age=age)

def get_student(name:str,age:int=60,chinese:int=60,math:int=60)->Student:
    return Student(name=name,age=age,chinese=chinese,math=math)