numbers = [1,2,2,4,4,3] # 초기 리스트 생성


print("중복제거")

set_numbers = set(numbers) # 집합으로 변환 후 출력 
new_list = list(set_numbers)

print(new_list)

new_list2 = []

for i in numbers: # 반복문을 이용한 중복제거 
    if i not in new_list2:
        new_list2.append(i)

print(new_list2)
