def create_log(fi,f1,f2,f3,f4):
	for line in fi:
		if("GET" in line):
			f1.write(line)

		elif("POST" in line):
			f2.write(line)

		elif("PUT" in line):
			f3.write(line)
		
		elif("DELETE" in line):
			f4.write(line)


fi = open("access.log")
f1 = open("get.log",'w')
f2 = open("post.log",'w')
f3 = open("put.log",'w')
f4 = open("delete.log",'w')

create_log(fi,f1,f2,f3,f4)
