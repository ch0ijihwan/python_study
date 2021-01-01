
# while문  : 반복해서 문장을 수행해야 할 경우 while문을 사용한다. 따라서 while는 반복문이라고 부른다.
"""
while 의 구조

while 조건문 : 
    수행 문장 1
    수행 문장 2

"""
# 예시 : 돌탑을 쌓는 프로 그램.
stone = 1
while stone <11:
    print("돌멩이 하나 올리고~")
    print("돌 탑 높이 %d" % stone)
    stone = stone + 1


# 여기서 문제. 만약 while문이 종료가 되지 않고 무한반복해서 실행이 된다면? 어떻게 해야할까?

#  while 강제로 빠져나가기 : break 문
coffee = 10
money = 300
while money: # 이경우 money의 값이 있으면 무조건 참이기 때문에 무한 루프에 빠지게 된다.
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d 개입니다" %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌어요")
        break #팔 커피가 없으므로 자판기는 중지를 하고 while문에서 탈출을 한다.


