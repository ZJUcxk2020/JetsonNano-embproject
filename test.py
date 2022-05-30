import json
import numpy
import face_recognition
from flask import Flask
import requests
import gothrough
import os
known_face_encodings = []
known_face_names = []
path = r'./pictures/'
#print(path)
jpglist = gothrough.getFileList(path,[],"jpg")

for imgpath in jpglist:
    image = face_recognition.load_image_file(imgpath)
    face_encodings = face_recognition.face_encodings(image)[0]
    #print(face_encodings)
    known_face_encodings.append(face_encodings.tolist())
    known_face_names.append(os.path.basename(imgpath)[:-4])

print(len(known_face_names))
app = Flask("server") # 创建一个Flask实例
@app.route('/',methods=['GET','POST']) # 设置路由地址，即网页地址，也称为URL

def ret_pic_encoding(): # URL的处理函数
    json_data={"pic_encodings":known_face_encodings,"pic_names":known_face_names}
    r = requests.post("http://192.168.137.7:5000/get_encoding", json=json_data,timeout=3)
    print(r.text)
    return "suscess"

app.run(host='0.0.0.0',debug=False, use_reloader=False)
