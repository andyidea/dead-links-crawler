import urllib

class URLOpener():
  def __init__(self,url):
    self.url = url
    self.response = None
    self.valid = False
    try:
      self.response = urllib.urlopen(self.url)
      if self.response.code == 200 :
        print self.response.geturl()
        self.valid = True
    except:
      print "Unable to find URL"

  def get_content(self):
    return self.response.read()

  def is_valid(self):
    return self.valid
