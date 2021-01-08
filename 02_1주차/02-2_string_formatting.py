 
#문자열 포매팅 
# 문자열 안의 특정한 값을 바꿔야 할 경우가 있을 때 이것을 가능하게 해주는 것이 바로 문자열 포매팅 기법이다.

# 1. 숫자 바로 대입
print("I eat %d apples." % 3)

# 2. 문자열 배로 대입 [ ""과 ""사이에 ,를 넣지말자. C언어랑 다르다.] 
print("I eat %s apples." % "five")

#3. 숫자 값을 나타내는 변수로 대입
number = 3
print( "I eat %d apples" % number)

#4. 2개 이상의 값 넣기
number = 10
day = "three"
print(" I ate %d apples. so I was sick for %s days." % (number, day)) 
# % 뒤에 ( ) 값에 순서대로 변수 입력.

#%s 포맷 코드에는 어떤 형태의 값이든 변환해 넣을 수 있다!!
print("I have %s apples" %3)
print("rate is %s" %3.234)

#포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다.
# 즉 %을 출력하긴 위해선 %%를 써줘야한다.
print("Error is %d%%. " %98)

#vhaot zhemdh ktntwk gkaRp tkdydgkrl

#1. 정렬과 공백 포맷 코등
print("%10s" % "hi")

print("%-10sjane"% 'hi') #hi를 왼쪽으로 10칸만큼 정렬하고 jane 출력.

#2. 소수점 표현하기
print("%0.4f"%3.42134234) # 소수점 4번째 자리 까지만 출력
print("%10.4f"%3.42134234) # 소수점 4번째 짜리 까지 출력하고 전체길이가 10개

#3.숫자 바로 대입하기
print("I eat {0} apples".format("five"))

#4.숫자 값을 가진 변수로 대입하기
number = 3
print("I eat {0} apples".format(number))

#5. 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number,day))

#6. 이름으로 넣기
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))

#7. 인덱스와 이름을 혼용해서 넣기
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))

#8. 왼쪽 정렬
print ("{0:<10} jihwan".format("hi")) #왼쪽 정렬로 hi를 10칸으로 규격으로 출력하고 나머지 출력

#9. 오른쪽 정렬
print ("{0:>10} jihwan".format("hi"))

#10. 가운데 정렬
print ("{0:^10} jihwan".format("hi"))

#11. 공백 채우기
print ("{0:=^10} jihwan".format("hi"))
print("{0:!<10}".format("hi"))

#12. 소수점 표현하기 
y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))

#13. { 또는 } 표현하기
print("{{ and }}" .format()) # {{ 혹은 }} 처럼 두번 누르면 한번 출력 됨

#14. f 문자열 포매팅
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다. ') # f사용시 format 생략

#f문자열 포매팅은 변수 값을 생성한 후에 그 값을 참조할 수 있다. 또한 f포매팅은 표현식을 지원한다.
age = 30
print(f"나는 내년이면 {age+1}살이 된다.")

#f문자열 포맷팅 정렬
print(f'{"hi":<10}')#왼쪽 정렬
print(f'{"hi":>10}')#오른쪽 정렬
print(f'{"hi":^10}')#가운데 정렬

#f 문자열 공백채우기
print(f'{"hi":=^10}')
print(f'{"hi":+<10}')

# !!!python!!! 출력해보기
print(f'{"python":!^12}')



