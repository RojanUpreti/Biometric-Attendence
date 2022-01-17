from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.font import BOLD
from tkinter import messagebox
import mysql.connector
import cv2 as cv
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1320x650")
        self.root.title("Train Data")

        title_lbl=Label(self.root, text="Train Dataset",font=("times new roman",35,"bold"),bg="white",fg="purple")
        title_lbl.place(x=0,y=0, width=1320, height=80)

        #top left img
        img=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/1.jpg")
        img=img.resize((440,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=80,width=430,height=200)


        # top med img
        img1=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/2.jpg")
        img1=img1.resize((440,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=440,y=80,width=430,height=200)


        # top right img
        img2=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/3.jpg")
        img2=img2.resize((440,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=880,y=80,width=430,height=200)



        b1_1=Button(self.root,text="TRAIN IMAGES",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=0,y=280, width=1308, height=80)

        img_btm=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/train.png")
        img_btm=img_btm.resize((1308,340),Image.ANTIALIAS)
        self.imgbtm=ImageTk.PhotoImage(img_btm)
        f_lbl=Label(self.root,image=self.imgbtm)
        f_lbl.place(x=0,y=360,width=1308,height=340)




    def train_classifier(self):
        data_dir=("croppedfaces")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert("L")
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv.imshow("Training",imageNp)
            cv.waitKey(1)==13

        ids=np.array(ids)
        # print(ids)

        #====training the classifier and saving in model==
        clf=cv.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv.destroyAllWindows()
        messagebox.showinfo("Result","Training ImageData Completed!!")







if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()

