# https://pypi.org/project/image-quality/
import io

import imquality.brisque as brisque
import PIL.Image
from pathlib import Path
from PIL import Image
import cv2
from django.core.files.storage import FileSystemStorage
import pickle
import base64
import numpy as np

def image_quality(image_path):
    # path = r"C:\DIT\FYP\102flowers\sample-low-quality\blurry.jpg"
    begin = cv2.os.getcwd()
    image_root = begin.replace("\\", "/")

    path = image_root + image_path

    image = PIL.Image.open(path)
    # image.show()
    result = brisque.score(image)

    print(result)
    print("this is the path")
    print(type(path))
    print(path)
    # lower the number  = less pixelated
    # however, the blurry images do not work in this
    return result



# Take in base64 string and return cv image
# https://stackoverflow.com/questions/16214190/how-to-convert-base64-string-to-image/16214280
def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    image = Image.open(io.BytesIO(imgdata))

    jpg = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

    print(type(jpg))
    # cv2.imwrite('color_img.jpg', jpg)
    # cv2.imshow("image", jpg);

    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()