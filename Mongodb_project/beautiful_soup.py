from bs4 import BeautifulSoup
import urllib2

webpage = urllib2.urlopen('http://en.wikipedia.org/wiki/Main_Page')
soup = BeautifulSoup(webpage)
for anchor in soup.find_all('a'):
    print(anchor.get('href', '/'))
    
    
# Beautiful Soup is pyhon package for parsing HTML and XML documents 
# including having malformed markup 
# it creates a parse tree for arsed pages that can be used to extract data from HTML which is useful
# for web scraping
