#문자열 관련 함수

#1.문자 개수 세기
a = "hobby"
print(a.count('b'))

# 2. 위치 알려주기 1(find)

a = "Python is the best choice"
print(a.find('b'))
print(a.find('k')) # 존재하지 않으면 -1 반환

# 3. 위치 알려주기 2(index)
a ="Life is too short"
print(a.index('t'))
#print(a.index('k')) # k가 없으면 오류 발생 

# 4. 문자열 삽입 (join)
print(",".join("abcd")) 
print(",".join(['a','b','c','d']))
# 각 문자열 사이에 , 삽입

#5. 소문자를 대문자로 바꾸기(upper)
a = "hi"
print(a.upper())

#6. 대문자를 소문자로 바꾸기
a = "hi"
print(a.lower())

#6. 왼쪽 공백 지우기(lstrip)
a = "     hi     "
print(a.lstrip())

#7. 오른쪽 공백 지우기(rstrip)
a = "     hi     "
print(a.rstrip())

#8. 양쪽 공백  지우기(strip)
a = "     hi     "
print(a.strip())

#9. 문자열 나누기(split)
a = "Life is too short"
print(a.split())

b= "a:b:c:d"
print(b.split(':')) # :를 기준으로 문자열 나눔
