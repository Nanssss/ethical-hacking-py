#!/usr/bin/python3

#ce programme aide a nous rendre plus anonyme sur des sites http

#site qui montre les headers : http://httpbin.org/headers

import requests

myheaders = {'User-Agent' : 'Iphone 6', 'Host' : 'google.com'}
r = requests.get('http://httpbin.org/headers', headers=myheaders)
print(r.text)
