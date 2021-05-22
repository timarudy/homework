size = input("Enter the International size: ")

international = {1: 'XXS', 2: 'XS'}

for keys in international:
    if sorted(list(international[keys])) == sorted(list(size)):
        print(international[keys])

#тут я немного еще не успел доделать как только доделаю сброшу