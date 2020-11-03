def yield_function(file):
    field = next(file,"finish").split("\t") #lista me tin grammi
    field = [f.strip() for f in field] #bgazo to \n sto telos
    yield field

title_basics=open("title_basics_sort.tsv")
title_crew=open("title_crew_sort.tsv")
lst=list(open("title_crew_sort.tsv"))
last_line=lst[-1]
del lst[:]
arxeio=open("output1.1.txt",'w')
arxeio.write("primaryTitle"+"\t"+"directors"+"\n"+"-------------------------------------------------------"+"\n")

def merge_by_directors(file,id,directors):
	george1=next(yield_function(file))
	while(george1[0]!=id):
		george1=next(yield_function(file))
	else:
		arxeio.write(george1[2]+"\t"+directors+"\n")

next(yield_function(title_basics))
next(yield_function(title_crew))
george=[]
while(george!=last_line):
	george=next(yield_function(title_crew),"finish")
	if(len(george)<2):
		break
	elif(len(george[1])>10):
		merge_by_directors(title_basics,george[0],george[1])

title_basics.close()
title_crew.close()
arxeio.close()