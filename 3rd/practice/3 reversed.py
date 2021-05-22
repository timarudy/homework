import sys
filename = sys.argv[0]
f = open(filename, 'r')
f_1 = list(f)
for line in reversed(f_1):
	line_rev = line[::-1]
	print(line_rev)
f.close()


