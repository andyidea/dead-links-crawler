import urllib

class URLOpener():
  def __init__(self,url):
    self.url = url
    self.response = None
    self.valid = False
    try:
      print "open url " + self.url
      self.response = urllib.urlopen(self.url)
      print self.response.code
      if self.response.code == 200 :
        self.valid = True
    except:
      print "Unable to find URL"

  def get_content(self):
    return self.response.read()

  def is_valid(self):
    return self.valid

  def get_url(self):
    return self.response.geturl()
