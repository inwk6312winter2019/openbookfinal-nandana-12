import string

def words(book):
	d = {}
	d2 = {}
	l = []
	li = []
	punc = string.punctuation
	for line in book:
		line = line.strip()
		line = line.split()
		for w in line:
			for c in w:
				if c not in punc:
					l.append(w)
	for wo in l:
		d[w] = d.get(w,0) + 1
		for i,j in d.items(): 
			li.append((j,i))
		li.sort(reverse = True)
	for i in range(0,21):
		print(li[i][1])
		


f1 = open("Book1.txt")
#f2 = open("Book2.txt")
#f3 = open("Book3.txt")

words(f1)
