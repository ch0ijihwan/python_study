
def factorial(n):
    if n == 1:      
        return 1   
    return n * factorial(n - 1)    
 
print(factorial(5))
num_1 = int( input("정수를 하나 입력하세요: "))

print(num_1 ,"!","의 값은 ", factorial(num_1)," 입니다.") 
