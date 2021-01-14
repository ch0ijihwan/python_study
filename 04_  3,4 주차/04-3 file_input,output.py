f = open("newfile.txt" , 'w')
 # newfile.txt라는 이름의 파일을 'w'모드 즉 쓰기 모드로 불러옴.

for i in range(11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)  # data를 파일 객체 f에 써라. 
    #여기서 파일 객체 f는 newfile.txt 입니다.
f.close() #열었던 파일을 닫음
"""
이전 까지는 프로그램의 내부에서 단순 파일을 만들어 주거나, 값을 넣어주기만 했을 뿐이지, 외부의 파일안에 있는 데이터를 이용하지 못했다.

이번에는 외부에서 파일을 불러 그 안에 있는 데이터를 출력해보겠다.
"""
# readline 함수는 말 그대로 txt파일에서 읽기 모드로, 첫번째 문장을 불러와 준다.

f = open("newfile.txt",'r')
line = f.readline()
print(line)
f.close





"""readlines 함수
readlines 함수는 파일의 모든 줄을 읽어 각각의 줄을 요소로 갖는 리스트로 돌려준다. 

파일의 모든 글자를 리스트에 순서대로  한 '줄' 씩 넣어준다."""

f = open("newfile.txt",'r')
line = f.readlines()
print(line)
f.close()


#read 함수
#read 함수는 파일의 내용 전체를 문자열 형태로 받아와 준다.

f = open("newfile.txt",'r')
line = f.read()
print(line)
f.close()


# r모드 사용해보기

f = open("newfile.txt",'a')

for i in range(11,20): # 11부터 19까지 대입
    data = "%d \n" %i
    f.write(data)

f.close()

f = open("newfile.txt",'r')
line = f.read()
print(line)
f.close()

