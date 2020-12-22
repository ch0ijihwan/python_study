#02-3 리스트 자료형

#리스트의 형태
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

# 비어 있는 리스트 생성시
empty_list = list()

#리스트의 인덱싱과 슬라이싱

#리스트의 인덱싱
a = [1, 2, 3]
print(a)
#a[0]은 리스트의 a의 첫 번째 요솟값을 말한다.
print(a[0])
#a[0]과 a[2]를 더한 값 출력
print(a[0] + a[2])
#a[-1]은 마지막 요소 출력
print(a[-1])


#리스트 안에 또 다른 리스트가 있는 경우
a = [1, 2, 3, ['a', 'b', 'c']]
print(a)

print(a[0])
print(a[-1])
print(a[3])

#a리스트에서 'a' 값을 뽑아 출력
print(a[-1][0])
print(a[3][0])


#삼중리스트 예제
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])


##########################
#리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])

#예시
a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print(b)
print(c)

#중첩된 리스트에서 슬라이싱하기
a = [1,2,3,['a','b','c'],4,5]
print(a[2:5])
print(a[3][:2])

############################
#리스트 연산하기
#1. 리스트 더하기(+)
a = [1,2,3]
b = [4,5,6]
print(a+b)

#2. 리스트 반복하기 (*)
a = [1,2,3]
print(a*3)

#3. 리스트 길이 구하기
print(len(a))


#############################3
# 리스트의 수정과 삭제

# 리스트에서 값 수정하기
a = [1,2,3]
a[2] =4
print(a)

#del 함수 사용해 리스트 요소 삭제하기
a = [1,2,3]
del a[1]
print(a)

#슬라이싱을 이용해 값 여러개 삭제
a = [1,2,3,4,5]
del a[2:]
print(a)


##############################
#리스트 관련 함수

#1. 리스트에 요소 추가(append)
a = [1,2,3]
a.append(4)
print(a)

a.append([5,6])
print(a)

#2. 리스트 정렬(sort)
a = [1,5,2,4]
a.sort()
print(a)

a = ['a','d','c','b','e']
a.sort()
print(a)

#3. 리스트 뒤집기(reverse)
a = ['a','c','b']
a.reverse()
print(a)


#4. 위치 반환(index)
a = [1,2,3]
print(a.index(3))
print(a.index(1))

#5.리스트에 요소 삽입(insert)
a =[1,2,3]
a.insert(0,4) #a[0]위치에 4 삽입
print(a)

#6. 리스트 요소 제거(remove)
a = [1,2,3,1,2,3]
a.remove(3) #오소의 첫번째로 나오는 3 삭제
print(a)

#7. 리스트 요소 끄집어 내기
a = [1,2,3]
a.pop()
print(a)

#8.리스트에 포함된 요소 x의 개수 세기(count)
a = [1,2,3,1]
print(a.count(1))

#9.리스트 확장(extend) 
a = [1,2,3]
a.extend([4,5])
print(a)
b=[6,7]
a.extend(b)
print(a)