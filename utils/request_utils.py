import requests
from utils.decorators import request_check
from utils.config import host


class RequestUtil:

    def __init__(self):
        self.sess = requests.session()
        self.sess.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
                                          " (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57"

    @request_check
    def call(self, url, method, **kwargs):
        return self.sess.request(method, host+url, **kwargs)


req = RequestUtil()
