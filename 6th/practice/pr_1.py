john = [10, 12, 7, 6, 2]
martin = [6, 9 ,2 ,2, 7]
ivan = [4, 6, 8, 4, 8]
tom = [12, 12, 3, 6, 9]

students_marks = {'John Wall': john, 'Martin Leuter': martin, 'Ivan Kolesnik': ivan, 'Tom Barton Jr': tom}

mid_list = []

for i in students_marks:
    mid = sum(students_marks[i]) / len(students_marks[i])
    mid_list.append(mid)                                  

for item in students_marks:
    if sum(students_marks[item]) / len(students_marks[item]) == min(mid_list):
        print(item, " - stupid fellow. He has", min(mid_list))
    if sum(students_marks[item]) / len(students_marks[item]) == max(mid_list):
        print(item, " - cool dude. He has", max(mid_list))

    



