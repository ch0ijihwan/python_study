test_str = input("문자열을 입력하세요 : ")
out_str=test_str.title()

for i in out_str:
    if (i.isupper()):
        print(i, end='')
