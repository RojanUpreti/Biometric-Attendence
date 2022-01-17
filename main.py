from cgitb import text
from tkinter import *
from PIL import Image, ImageTk
from student import Student
import webbrowser
from train import Train
from face import Face_Reco
from atte import Attendence
from time import strftime
from datetime import datetime


class FaceRecog:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1300x650")
        self.root.title("Face Recognition System")

        
        # BG
        img3=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/bg.jpg")
        img3=img3.resize((1530,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0, y=170, width=1530, height=550)


        #title
        title=Label(self.root, text="BIOMETRIC ATTENDENCE", font=("bolditalic",int(66.8),"bold"), bg="lavender", fg="purple")
        title.place(x=0, y=0, width=1340, height=110)

        title=Label(self.root, text="With FACE-RECOGNITION", font=("times new roman",50,"bold"), bg="azure", fg="purple")
        title.place(x=0, y=110, width=1340, height=85)

        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,text)
        lbl=Label(title,font=("times new roman",20,"bold"),background='azure',foreground='blue')
        lbl.place(x=1100,y=0,width=220,height=80)
        time()



        # Student Details
        img4=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/student.jpg")
        img4=img4.resize((230,160),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photoimg4, command=self.student_details,cursor="hand2")
        b1.place(x=200,y=50,width=250,height=180)
       

        b1_1=Button(bg_img,text="STUDENT INFO",command=self.student_details,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=200,y=230, width=250, height=40)


        #Face Recog
        img5=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/facerecog.jpg")
        img5=img5.resize((230,160),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=50,width=250,height=180)

        b1_1=Button(bg_img,text="FACE RECOGNITION",command=self.face_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=500,y=230, width=250, height=40)



        #attendence
        img6=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/attendence.jpg")
        img6=img6.resize((230,160),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence_data)
        b1.place(x=800,y=50,width=250,height=180)

        b1_1=Button(bg_img,text="ATTENDENCE",command=self.attendence_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=800,y=230, width=250, height=40)



        #train
        img7=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/train.jpg")
        img7=img7.resize((230,160),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=290,width=250,height=180)
      

        b1_1=Button(bg_img,text="TRAIN FACE",command=self.train_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=200,y=470, width=250, height=40)



        # photos
        img8=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/photo2.jpg")
        img8=img8.resize((230,160),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=290,width=250,height=180)

        b1_1=Button(bg_img,text="PHOTOS",command=self.open_img,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=500,y=470, width=250, height=40)


        # exit
        img9=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/quit.webp")
        img9=img9.resize((230,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=800,y=290,width=250,height=180)

        b1_1=Button(bg_img,text="EXIT",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=800,y=470, width=250, height=40)

  

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def open_img(self):
        webbrowser.open("croppedfaces")

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Reco(self.new_window)

    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)




if __name__=="__main__":
    root=Tk()
    obj=FaceRecog(root)
    root.mainloop()