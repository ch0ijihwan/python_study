print("## 철수와 영이의 가위, 바위, 보 게임")

ca = input("철수는 무엇을 낼까요? ")
yo = input("영이는 무엇을 낼까요? ")

if ca  =='가위' :
    pass
elif ca  =='바위':
    pass
elif ca  == '보':
    pass
else:
    print("철수의 값 입력 오류=>",ca)


if yo  =='가위' :
    pass
elif yo  =='바위':
    pass
elif yo  == '보':
    pass
else:
    print("영이의 값 입력 오류=>",yo)

    



if(ca=='가위' and yo=='보') or (ca=='바위' and yo =='가위') or(ca=='보' and yo=='바위') :
    print('철수가 이겼습니다.')

elif(ca=='가위' and yo=='가위') or (ca=='바위' and yo =='바위') or(ca=='보' and yo=='보') :
    print('무승부 입니다.')

else:
    print("영이가 이겼습니다")
