#-*-coding: utf-8 -*-
import urllib2

def comic(pageNum):
	response =urllib2.urlopen('http://comic.naver.com/webtoon/list.nhn?titleId=471283&page=%d'%(pageNum))
	html=response.read().split('<td class="title">')
	print html[1]
	for data in html[1:]:
		print data.split('</a>')[0].split(')">')[1]

for i in range(1,10):
	comic(i)