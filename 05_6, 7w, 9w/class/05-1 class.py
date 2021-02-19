"""
class

같은 역할을 하는 기능들을 한곳에 몰아넣어 사용하기 쉽게함.

같은, 혹은 비슷한 기능을 하는 함수들을 매번 만들어주는 것이 복잡함. -> 클래스를 하용하여 함수를 만들어 주면 적재적소에 함수를 사용할 수 있음. 또한 변수 저장에도 용이함.

"""

#예시 계산기 만들어보기.

# class Calculator:
#     def __init__(self):
#         self.result = 0
#     def add(self, num):
#         self.result += num
#         return self.result

# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(5))
# print(cal2.add(23))



# #클래스 구조 만들기
# class FourCal:
#     def setdata(self,first,second):
#         self.first = first
#         self.second = second

#     def add(self):
#         result = self.first + self.second
#         return result

#     def sub(self):
#         result = self.first - self.second
#         return result
    
#     def mul(self):
#         result = self.first * self.second
#         return result

#     def div(self):
#         result = self.first / self.second
#         return result

# a = FourCal()
# b = FourCal()

# a.setdata(1,3)
# b.setdata(4,2)

# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())


# print(b.add())
# print(b.sub())
# print(b.mul())
# print(b.div())




#클래스 구조 만들기
class FourCal:
    def __init__(self,first,second): ##생성자 선언 방법
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

a = FourCal(1,3)# 생성자가 있으면 객체 생성과 동시에 생성자가 필요로
 #하는 매개변수를 지정해줘야한다.
b = FourCal(4,2)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

print(b.add())
print(b.sub())
print(b.mul())
print(b.div())


############상속
"""
1. 상속이란 '물려받다.'라는 뜻이다. 클래스를 생성하는데 있어서 같은 기능을 하는 클래스를 중복되게 생성할 필요는 없다. 

2. 예를 들어 일반 계산기 클래스가 있다고 가정하자. 우리가 공학용 계산기를 만들려할 때 공학용 계산기에는 일반 계산기가 하는 일은 당연히 작동해야한다.

3. 즉, 공학용 계산기를 만들때 일반 계산기가 하는 일을 '상속'받아 공학용 계산기를 만들 수 있다.
"""
#x 클래스를 y클래스가 상속 받는다면.
class x :
	pass #여기서 pass는 말 그대로 통과이다. 아무 기능을 하지 않는 클래스이기 때문에 사용

class y (x):
	pass




class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result



T = MoreFourCal(2,3)
print(T.pow())


###매서드 오버라이딩
"""
## 매서드 오버라이딩(Overriding, 덮어쓰기)

상속받은 클래스가 부모클래스에 있는 메서드를 동일한 이름으로 다시 작성하는 것

오버라이딩을 하면 부모클래스의 맷드 대신 오버라이딩한 자식 클래스의 매서드가 호출된다.
"""


class Family :
    lastname = "최"

"""
Family 클래스에 선언한 lastname "최"가 바로 클래스 변수이다.
"""
print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

#만약 최를 김으로 바꾸면 어떻게 될까?
Family.lastname = "김"
print(a.lastname)
print(b.lastname)

