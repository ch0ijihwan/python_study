"""
1. hello라는 파일을 만들어 주자.
2. hello라는 파일에 이름을 입력해 보자.
3. hello라는 파일에 있던 이름을 지우지 않고, 다음 줄에 전화번호를 입력해보자.
4. hello의 세번째 줄에 나이를 입력 해보자
5. hello의 모든 문장을 출력 해보자
6. hello에서 마지막 문장인 나이만 출력해보자.


"""


# 1번
with open('hello.txt', 'w') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
 
 file.close()

 #2번
 with open('hello.txt', 'w') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    data = "최지환 \n"
    file.write(data)
 file.close()

 #3번   
 with open('hello.txt', 'a') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    data = "010 - 1234 - 1234\n"
    file.write(data)
 file.close()


 #4번   
 with open('hello.txt', 'a') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    data = "나이 : 24 \n "
    file.write(data)
 file.close()

# 5번
 with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
     line = file.read()
     print(line)
 file.close()


 # 6번 마지막 문장인 나이만 출력해 보자

with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    line = file.readlines()
    print(line[-2]) #의문. 왜 -1이 아닐까.


file.close()
