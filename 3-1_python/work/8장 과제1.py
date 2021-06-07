num = {"one": "하나", "two":"둘","three":"셋","four":"넷"}


input_num = input("단어를 입력하세요")
    
if(input_num in num):
        print(num[input_num])
else:
        print("없는 단어 입니다.")
    
