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
	
fin = open("Book1.txt")
unique = unique_words(fin)
print(unique)
