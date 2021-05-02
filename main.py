import os
import paddlehub as hub
from PIL import Image
import cv2
from flask import Flask, render_template, request, redirect, Response, send_file
from werkzeug.utils import secure_filename
import photo
app = Flask(__name__)


model = hub.Module(name='deoldify')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index_new')
def index_new():
    return render_template("index_new.html")


@app.route('/upload', methods=['post'])
def up_photo():
    f = request.files['image']
    basepath = os.path.dirname(__file__)
    path = os.path.join(basepath, 'images', secure_filename(f.filename))
    f.save(path)
    img = cv2.imread(path)
    cv2.imwrite(os.path.join(basepath, 'images', 'old.png'), img)
    photo.delete(path)
    input_img = './images/old.png'
    print(photo.photo(model, input_img))
    return render_template("index_new.html")


@app.route('/images/<imageid>', methods=['GET'])
def images(imageid):
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(basedir, 'images', imageid)
    return send_file(file_path)


if __name__ == '__main__':
    app.run()
