import sys
from crawler import Crawler
if __name__ == '__main__':
  if len(sys.argv) > 1:
    url = sys.argv[1]
    crawler = Crawler(url)
    print crawler.get_dead_urls()
  else: 
    print 'URL required'
