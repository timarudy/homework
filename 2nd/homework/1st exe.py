#1

number = int(input("Give it to me! - "))

if (number >= 100):
    print ("Thanks, man!")
elif ((number > 10) and (number < 100)):
    print ("OK :(")
else:
    print ("WHAAAAT????")

if (number > 1000):
    print ("!!!!WOOOOWWWW!!!")

#2

test = True
result = 'Test is True' if test else 'Test is False'
print(result)

#3

print ('ttt' if test else 'fff')

#4

s = True

if s:
    print("s = true")
    
if 8 % 2:
    print("hm ok")

#5

a = 11
if a>10 and a < 20:
    print(a, "is a cool number")

#6

result = test and 'Test is True' or 'Test is False'
print(result)