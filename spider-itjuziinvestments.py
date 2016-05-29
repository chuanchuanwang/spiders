import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
from bs4 import BeautifulSoup
import datetime

starttime = datetime.datetime.now()

# 记得确认文件路径和爬多少页
# 记得确认文件路径和爬多少页
# 记得确认文件路径和爬多少页

# 输出文件路径
path = '/Users/admin/Documents/Python/ITjuzi_data/'+str(datetime.date.today())+'.csv'

# 爬多少个页
pagenumbers = 1300


# 清空文件,初始化首行
f= file(path,'w')
f.write('时间,备注,公司,领域,省市,轮次,融资额,投资方'+'\n')
f.close()



count = 1
# 处理第一个网页
#for count in range(1,2):

	# 对每张网页以追加方式打开和关闭，万一错误中段，已分析记录可以保存
while (count <= pagenumbers):

	f= file(path,'a')

	url = 'https://www.itjuzi.com/investevents?page=' + str(count)

	time_consuming = datetime.datetime.now()-starttime

	print '用时 ' + str(time_consuming) + ' ' + url + '解析中... ' + '还有' + str(time_consuming/count * (pagenumbers - count ))

	request = urllib2.Request(url)
	request.add_header('User-Agent','fake-client')
	html = urllib2.urlopen(request).read()
	
	soup = BeautifulSoup(html,'html.parser')
	listpart = soup.find_all('ul',class_='list-main-eventset')[1]

	ipart=listpart.find_all('i')

	for x in range(10):
		for y in ipart[6*x:6*x+5]:
			f.write(y.get_text(',',strip=True) + ',')
		f.write(ipart[6*x+5].get_text('|',strip=True) + '\n')

	f.close()

	count = count +1






