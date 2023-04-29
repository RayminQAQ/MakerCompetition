import tkinter.ttk
from tkinter import *
from PIL import Image, ImageTk
import cv2
import time
from tkinter import filedialog
import os

# NOTE: progressbar value
progressbar_weight = 100
progressbar_space = 0.8
max_weight = 200

# Picture for each window
pic_compress = Image.open('CompressPic.png')
pic_info = Image.open('maker_URL.png')

# window for callback design
class basedesk():
    def __init__(self, master):
        self.root = master
        self.root.config(bg="#E0E0E0")  # UNSURE
        self.root.resizable(0, 0) # 固定視窗伸縮
        self.root.title("Maker：WALL-E")

        # call MainWindow
        mainWindow(self.root)

# MainWindow
class mainWindow():
    def __init__(self, master):
        self.master = master

        # 以下是mainWindow介面
        self.master.geometry("450x200")
        self.master.resizable(0, 0)
        self.mainWindow = PanedWindow(self.master, orient="vertical")
        self.mainWindow.pack(fill="both", expand=0)

        # 新增物件banner 進 Frame
        banner = Label(self.mainWindow, text=" WALL-E ", bg="white", bd=20, font=("Arial", 25))
        self.mainWindow.add(banner, height=100)

        # frame1 & set info
        frame1 = Frame(self.mainWindow, height=100)
        self.mainWindow.add(frame1)

        label_weigth = Label(frame1, text="垃圾重量：  ")
        label_weigth.grid(row=0, column=0)
        Label(frame1, text=str(progressbar_weight)+" kg").grid(row=0, column=2, padx=5,pady=5)

        # label_weigth 加入進度條 & 數字顯示
        progressbar = tkinter.ttk.Progressbar(frame1, length=130)
        progressbar['maximum'] = max_weight
        progressbar['value'] = progressbar_weight
        progressbar.grid(row=0, column=1)

        label_space = Label(frame1, text="垃圾箱容量：  ")
        label_space.grid(row=1, column=0, pady=5)
        Label(frame1, text= str(progressbar_space * 100) + " %").grid(row=1, column=2, padx=5, pady=5)

        # label_space 加入進度條 & 數字顯示
        progressbar = tkinter.ttk.Progressbar(frame1, length=130)
        progressbar['maximum'] = 100
        progressbar['value'] = progressbar_space * 100
        progressbar.grid(row=1, column=1)

        # 新增物件button 進 Frame
        hbutton = PanedWindow(orient='horizontal')
        btn_compress = Button(hbutton, text="Compress", height=20, width=20, command=self.clickCompress)
        btn_game = Button(hbutton, text="Camera", height=20, width=20, command=self.clickCamera)
        btn_moreinfo = Button(hbutton, text="More Information", height=20, width=20, command=self.clickInfo)

        hbutton.add(btn_compress)
        hbutton.add(btn_game)
        hbutton.add(btn_moreinfo)

        self.mainWindow.add(hbutton, stretch="never", height=30)

    def clickCompress(self):
        self.mainWindow.destroy()
        CompressWindow(self.master)

    def clickCamera(self):
        self.mainWindow.destroy()
        CameraWindow(self.master)

    def clickInfo(self):
        self.mainWindow.destroy()
        InfoWindow(self.master)

class CompressWindow():
    def __init__(self, master):
        self.master = master

        # 以下是 Compress 介面
        self.master.geometry("450x200")  # 控制視窗大小
        self.master.resizable(1, 1)  # 控制視窗是否可以伸縮
        self.CompressWindow = Frame(self.master)
        self.CompressWindow.pack()

        # add Compress Pic
        global tk_img   # IMPORTANT: PYTHON 的垃圾回收繼志會把它回收，所以要用glonal
        tk_img = ImageTk.PhotoImage(pic_compress)  # 開啟檔案，轉換為 tk 圖片物件
        label = Label(self.CompressWindow, image=tk_img)  # 在 Lable 中放入圖片
        label.pack()

        # button for get back
        btn_back = Button(self.CompressWindow, text="Go Back", command=self.back)
        btn_back.pack()

    def back(self):
        self.CompressWindow.destroy()
        mainWindow(self.master)

class CameraWindow():
    def __init__(self, master):
        self.master = master
        self.camera = cv2.VideoCapture(0) # 選擇第二隻攝影機

        # 計時器
        starttime = time.time()

        while(True):
            # 從攝影機擷取一張影像
            ret, frame = self.camera.read()

            # 顯示圖片
            cv2.imshow('frame', frame)

            # 若按下 q 鍵則離開迴圈
            if cv2.waitKey(1) & (time.time() - starttime >= 10):
                break

        # 釋放攝影機
        self.camera.release()

        # 關閉所有 OpenCV 視窗
        self.back()

    def back(self):
        # delete camera
        cv2.destroyAllWindows()

        #  return to mainWindow
        mainWindow(self.master)

class InfoWindow():
    def __init__(self, master):
        self.master = master

        # 以下是 Compress 介面
        self.master.geometry("450x200")
        self.InfoWindow = Frame(self.master)
        self.InfoWindow.pack()

        # URL Pic
        global tk_img   # IMPORTANT: PYTHON 的垃圾回收繼志會把它回收，所以要用glonal
        tk_img = ImageTk.PhotoImage(pic_info)  # 開啟檔案，轉換為 tk 圖片物件
        label = Label(self.InfoWindow, image=tk_img)  # 在 Lable 中放入圖片
        label.pack()

        # button for get back
        btn_back = Button(self.InfoWindow, text="Go Back", command=self.back)
        btn_back.pack()

    def back(self):
        self.InfoWindow.destroy()
        mainWindow(self.master)

if __name__ == "__main__":
    # Instantiating top level
    root = Tk()

    # call MainWindow
    basedesk(root)

    # Mainloop which will cause this toplevel to run infinitely
    root.mainloop()

