from bs4 import BeautifulSoup
import urllib2
import sys

def main():
	response = urllib2.urlopen('https://www.google.com/finance/historical?q=INDEXSP%3A.INX&ei=xXojV6HyDoKB0gSQra6wCA&start='+sys.argv[1]+'&num=30')
	print sys.argv[1]
	url = 'https://www.google.com/finance/historical?q=INDEXSP%3A.INX&ei=xXojV6HyDoKB0gSQra6wCA&start='+sys.argv[1]+'&num=30'
	print url
	html = response.read()
	soup = BeautifulSoup(html,'html.parser')

	tabulka = soup.find("table", {"class" : "gf-table historical_price"})

	records = [] # store all of the records in this list
	for row in tabulka.findAll('tr'):
	    col = row.findAll('td')
	    record = '%s;%s' % (col[0],col[1])
	    records.append(record)
	filename = 'output'+sys.argv[1]+'.txt'
	fl = open(filename,'w')
	line = ';'.join(records)
	fl.write(line + u'\r\n')
	fl.close()

if __name__ == '__main__':
		main()
