#딕셔너리 : 대응 관꼐를 나타내는 자료형, => 연관 배열 또는 해시라고 부름.
#특징 : 리스트나 튜플 처럼 순차적으로 해당 요솟값을 구하지 않고 Key를 통해 Value를 얻는다. -> 사전이라고 생각하면 편함.

#예시
dic = {'name': 'pey', 'phone': '01199993323', 'burth': '1118'}
print(dic)

#1. 딕셔너리 쌍 추가하기, 삭제하기
a = {1: 'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

a[3] = [1, 2, 3]
print(a)

#2. 딕셔너리 요소 삭제하기
del a[1]
print(a)

#########################
#딕셔너리를 사용하는 방법

#딕셔너리에서 Key사용해 Value 얻기
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])


#리스트,튜플,문자열은 인덱싱, 슬라이싱이 가능. 하지만 딕셔너리는 불가함. key값을 이용해서 Value를 구해야 함.
a = {1: 'a', 2: 'b'}
print(a[1])
print(a[2])

#반대로 뒤집어서도 가능
a = {'a': 1, 'b': 2}
print(a['a'])
print(a['b'])

# 딕셔너리를 만들 때 주의할 사항
#Key는 고유한 값이므로 중복되는 key값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다.
a= {1:'a',1:'b'}
print(a) #이럴 경우'a'는 무시된다. key를 통해 value에 진입을 하는데 동일한 key가 존재해서 어떤 value를 불러올지 모른다.
#또한 리스트는 값이 변할 수 있기 때문에 key로는 쓰이지 않는다.

################################################################################################################
#딕셔너리 관련 함수

# 1. key리스트 만들기(keys)
a = {'name':'pey','phone':'0119993323','birth':'1118'}
print(a.keys())
print(a.values())


#1. 응용
for k in a.keys():
    print(k)

# 2. key, Value 쌍 얻기 (items)
print(a.items())

# 3. Key: Value 쌍 모두 지우기 (clear)
a.clear()
print(a)

# 4. Key로 value얻기 (get)
a = {'name':'pey','phone':'0119993323','birth':'1118'}
print(a.get('name'))
print(a.get('phone'))

print(a.get('no')) # 찾으려는 키값이 없으면 none 반환
print(a.get('no', 'bar')) #없는 경우 반환 값을 지정해 줄 수 있음

#5. 해당 key가 딕셔너리 안에 있는지 조사하기 (in)
a = {'name':'pey','phone':'0119993323','birth':'1118'}
print('name' in a)
print('email' in a)
