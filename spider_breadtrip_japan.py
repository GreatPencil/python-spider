#coding=utf-8
import sys
sys.path.append('/Users/RUI/PycharmProjects/spider/new_folder.py')
import new_folder
import re
import requests
import urllib
import random
from time import sleep
url=requests.get('http://web.breadtrip.com/trips/2387300837/')
# print url.text
title=re.search('<h2 title="(.*?)">',url.content,re.S).group(1)
# print title
new_folder.mkdir('/Users/RUI/Desktop/python/spider/%s'%(title))
pictuer_urls=re.findall('data-photo="(.*?)"',url.content,re.S)
sum_pic = len(pictuer_urls)
i=0
print len(pictuer_urls)
for pictuer_url in pictuer_urls:
	i += 1
	if pictuer_url =='':
		pass
	else:
		path='/Users/RUI/Desktop/python/spider/%s'%(title)+str(i)+'.jpg'
		urllib.urlretrieve(pictuer_url,path)
		print '你下载了'+str(i)+'张图片'
		sleep(random.uniform(0.5,1))












