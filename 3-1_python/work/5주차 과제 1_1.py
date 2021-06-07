print("시작값을 입력하세요 : ")

start = int(input())

end = int(input("끝값을 입력하세요 : "))
plus = int(input("증가값을 입력하세요 : "))

result = 0


for i in range(start,end,plus):
    result = result + i


print(start,"에서 ", end ,"까지 증가시킨 값의 합계 : " , result)
