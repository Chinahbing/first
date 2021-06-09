import numpy
import json
from flask import Flask, app, jsonify, Request, Response

app = Flask(__name__)

def dict():
    url = "www.baidu.com"
    path = "video"
    data = {}
    data['url'] = url
    data['path'] = path
    print(type(data))
    print(data)
    data1 = json.dumps(data)
    print (type(data1))
    print(data1)
    ls = []
    ls.append(data)
    ls.append(data)
    ls.append(data1)
    print(type(ls))
    print(ls)


def list():
    ls = []
    ls.append('baidu')
    ls.append('huiwei')
    ls.append('Google')
    print(type(ls))
    print(ls)

if __name__ == '__main__':
    dict()
    list()