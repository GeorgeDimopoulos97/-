def yield_function(file):
    field = next(file,"finish").split("\t") #lista me tin grammi
    field = [f.strip() for f in field] #bgazo to \n sto telos
    yield field

def exit_method():
	title_basics.close()
	title_ratings.close()
	arxeio.close()
	exit()

title_basics=open("title_basics_sort.tsv")
title_ratings=open("title_ratings_sort.tsv")
lst=list(open("title_basics_sort.tsv"))
last_line=lst[-1]
del lst[:]
arxeio=open("output1.3.txt",'w')
arxeio.write("primaryTitle"+"\n"+"-----------------------------------"+"\n")

next(yield_function(title_basics))
next(yield_function(title_ratings))

george=next(yield_function(title_basics))
george1=next(yield_function(title_ratings))
while(george!=last_line):

	while(george[0]==george1[0]):
		george=next(yield_function(title_basics))
		george1=next(yield_function(title_ratings))
		if(len(george1)<2):
			exit_method()
	while(george[0]!=george1[0]):
		if(len(george)<2):
			exit_method()
		arxeio.write(george[2]+"\n")
		george=next(yield_function(title_basics),"finish")
