input_str = input("문자열을 입력하세요") #문자열 입력
input_str=input_str.replace(' ','') #공백제거
b_input_str = input_str[::-1]       #문자열을 뒤집어서 b_input_str로 저장

if(input_str==b_input_str): #조건문으로 회문인지 아닌지 판별
    print("회문입니다.")
else:
    print("회문이 아닙니다.")

