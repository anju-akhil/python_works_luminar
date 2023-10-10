from json import load
path="C:\\Users\\HP\\Desktop\\pythonworks\\movies\\mdb.json"
with open(path,encoding="utf-8") as f:
    movies=load(f)

#----------total number of movies----------
#print(len(movies))

#----------------print all movie name-----------
movie_name=[m.get("title")for m in movies]
#print(movie_name)

#---------------print movie title released in 2005----------
movie_title=[m.get("title")for m in movies if m.get("year")=="2005"]
#print(movie_title)

#------------print movie title whose genre="comedy"
movie_filter=[m.get("title")for m in movies if "Comedy" in m.get("genres")]
#print(movie_filter)

#---------------------lengthy movie title-------------------
runtime_movie=max(movies,key=lambda m:int(m.get("runtime")))
#print(runtime_movie)

#-------------------print all genres--------------------
genre_name={g for m in movies for g in m.get("genres")}
#print(genre_name)

#-----------------comedy movies released in 2015---------------
c_movies=[m.get("title")for m in movies if"Comedy" in m.get("genres")and m.get("year")=="2015"]
#print(c_movies)

#--------------
wc={}
for m in movies:
    year=m.get("year")
    if year in wc:
        wc[year]+=1
    else:
        wc[year]=1
print(max(wc,key=lambda m:wc.get(m)))