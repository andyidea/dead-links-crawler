from HTMLParser import HTMLParser
import urllib

class LinkParser(HTMLParser):
 	def reset(self):
 		HTMLParser.reset(self)
 		self.hrefs = []

 	def handle_starttag(self, tag, attrs):
 		href = [v for k,v in attrs if k.lower() == 'src']
 		if href: self.hrefs.extend(href)
 		href = [v for k,v in attrs if k.lower() == 'href']
 		if href: self.hrefs.extend(href)

class HTMLDoc():
  def __init__(self, html_content):
    self.html_content = html_content

  def get_links(self):
    links = None
    try:
      parser = LinkParser()
      parser.feed(self.html_content)
      parser.close()
      links = [ href for href in parser.hrefs] if parser.hrefs else None
    except :
      print "Unable to parse URL data"
    return links
