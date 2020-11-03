def yield_function(file):
    field = next(file,"finish").split("\t") #lista me tin grammi
    field = [f.strip() for f in field] #bgazo to \n sto telos
    yield field

def exit_method():
	title_basics.close()
	title_ratings.close()
	for i in sorted (dict.keys()):
		print "year: ",i," average rating: ",dict[i][0]/dict[i][1]	
	exit()

title_basics=open("title_basics_sort.tsv")
title_ratings=open("title_ratings_sort.tsv")
lst=list(open("title_basics_sort.tsv"))
last_line=lst[-1]
del lst[:]
dict={}
def merge_by_starYear(year,rating):
	if year=="\\N":
		count=0
	elif int(year) in dict:
		dict[int(year)][0]=dict[int(year)][0]+rating
		dict[int(year)][1]=dict[int(year)][1]+1
	else:
		dict[int(year)]=[rating,1]

next(yield_function(title_basics))
next(yield_function(title_ratings))

george=next(yield_function(title_basics))
george1=next(yield_function(title_ratings))
while(george!=last_line):

	while(george[0]==george1[0]):
		merge_by_starYear(george[5],float(george1[1]))
		george=next(yield_function(title_basics))
		george1=next(yield_function(title_ratings))
		if(len(george1)<2):
			exit_method()
	while(george[0]!=george1[0]):
		if(len(george)<2):
			exit_method()
		george=next(yield_function(title_basics),"finish")
