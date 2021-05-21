jumin_num = input("주민등록번호를 입력하세요")
temp =jumin_num.split('-')  #임시공간에 -을 제외한 나머지 숫자부분을 저장

if(temp[-1].startswith('1')==True): #숫자 부분중 뒷 값의 맨앞이 1이면 남성
    print("남성입니다.")
 
else:                                #그렇지 않은 경우 여성
    print("여성입니다.")