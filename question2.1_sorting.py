import time

title_ratings=open("title_ratings_sort.tsv")
lst=list(open("title_ratings_sort.tsv"))
del lst[0]
george=[]
for i in range(0,len(lst)):
	george.append(float(lst[i][10:13]))
del lst[:]
title_ratings.close()

count=0
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0

start=time.time()
george.sort()
for i in range(0,len(george)-1):
	if george[i]<=1:
		count=count+1
		i=i+1	
	elif george[i]>=1.1 and george[i]<=2:
		count1=count1+1		
	elif george[i]>=2.1 and george[i]<=3:
		count2=count2+1
	elif george[i]>=3.1 and george[i]<=4:
		count3=count3+1
	elif george[i]>=4.1 and george[i]<=5:
		count4=count4+1
	elif george[i]>=5.1 and george[i]<=6:
		count5=count5+1
	elif george[i]>=6.1 and george[i]<=7:
		count6=count6+1
	elif george[i]>=7.1 and george[i]<=8:
		count7=count7+1
	elif george[i]>=8.1 and george[i]<=9:
		count8=count8+1
	elif george[i]>=9.1 and george[i]<=10:
		count9=count9+1
end=time.time()	
print "0.1 - 1.0  :   ",count
print "1.1 - 2.0  :   ",count1 
print "2.1 - 3.0  :   ",count2 
print "3.1 - 4.0  :   ",count3 
print "4.1 - 5.0  :   ",count4 
print "5.1 - 6.0  :   ",count5 
print "6.1 - 7.0  :   ",count6 
print "7.1 - 8.0  :   ",count7 
print "8.1 - 9.0  :   ",count8
print "9.1 - 10.0 :   ",count9,"\n--------------------------------\n"
print "Total time: ",end-start