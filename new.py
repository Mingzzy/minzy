import urllib

from bs4 import BeautifulSoup

htmltext = urllib.urlopen("http://pgr21.com/pb/pb.php?id=freedom").read()

soup = BeautifulSoup(htmltext, from_encoding="utf-8")

authors = []

for tag in soup.select(".tdname"):
	authors.append(tag.get_text())

for author in authors:
	print author.encode('utf-8')

#my url
htmltext=urllib.urlopen("http://trendinsight.biz/archives/category/design/page/2").read()

soups=BeautifulSoup(htmltext,from_encoding="utf-8")

authorss=[]

for tags in soups.select(".loop .hentry a:hover"):
	authorss.append(tags.get_text())

for name in authorss:
	print name.encode('utf-8')