#1

print("1st programme")

n = int(input ("n="))

if ( n % 2 == 0):
    print ("Number n is countable")
else:
    print ("Number n is uncountable")

#2

print("2nd programme")

m = int(input ("m="))

if (m % 2):
    print ("Number n is uncountable")
else:
    print ("Number n is countable")

if (not (m % 3) and not (m % 5) and (m % 10)):
    print ("true")
else:
    print("false")

#3

print("3rd programme")

y = int(input ("y="))

i = 1 

for i in range(y):
    i += 1
    if (y % i == 0):
        print(i)

#4

print("4th programme")

sum = int(input("sum="))

conv = str(sum)

print(" ".join(conv))

