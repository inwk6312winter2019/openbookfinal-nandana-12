import string

def words(book):
	d = {}
	d2 = {}
	l = []
	li = []
	punc = string.punctuation
	for line in book:
		line = line.strip(punc)
		line = line.split()
		for w in line:
			d[w] = d.get(w,0) + 1
		for i,j in d.items(): 
			li.append((j,i))
		li.sort(reverse = True)
	for i in range(0,21):
		print(li[i][1])
		
f1 = open("Book1.txt")
f2 = open("Book2.txt")
f3 = open("Book3.txt")

words(f1)
words(f2)
words(f3)
