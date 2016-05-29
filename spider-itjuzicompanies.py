import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import datetime

from bs4 import BeautifulSoup
import urllib2

starttime = datetime.datetime.now()

# set path of the file to save
where_to_save_company_list = '/Users/admin/Documents/Python/ITjuzi_data/companies'

path = where_to_save_company_list + str(datetime.date.today()) + '.csv'
f=file(path,'w')
f.write('name,date,field,location,status,discription,link\n')
f.close()

for page in range(1,2495):

	url = 'http://www.itjuzi.com/company?page=' + str(page)

	print str(datetime.datetime.now()-starttime) + url + '...'

	request = urllib2.Request(url)
	request.add_header('User-Agent','fake-client')
	html = urllib2.urlopen(request).read()


	Soup = BeautifulSoup(html,'html.parser')

	listarea = Soup.find('ul', class_ = 'list-main-icnset').next_sibling.next_sibling

	# list out all companies' info
	companies = listarea.find_all('li')


	for num in range(10):

		record = []

		companyinfolist = companies[num].find_all('i')

		span = companyinfolist[1].find_all('span')

		# name
		record.append(span[0].get_text(strip=True))
		# date
		record.append(companyinfolist[2].get_text(strip=True))
		# type
		record.append(span[2].get_text(strip=True))
		# location
		record.append(span[3].get_text(strip=True))
		# finacial status
		record.append(companyinfolist[3].get_text(strip=True))
		# discription
		record.append('"'+span[1].get_text(strip=True)+'"')
		# link of the company
		record.append(companyinfolist[0].a.attrs['href'])

		f=file(path,'a')

		for i in record:
			f.write(i + ',')

		f.write('\n')
		f.close()

print '\n\n\nDone\n\n\n'




