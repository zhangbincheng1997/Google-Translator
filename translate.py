#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import requests
from tk import Py4Js

from urllib.parse import urlencode


class google_translate():

    def __init__(self, content):
        self.content = content
        js = Py4Js()
        tk = js.getTk(self.content)
        self.tk = tk

    def translate(self):
        data = {
            "client": "t",
            "sl": "en",
            "tl": "zh-CN",
            "hl": "zh-CN",
            "dt": "at",
            "dt": "bd",
            "dt": "ex",
            "dt": "ld",
            "dt": "md",
            "dt": "qca",
            "dt": "rw",
            "dt": "rm",
            "dt": "ss",
            "dt": "t",
            "ie": "UTF-8",
            "oe": "UTF-8",
            "source": "bh",
            "ssel": "0",
            "tsel": "0",
            "kc": "1",
            "tk": self.tk,
            "q": self.content,
        }
        params = urlencode(data)
        base = 'https://translate.google.cn/translate_a/single'
        url = base + '?' + params
        print(url)
        head = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}

        string = requests.get(url, headers=head).text
        return re.findall('.*?"(.*?)"', string, re.S)[0]


if __name__ == '__main__':
    gt = google_translate('hello, world')
    ch = gt.translate()
    print(ch)
