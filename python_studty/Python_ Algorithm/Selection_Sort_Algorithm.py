import random

def selected_sort(random_list):

    
    for sel in range(len(random_list)-1): #램덤리스트 -1 을 해주어 총 몇번 연산을 하는지 확인.  n-1번을 해줘야함.
        min = random_list[sel]
        minindex = sel

        #find min value
        for step in range(sel+1,len(random_list)): # 여기서도 n 번
            if min > random_list[step]:
                min = random_list[step]
                minindex = step

        
        # swap
        random_list[minindex] = random_list[sel]
        random_list[sel] = min
    # 따라서 시간 복잡도는 (n-1) * n = n^2임. 빅오로는 O(n^2)
if __name__=='__main__':
    list=[]
    for i in range(10):
        list.append(random.randint(1,10))

    print("정렬전 : ")
    print(list) 
    selected_sort(list) #정렬 시작
    print("\n정렬 후")
    print(list)