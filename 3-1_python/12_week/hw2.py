
#함수부분##
def hap(num):
   
    add = 0
    
    
    for i in range(len(num)): 
        add = add + int(num[i]) #각 자리수를 int로 바꾼 후 add 에 더함.

    return add
        




    
##메인부분##
input_number = input("정수를 입력하세요 : ")

print(hap(input_number))
