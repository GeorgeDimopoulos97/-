def takeSecond(elem):
    return float(elem[2:10])

#sort gia title.crew.tsv
title_crew=open("title.crew.tsv")
title_crew_sort=open("title_crew_sort.tsv",'w')
lst=list(open("title.crew.tsv"))
title_crew_sort.write(lst[0])
del lst[0]
lst.sort(key=takeSecond)
title_crew_sort.writelines(lst)
del lst[:]
title_crew_sort.close()
#telos sort gia title.crew.tsv

#sort gia title.basics.tsv
title_basics=open("title.basics.tsv")
title_basics_sort=open("title_basics_sort.tsv","w")
lst=list(open("title.basics.tsv"))
title_basics_sort.write(lst[0])
del lst[0]
lst.sort(key=takeSecond)
title_basics_sort.writelines(lst)
del lst[:]
title_basics_sort.close()
#telos gia title.basics.tsv

#sort gia title.episode.tsv
title_episode=open("title.episode.tsv")
title_episode_sort=open("title_episode_sort.tsv","w")
lst=list(open("title.episode.tsv"))
title_episode_sort.write(lst[0])
del lst[0]
lst.sort(key=takeSecond)
title_episode_sort.writelines(lst)
del lst[:]
title_episode_sort.close()
#telos gia title.episode.tsv

#sort gia title.ratings.tsv
title_ratings=open("title.ratings.tsv")
title_ratings_sort=open("title_ratings_sort.tsv","w")
lst=list(open("title.ratings.tsv"))
title_ratings_sort.write(lst[0])
del lst[0]
lst.sort(key=takeSecond)
title_ratings_sort.writelines(lst)
del lst[:]
title_ratings_sort.close()
#telos gia title.ratings.tsv