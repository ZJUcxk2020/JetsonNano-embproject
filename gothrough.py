import os
import cv2

def getFileList(dir, Filelist, ext=None):
    """
    获取文件夹及其子文件夹中文件列表
    输入 dir：文件夹根目录
    输入 ext: 扩展名
    返回： 文件路径列表
    """
    newDir = dir
    if os.path.isfile(dir):
        if ext is None:
            Filelist.append(dir)
        else:
            if ext in dir[-3:]: #jpg为-3/py为-2
                Filelist.append(dir)

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            getFileList(newDir, Filelist, ext)
    return Filelist


# org_img_folder = r'./pictures/'

# # 检索文件
# imglist = getFileList(org_img_folder, [], 'jpg')
# print('本次执行检索到 ' + str(len(imglist)) + ' 个jpg文件\n')


# for imgpath in imglist:
#     imgname = os.path.splitext(os.path.basename(imgpath))[0]
#     print(imgpath)
#     img = cv2.imread(imgpath, cv2.IMREAD_COLOR)
#     cv2.imshow("img",img)
#     cv2.waitKey(0)
