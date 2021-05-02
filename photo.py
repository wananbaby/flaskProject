import os
import paddlehub as hub
from PIL import Image


def delete(path):
    os.remove(path)


def photo(model, path):
    result = model.predict(path)
    output_img = result[1]
    img = Image.open(output_img)
    img.save('./images/new.png')
    path1 = './output/DeOldify/old.png'
    os.remove(path1)
    return '转换完成'

