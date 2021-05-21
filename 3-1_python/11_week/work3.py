# otp 암호 만들기

import random

num = "0123456789"
pwlen=4 
a = "".join(random.sample(num,pwlen) )# num 중에, pwlen개수만큼 랜덤으로 가져옴
print(a)
print(type(a))  
