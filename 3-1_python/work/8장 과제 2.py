menu = {"Americano":3000,"Ice Americano":3500,"Cappuccino":4000,
        "Caffe Latte":4500,"Espresso":3600}

print("Americano         3000원")
print("Ice Americano     3500원")
print("Cappucino         4000원")
print("Caffe Latte       4500원")
print("Espresso          3600원") 


input_mene = input("위의 메뉴중 하나를 선택하세요 : ")

if input_mene in menu:
    print(input_mene,"는 ",menu[input_mene],"원 입니다. 결재를 부탁합니다")
