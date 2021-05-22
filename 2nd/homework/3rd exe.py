#FIZZ-BUZZ

print("FIZZ-BUZZ GAME!!!")

fizz = int(input("fizz="))
buzz = int(input("buzz="))
third_num = int(input("num="))

for i in range(third_num):
    i += 1
    if not(i % buzz) and not(i % fizz):
        print("FB")
    elif not i % buzz:
        print("B")
    elif not i % fizz:
        print("F")
    else:
        print(i)