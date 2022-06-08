def readtelephone():
    f = open("phonenumber","r",encoding="utf-8")
    data = f.readline()
    name = []
    tele = []
    while data:
        info = data.split()
        name.append(info[0])
        tele.append(info[1])
        data = f.readline()
    #print(name)
    #print(tele)
    dic = dict(zip(name,tele))
    #print(dic)
    return dic
