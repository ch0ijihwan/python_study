


#1번
a_list = [44,66,34,24,144,98,568,234,345]
A_list = [x for x in a_list if x%12 == 0]
print(a_list)
print(A_list)

print("\n")


#2번

b_list = [-22.3,29.44,902.2,45.7,-887.1,-56.3]
B_list = [int(x) for x in b_list if x >0]
print(b_list)
print(B_list)
