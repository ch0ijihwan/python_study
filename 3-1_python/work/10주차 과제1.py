"""
contacts ={}

while True:
    
    mode = input("1) 전화번호 저장, 2) 전화번호 검색")

    if mode =="1":
        name = input("저장할 사용자의 이름을 입력하세요")
        tel = input("전화번호를 입력하세요.")
        contacts[name] = tel

    elif mode == "2":
        name = input("검색할 사용자의 이름을 입력하세요.")
        print(contacts.get(name,"그런 데이터는 없습니다"))
"""


numbers = [1,2,2,4,4,3] # 초기 리스트 생성
print(numbers)


print("중복제거")

set_numbers = set(numbers) # 집합으로 변환 후 출력 
new_list = list(set_numbers)

print(new_list)

new_list2 = []

for i in numbers: # 반복문을 이용한 중복제거 
    if i not in new_list2:
        new_list2.append(i)

print(new_list2)




