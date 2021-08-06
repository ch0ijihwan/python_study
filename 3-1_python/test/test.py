inStr, outStr = "",""

count, i = 0,0

inStr = input("inStr")

count = len(inStr)

for i in range(0,count):
    outStr=outStr.append(inStr[count-(i+1)])


print(outStr)