import urllib
import cookielib
import urllib2


class NomaBooker():

    def __init__(self):
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        self.opener.addheaders = [
            ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'),
            ('Host', 'dinnerbooking.com'),
            ('Origin', 'http://dinnerbooking.com'),
            ('Referer', 'http://dinnerbooking.com/login'),
            ('Accept', '*/*')
        ]
        urllib2.install_opener(self.opener)

    @staticmethod
    def login_dinnerbooking(email, password):

        login_url = "http://dinnerbooking.com/login"

        payload = {
            'email': email,
            'password': password,
            'remember_me': 0
        }

        data = urllib.urlencode(payload)
        req = urllib2.Request(login_url, data)
        response = urllib2.urlopen(req)

        return response.read()