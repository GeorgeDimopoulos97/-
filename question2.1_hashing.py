import time

title_ratings=open("title_ratings_sort.tsv")
lst=list(open("title_ratings_sort.tsv"))
del lst[0]
george=[]
for i in range(0,len(lst)):
	george.append(float(lst[i][10:13]))
del lst[:]
title_ratings.close()
start=time.time()
hash=[0,0,0,0,0,0,0,0,0,0]
for i in range(0,len(george)-1):
	if george[i]<=1:
		hash[0]=hash[0]+1
	elif george[i]>=1.1 and george[i]<=2:
		hash[1]=hash[1]+1
	elif george[i]>=2.1 and george[i]<=3:
		hash[2]=hash[2]+1
	elif george[i]>=3.1 and george[i]<=4:
		hash[3]=hash[3]+1
	elif george[i]>=4.1 and george[i]<=5:
		hash[4]=hash[4]+1
	elif george[i]>=5.1 and george[i]<=6:
		hash[5]=hash[5]+1
	elif george[i]>=6.1 and george[i]<=7:
		hash[6]=hash[6]+1
	elif george[i]>=7.1 and george[i]<=8:
		hash[7]=hash[7]+1
	elif george[i]>=8.1 and george[i]<=9:
		hash[8]=hash[8]+1
	elif george[i]>=9.1 and george[i]<=10:
		hash[9]=hash[9]+1
end=time.time()
print "0.1 - 1.0  :   ",hash[0]
print "1.1 - 2.0  :   ",hash[1]
print "2.1 - 3.0  :   ",hash[2]
print "3.1 - 4.0  :   ",hash[3]
print "4.1 - 5.0  :   ",hash[4]
print "5.1 - 6.0  :   ",hash[5]
print "6.1 - 7.0  :   ",hash[6]
print "7.1 - 8.0  :   ",hash[7]
print "8.1 - 9.0  :   ",hash[8]
print "9.1 - 10.0 :   ",hash[9],"\n--------------------------------\n"
print "Total time: ",end-start