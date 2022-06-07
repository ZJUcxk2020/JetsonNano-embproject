import PySimpleGUI as sg
import datetime

def setupguiwindow():
    sg.theme('DarkAmber')   # 设置当前主题
    layout = [  [sg.Text('Enter the name of the class or meeting'), sg.InputText()],
            [sg.Text("All time Format:Year-Month-Day Hour:Minute")],
            [sg.Text('Class starttime'),sg.InputText(),sg.Text('Length of the class'),sg.InputText()],    
            [sg.Text('Acceptable Delay time'),sg.InputText()],
            [sg.Text('Sign in starttime:'),sg.InputText()],
            [sg.Text('Sign out starttime:'),sg.InputText(),sg.Text('Duaration'),sg.InputText()],
            [sg.Button('Ok')] ]
    window = sg.Window('Setup', layout)
    while True:
        event, values = window.read()
        if event in (None,'Ok'):   # 如果用户关闭窗口或点击`Cancel`
            break

#print(values)
    classname = values[0]
    starttime = values[1]
    delay = int(values[2])
    length = int(values[3])
    signin = values[4]
    signout = values[5]
    signoutdur = int(values[6])
    window.close()
    return classname,starttime,delay,length,signin,signout,signoutdur


#a,b,c,d,e,f,g = setupguiwindow()
#print(a,b,c,d,e,f,g)
