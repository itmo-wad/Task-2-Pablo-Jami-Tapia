import os
from flask import Flask, render_template, send_from_directory
from flask import url_for, make_response

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')
    

@app.route('/images/<string:image>')
def rout_img(image):
    return send_from_directory(os.path.join(app.root_path, 'static', 'images'),
                               image)


@app.route('/css/<string:style>')
def rout_css(style):
    return send_from_directory(os.path.join(app.root_path, 'static', 'css'),
                               style)

if __name__ == '__main__':
    app.run(debug=True)