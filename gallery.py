import os
from flask import Flask , send_from_directory,render_template

app = Flask (__name__)
@app.route('/',methods=['GET','POST'])

def index ():
    return  render_template('index.html')

@app.route('/images/<path:path>')
def index2(path):
    return send_from_directory('static/images',path)

@app.route('/css/<string:stylesheet>')
def rout_css(stylesheet):
    return send_from_directory('static/css', stylesheet)

if __name__ == '__main__':
    app.run(debug=True)
