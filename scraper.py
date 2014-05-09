import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

url = 'http://adbnews.com/area51/contact.html'

br = mechanize.Browser()
urls = [url]
visited = [url]

while len(urls)>0:
    br.open(url)
    urls.pop(0)
    for link in br.links():
        newurl = urlparse.urljoin(link.base_url,link.url)  

        b1 = urlparse.urlparse(newurl).hostname
        b2 = urlparse.urlparse(newurl).path

        print 'http://'+b1+b2
