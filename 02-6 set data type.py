# 집합 자료형
s1 = set([1,2,3])
print(s1)

s2 = set("Hello")
print(s2) 
#집함은 순서가 없기 때문에 인덱싱이 불가능하다. 따라거 인덱싱을 해주려면 리스트나 튜플로 변환해야한다.

s1 = set([1,2,3])
l1 = list(s1)
print(l1)

#교집합, 합집합, 차집합 구하기
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

#교집합
print(s1&s2)
print(s1.intersection(s2))

#합집합
print(s1|s2)
print(s1.union(s2))

#차집합
print(s1-s2)
print(s1.difference(s2))

#########################################3
#집합 자료형 관련 함수

# 값 추가하기 add
s1 = set([1,2,3])
s1.add(4)
print(s1)

# 값 여러개 추가하기(updata)
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)

#특정 값 제거하기(remove)
s1 = set([1,2,3])
s1.remove(2)
print(s1)
