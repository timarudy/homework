#condition
print("Our ATM does not take the bill < than 20 UAH")
summa = int(input("Enter the amount of money - "))


#notes list
notes = [1000, 500, 200, 100, 50, 20]


if (summa < notes[5]):
    print("Our ATM does not take the bill < than 20 UAH")
else:
    pass

i = 5000

#function
def circle(x):
    for i in range(summa, 0, -1):
        i -= 1
        if not(i % x):
            print(x)
        else:
            pass
    return summa -= x

#output

item = 0

while item < len(notes):
    circle(notes[item])
    item += 1