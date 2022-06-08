import json
import numpy
import face_recognition
from flask import Flask,request,jsonify,render_template
import requests
import gothrough
import os
import cv2
import startupgui
import matplotlib.pyplot as plt
from math import *
import threading
import readfile
attend_people=0
delay_people=0
early_people=0

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

print("The number of the students is %d:" %len(known_face_names))
people_cnt=len(known_face_names)
telephonedic = readfile.readtelephone()

def run_show():
    #print("I'm here")
    plt.ion() 
    t = [0]
    mattend = [0]
    mlate = [0]
    mearly = [0]
    index=0
    while True:
        t_now = index*5
        t.append(t_now)
        mattend.append(attend_people/people_cnt)
        mlate.append(delay_people/people_cnt)
        mearly.append(early_people/people_cnt)
        plt.subplot(1,3,1)
        plt.plot(t,mattend,'-r')
        plt.subplot(1,3,2)
        plt.plot(t,mlate,'-r')
        plt.subplot(1,3,3)
        plt.plot(t,mearly,'-r')
        plt.pause(5)
        index+=1


classname,starttime,delay,length,signin,signout,signoutdur = startupgui.setupguiwindow()


app = Flask("server") # 创建一个Flask实例
@app.route('/',methods=['GET','POST']) # 设置路由地址，即网页地址，也称为URL

def ret_pic_encoding(): # URL的处理函数
    json_data={"pic_encodings":known_face_encodings,"pic_names":known_face_names,
    "class_name":classname,"start_time":starttime,"delay_time":delay,"class_length":length,
    "signin_time":signin,"signout_time":signout,"signout_duration":signoutdur,
    "telephonedic":telephonedic}
    r = requests.post("http://192.168.137.7:5000/get_encoding", json=json_data,timeout=3)
    print(r.text)
    return "success"

@app.route('/get_data',methods=['GET','POST'])

def getdata():
    global attend_people
    global delay_people
    global early_people
    values = request.get_json()
    attend_people=values["attend_people"]
    delay_people=values["late_people"]
    early_people=values["early_people"]
    return "getdata success"


def run_flask():
    app.run(host='0.0.0.0',debug=False, use_reloader=False)


t1=threading.Thread(target=run_flask)
t1.start()
run_show()
