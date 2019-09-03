from flask import Flask
from flask import request
import time
import cv2 as cv

app = Flask(__name__)
upload_dir = 'images/'

# 加载物体检测分类器
face_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
smile_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_smile.xml')


@app.route("/face/smile", methods=["POST"])
def smile_detector():
    # 接收客户端图片
    f = request.files['image']
    suffix = f.filename[f.filename.rindex('.'):]
    image_new_path = upload_dir + str(time.time()) + suffix
    f.save(image_new_path)

    # 读取待检测图片
    img = cv.imread(image_new_path)

    # 将图片转换成灰度模式
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # 获取识别的面部区域列表
    faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)

    # 获取面部矩形区域信息（起点 xy 轴坐标、长、宽）
    for (x, y, w, h) in faces:
        # 在灰度模式的图片上划分出该面部区域
        roi_face_gray = img_gray[y: y + h, x: x + w]
        # 在该区域内，获取识别的笑脸区域列表
        smiles = smile_cascade.detectMultiScale(roi_face_gray, 1.78, 10)

    return str(smiles)
