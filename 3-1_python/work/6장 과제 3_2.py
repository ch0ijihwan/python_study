hap, i = 0,0

while(i<101):

    if(i%2 == 1):
        hap += i

   
    if hap>=1000:
        break

    i = i + 1

  

print("1~100의 합계를 최초로 1000이 넘는 위치 : %d" %i)
