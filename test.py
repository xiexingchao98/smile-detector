import cv2 as cv
import os

images_dir = "images/"


def detect(filename):
    # 读取待检测图片
    img = cv.imread(images_dir + filename)

    # 将图片转换成灰度模式
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # 获取识别的面部区域列表，默认检测参数（不准确）
    faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)

    # 获取面部矩形区域信息（起点 xy 轴坐标、长、宽）
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # 在灰度模式的图片上划分出该面部区域
        roi_face_gray = img_gray[y: y + h, x: x + w]
        roi_img = img[y: y + h, x: x + w]
        # 在该区域内，获取识别的笑脸区域列表，默认检测参数（不准确）
        smiles = smile_cascade.detectMultiScale(roi_face_gray, 1.78, 10)
        for (sx, sy, sw, sh) in smiles:
            cv.rectangle(roi_img, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)

    cv.imshow(filename, img)
    cv.waitKey(0)


files = os.listdir("images")

# 加载物体检测分类器
face_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
smile_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_smile.xml')

for f in files:
    detect(f)
