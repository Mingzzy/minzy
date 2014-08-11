#-*-coding: utf-8 -*-
import urllib2

def news(pageNum):
	response =urllib2.urlopen('http://trendinsight.biz/archives/category/design/page/%d'%(pageNum))
	html=response.read().split('rel="bookmark">')
	for data in html[1:]:
		print data.split('</a></h2')[0]

for i in range(1,10):
	news(i)