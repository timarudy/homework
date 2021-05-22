python = ['Anthony', 'Timur', 'Kolya']
frontend = ['Luisa', 'Anthony', 'Toe']
java = ['Ron', 'Kon', 'Ilona', 'Timur']
fullstack = ['Anthony', 'Tom', 'Harry']


subj = {'python': python, 'frontend': frontend, 'java': java, 'fullstack': fullstack}

for_more = []

#1
for item in subj:
    for index in subj[item]:
        for_more.append(index)
        lad_amount = for_more.count(index)
        if lad_amount > 1:
            print(lad_amount, index)
#2
all_lad = set(python + frontend + java + fullstack)
not_frontend = list(all_lad - set(frontend))
print(not_frontend)
#3
python_and_java = list(set(python + java))
print(python_and_java)
