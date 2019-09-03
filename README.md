# Smile Detector

笑容检测器

## 使用

### Web API 服务（依赖于 Flask ）

启动 Flask Server

```
# windows command line
set FLASK_APP=main.py
# linux
export FLASK_APP=main.py
flask run
```

发送 HTTP 请求

```
POST localhost:5000/face/smile

Param name: image
Param type: [image object]
Response type: string
Response example: [[100, 100, 100, 100]]
```

## 预览效果

图片识别目录为 `images`

启动测试脚本

```
python test.py
```

## 缺陷

+ 无法准确识别面部区域（Gakki 的脸无法识别）

+ 无法准确识别笑容区域（小男孩、女人照片）

## 参阅

https://docs.opencv.org/3.4.1/d7/d8b/tutorial_py_face_detection.html

## TODO

> just for fun~

+ [ ] 检测并识别出 Gakki 的脸和笑容