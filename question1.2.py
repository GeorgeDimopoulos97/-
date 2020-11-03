def yield_function(file):
    field = next(file,"finish").split("\t") #lista me tin grammi
    field = [f.strip() for f in field] #bgazo to \n sto telos
    yield field

title_basics=open("title_basics_sort.tsv")
title_episode=open("title_episode_sort.tsv")
lst=list(open("title_episode_sort.tsv"))
last_line=lst[-1]
del lst[:]
arxeio=open("output1.2.txt",'w')
arxeio.write("primaryTitle"+"\t"+"parentTconst"+"\t"+"seasonNumber"+"\n"+"-------------------------------------------------------"+"\n")
def merge_by_episode(file,id,parentTconst,seasonNumber):
	george1=next(yield_function(file))
	while(id!=george1[0]):
		george1=next(yield_function(file))
	else:
		arxeio.write(george1[2]+"\t"+parentTconst+"\t"+seasonNumber+"\n")


next(yield_function(title_basics))
next(yield_function(title_episode))

george=[]
while(george!=last_line):
	george=next(yield_function(title_episode),"finish")
	if(len(george)<2):
		break
	elif(george[3]=="1"):
		merge_by_episode(title_basics,george[0],george[1],george[2])

title_basics.close()
title_episode.close()
arxeio.close()