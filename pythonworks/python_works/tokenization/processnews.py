f_news=open("C:\\Users\\HP\\Desktop\\pythonworks\\tokenization\\news.txt")
f_stop=open("C:\\Users\\HP\\Desktop\\pythonworks\\tokenization\\stopwords.txt")
stop_words={line.rstrip("\n") for line in f_stop }
news_set=set()
for line in f_news:
    words=line.split()
    for w in words:
        news_set.add(w)
print(news_set.difference(stop_words))