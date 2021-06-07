he = int(input("키를 센치미터 단위로 입력하세요 : "))

we = int(input("몸무게를 킬로그램 단위로 입력하세요 : "))

bmi = we/((he/100)**2)
print("당신의 BMI는",bmi,"입니다.")
