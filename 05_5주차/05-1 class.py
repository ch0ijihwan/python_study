"""
class

같은 역할을 하는 기능들을 한곳에 몰아넣어 사용하기 쉽게함.

같은, 혹은 비슷한 기능을 하는 함수들을 매번 만들어주는 것이 복잡함. -> 클래스를 하용하여 함수를 만들어 주면 적재적소에 함수를 사용할 수 있음. 또한 변수 저장에도 용이함.

"""

#예시 계산기 만들어보기.

class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(5))
print(cal2.add(23))



#클래스 구조 만들기
class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
b = FourCal()

a.setdata(1,3)
b.setdata(4,2)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())


print(b.add())
print(b.sub())
print(b.mul())
print(b.div())