import os
from flask import Flask, request, render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("downLoad.html")


@app.route('/downLoad', methods=['POST', 'GET'])
def downLoad():
    url = request.form.get('video_url')
    path = request.form.get('video_path')
    cmd = "you-get -o " + path + " " + url
    print(cmd)
    if cmd:
        os.system(cmd)
    res = {'msg': '成功'}
    return res

if __name__ == "__main__":
     app.run(port=2020,host="0.0.0.0",debug=True)