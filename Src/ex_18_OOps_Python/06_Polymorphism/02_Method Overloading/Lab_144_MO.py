class Browser:

    def make_http_request(self,url):
        print("Let's make a http request without authentication",url)

    def make_http_request(self,url,auth=None):
        print("Let's make a http request with authentication",url,auth)

t=Browser()
t.make_http_request("http://www.python.org","admin")




