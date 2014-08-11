#-*- coding:utf8 -*-
import urllib

from bs4 import BeautifulSoup

# my url
htmltext = urllib.urlopen("http://www.ppomppu.co.kr/recent_main_article.php?type=event").read()

soups = BeautifulSoup(htmltext)

titles = []
for tags in soups.select("span.first_list"):
    titles.append(tags.get_text())

for title in titles:
    print title.encode('utf-8','ignore')
