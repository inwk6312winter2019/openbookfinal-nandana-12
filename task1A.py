def unique_words(book):
	dic = {}
	list_unique = []
	for line in book:
		line = line.strip()
		line = line.split()
		for word in line:
			if word not in dic:
				dic[word] = 1
			else:
				dic[word]+=1
	for i,j in dic.items():
		list_unique.append(i)
	return list_unique 


def count_the_article(book):
	d = {}
	word_list = ["a", "the", "at", "run", "to","and","are","or","for","an","this"]
	for line in book:
		line = line.strip()
		line = line.split()
		for w in line:
			if w in word_list:
				d[w] = d.get(w,0) + 1
	return d


def sorted_words(book):
	dic1 = {}
	l = unique_words(book)
	li = []
	for w in l:
		if w not in dic1:
			dic1[w] = len(w)
	for m,n in dic1.items():
		li.append((n,m))

	li.sort(reverse = True)	
	return li


def character_word_count(book):
	dic1 = {}
        l = unique_words(book)
        li = []
        for w in l:
                if w not in dic1:
                        dic1[w] = len(w)
	return dic1 			 	  

def starts_with_vow(book):
	char_tup = ("a", "e", "i", "o", "u")
	count = 0
	for l in book:
		l = l.strip()
		l = l.split()
			for w in l:
				if w[0] in char_tup:
					count+=1
	return count	



book_name = input("enter the name of the book : ")
f1 = open(book_name)
print(unique_words(f1))
f2 =  open(book_name)
print(count_the_article(f2))
f3 = open(book_name)
print(sorted_words(f3))
f4 = open(book_name)
print(character_word-count(f4))
f5 = open(book_name)
print(starts_with_vow(f5))





