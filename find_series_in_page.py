from bs4 import BeautifulSoup
import opener
import re




def i_have_gotten_series_name(url,name):
	pass
	




def i_have_gotten_page_number(url):
	
	data=opener.fetch(url)['data']
	soup=BeautifulSoup(data)
	l=soup.find_all('a')
	reg=re.compile(r'.*/watch-\d+-(.*)')
	for i in l:
		if not i.has_key('href'):
			continue;
		if not i.has_key('title'):
			continue;
		link =i.get('href')
		m=reg.match(link)
		if m:
			series_name=i.get('title')
			series_link="http://www.1channel.ch"+m.group(0)
			print series_name,series_link
			#~ got series name and series link


def get_page_count_and_go_deeper(url):
	data=opener.fetch(url)['data']
	soup=BeautifulSoup(data)
	l=soup.select('.pagination > a ')
	ref = l[len(l)-1]['href']
	reg=re.compile(r'.*?page=(\d+).*?')
	page_count=1
	m=reg.match(ref)
	if m:
		page_count=int(m.group(1))
	
	for i in range(1,page_count+1):
		new_url=url+"&page="+str(i)
		#~ i have got the new url and now i have to go through all the urls
		print new_url
	


def tester(url):
	pass
	
	
	
	

if __name__=='__main__':
	
	#~ i_have_gotten_page_number('http://www.1channel.ch/?letter=123&tv&page=1')
	get_page_count_and_go_deeper('http://www.1channel.ch/?letter=123&tv')
	
	
