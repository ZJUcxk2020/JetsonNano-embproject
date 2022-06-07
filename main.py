import json
import numpy
import face_recognition
from flask import Flask
import requests
import gothrough
import os
import cv2
import startupgui
import matplotlib.pyplot as plt
from math import *
import threading
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

def show_attend():
    plt.ion() 
    t = [0]
    t_now = 0
    m = [0]
    index=0
    while True:
        t_now = index*0.1
        t.append(t_now)
        m.append(attend_people/people_cnt)
        plt.plot()
        plt.pause(0.1)
        index+=1
    
def show_delay():
    plt.ion() 
    t = [0]
    t_now = 0
    m = [0]
    index=0
    while True:
        t_now = index*0.1
        t.append(t_now)
        m.append(delay_people/people_cnt)
        plt.plot()
        plt.pause(0.1)
        index+=1

def show_early():
    plt.ion() 
    t = [0]
    t_now = 0
    m = [0]
    index=0
    while True:
        t_now = index*0.1
        t.append(t_now)
        m.append(early_people/people_cnt)
        plt.plot()
        plt.pause(0.1)
        index+=1

def run_show():
    while True:
        key=cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            show_attend()
        elif key & 0xFF ==ord('w'):
            show_delay()
        elif key & 0xFF ==ord('e'):
            show_early()



classname,starttime,delay,length,signin,signout,signoutdur = startupgui.setupguiwindow()


t1=threading.Thread(target=run_show)
app = Flask("server") # 创建一个Flask实例
@app.route('/',methods=['GET','POST']) # 设置路由地址，即网页地址，也称为URL

def ret_pic_encoding(): # URL的处理函数
    json_data={"pic_encodings":known_face_encodings,"pic_names":known_face_names,
    "class_name":classname,"start_time":starttime,"delay_time":delay,"class_length":length,
    "signin_time":signin,"signout_time":signout,"signout_duration":signoutdur}
    r = requests.post("http://192.168.137.7:5000/get_encoding", json=json_data,timeout=3)
    print(r.text)
    return "success"

@app.route('/get_data',methods=['GET','POST'])

def visualizedata():
    global attend_people
    global delay_people
    global early_people
    r = requests.get_json()
    attend_people=r["attend_people"]
    delay_people=r["late_people"]
    early_people=r["early_people"]

    
app.run(host='0.0.0.0',debug=False, use_reloader=False)
