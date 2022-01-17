from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.font import BOLD
from tkinter import messagebox
import mysql.connector
import cv2 as cv
import os
import numpy as np
from time import strftime
from datetime import datetime



class Face_Reco:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1320x650")
        self.root.title("Train Data")

        title_lbl=Label(self.root, text="FACE-RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0, width=1320, height=80)

        img=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/face_recog.webp")
        img=img.resize((610,700),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=80,width=610,height=628)

        img=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/face-recog.jpg")
        img=img.resize((680,700),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img)
        f_lbl1=Label(self.root,image=self.photoimg1)
        f_lbl1.place(x=610,y=80,width=680,height=628)


        b1_1=Button(self.root,text="FACE-RECOGNITION",command=self.f_recog,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=688,y=598, width=220, height=58)


    #==attendence====
    def mark_attendence(self,i,r,n,d):
        with open('attendence.csv',"r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d\%m\%Y")
                dfstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dfstring},{d1},Present")



    #====FR====
    def f_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost", username="root",password="0422K10Jrojan88/?s",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Roll_no= "+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Course from student where Roll_no= "+str(id))
                c=my_cursor.fetchone()
                c="+".join(c)

                my_cursor.execute("select Level from student where Roll_no= "+str(id))
                l=my_cursor.fetchone()
                l="+".join(l)

                my_cursor.execute("select Phone_no from student where Roll_no= "+str(id))
                p=my_cursor.fetchone()
                p="+".join(p)

                if confidence>80:
                    cv.putText(img,f"Name:{n}",(x,y-80),cv.FONT_ITALIC,0.8,(0,0,255),3)
                    cv.putText(img,f"Level:{l}",(x,y-55),cv.FONT_ITALIC,0.8,(0,0,255),3)
                    cv.putText(img,f"Course:{c}",(x,y-30),cv.FONT_ITALIC,0.8,(0,0,255),3)
                    cv.putText(img,f"Roll_no:{p}",(x,y-5),cv.FONT_ITALIC,0.8,(0,0,255),3)
                else:
                    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv.putText(img,"Unknown Face",(x,y-5),cv.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv.CascadeClassifier("haarcascade_profileface_default.xml")
        clf=cv.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv.imshow("Welcome to Face Recognition",img)
            if cv.waitKey(1)==13:
                break
        video_cap.release()
        cv.destroyAllWindows()


if __name__=="__main__":
    root=Tk()
    obj=Face_Reco(root)
    root.mainloop()

