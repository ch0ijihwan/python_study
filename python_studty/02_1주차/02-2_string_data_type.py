#2-2

#문자열 출력해보기
print("Hello World")
print('Python is fun')

#따옴표를 이용하여 출력
print("""Life is too short, You need python""")
print('''Life is too short need ptyhon''')

#문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때
print("Python's favorite food is perl") # "" 안에있는 ' 는 문자열을 나타내기 위한 기호로 인식되지 않는다.

#문자열을 변수 안에 저장하고 출력해보자.
food = "Python's favorite food is perl"
print(food)

# 백슬래시(/)를 사용하여 작은따음표와(') 큰따옴표(")를 문자열에 포함시키기
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says"
print(food)
print(say)

#여러 줄인 문자열을 변수에 대입하고 싶을 때
multiline = "Life is too short \n You need python"
print(multiline)


# 문자열 연산하기
#1. 문자열 더해서 연결하기
head = "Python"
tail = " is fun"
print(head + tail)


#2.문자열 곱하기
a = "Python \n"
print(a*3)

#3.문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)

#4. 문자열 길이 구하기
a = "Life is too short"
print(len(a))

