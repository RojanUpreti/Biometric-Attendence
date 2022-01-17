from cgitb import text
from operator import delitem
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.font import BOLD
from tkinter import messagebox
import mysql.connector
import cv2 as cv
import os
import csv
from tkinter import filedialog


my_data=[]
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x650")
        self.root.title("Attendence list")

        
        self.var_attend_name=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_department=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_status=StringVar()

        img=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/student1.jpg")
        img=img.resize((440,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=430,height=170)

        img1=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/student2.jpg")
        img1=img1.resize((440,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=440,y=0,width=430,height=170)


        # top right img
        img2=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/student3.webp")
        img2=img2.resize((440,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=880,y=0,width=430,height=170)

        img3=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/bg1.jpg")
        img3=img3.resize((1530,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=170,width=1530,height=580)


        # title
        title_lbl=Label(bg_img, text="Attendence Details",font=("times new roman",35,"bold"),bg="white",fg="purple")
        title_lbl.place(x=8,y=8, width=1280, height=40)


        # main_frame
        main_frame=Frame(bg_img,bd=4)
        main_frame.place(x=8,y=56,width=1280,height=470)


        # left_frame
        lef_frame=LabelFrame(main_frame,bd=20,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        lef_frame.place(x=10,y=5,width=600,height=450)



        #img_left
        img_left=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/imgleft.jpg")
        img_left=img_left.resize((560,250),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(lef_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=560,height=200)

        # Class_information
        left_frame=LabelFrame(lef_frame,bd=4,bg="white",relief=RIDGE,text="Class Information",font=("times new roman",12,"bold"))
        left_frame.place(x=5,y=200,width=552,height=200)



        #Student_name
        stdnt_label=Label(left_frame,text="Student Name:",font=("times new roman",12,"bold"))
        stdnt_label.grid(row=0,column=0,padx=5)

        stdnt_combo=ttk.Entry(left_frame,width=16,font=("times new roman",12,"bold"))
        stdnt_combo.grid(row=0,column=1,padx=4,pady=7)

        # Roll No
        roll_label=Label(left_frame,text="Roll No:",font=("times new roman",12,"bold"))
        roll_label.grid(row=0,column=2,padx=5)
        
        roll_combo=ttk.Entry(left_frame,width=16,font=("times new roman",12,"bold"))
        roll_combo.grid(row=0,column=3,padx=2,pady=7)

        #Departmnt
        roll_label=Label(left_frame,text="Department:",font=("times new roman",12,"bold"))
        roll_label.grid(row=1,column=0,padx=5)
        
        roll_combo=ttk.Entry(left_frame,width=16,font=("times new roman",12,"bold"))
        roll_combo.grid(row=1,column=1,padx=2,pady=7)


        #date
        roll_label=Label(left_frame,text="Date:",font=("times new roman",12,"bold"))
        roll_label.grid(row=1,column=2,padx=5)
        
        roll_combo=ttk.Entry(left_frame,width=16,font=("times new roman",12,"bold"))
        roll_combo.grid(row=1,column=3,padx=2,pady=7)
        
        #tym
        roll_label=Label(left_frame,text="Time:",font=("times new roman",12,"bold"))
        roll_label.grid(row=2,column=0,padx=5)
        
        roll_combo=ttk.Entry(left_frame,width=16,font=("times new roman",12,"bold"))
        roll_combo.grid(row=2,column=1,padx=2,pady=7)

        #attendence status
        roll_label=Label(left_frame,text="Attendence Status:",font=("times new roman",12,"bold"))
        roll_label.grid(row=2,column=2,padx=5)
        
        roll_combo=ttk.Entry(left_frame,width=16,font=("times new roman",12,"bold"))
        roll_combo.grid(row=2,column=3,padx=2,pady=7)


        btn_frame=Frame(left_frame,bd=2,relief=RIDGE,bg='red')
        btn_frame.place(x=0,y=128,width=545,height=36)

        reset_btn=Button(btn_frame,text="Import CSV",textvariable=self.importCsv,width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=0)

        # b1_1=Button(btn_frame,text="Reset",textvariable=self.reset_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        # b1_1.place(x=0,y=0, width=136, height=20)

        save_btn=Button(btn_frame,text="Export CSV",textvariable=self.exportCsv,width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        delete_btn=Button(btn_frame,text="Reset",textvariable=self.reset_data,width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=3)


        # right_frame
        right_frame=LabelFrame(main_frame,bd=20,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        right_frame.place(x=640,y=5,width=600,height=450)


        #====table frame====
        table_frame=LabelFrame(right_frame,bd=4,bg="white",relief=RIDGE)
        table_frame.place(x=0,y=0,width=552,height=400)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=["n","r","d","da","t","a"],xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('n',text="Student Name")
        self.student_table.heading('r',text="Roll No")
        self.student_table.heading("d",text="Department")
        self.student_table.heading('da',text="Date")
        self.student_table.heading('t',text="Time")
        self.student_table.heading("a",text="Attendence Status")
        self.student_table["show"]="headings"

        self.student_table.column("n",width=120)
        self.student_table.column("r",width=120)
        self.student_table.column("d",width=120)
        self.student_table.column("da",width=120)
        self.student_table.column("t",width=120)
        self.student_table.column("a",width=140)

        self.student_table.pack(fill=BOTH,expand=True)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)

    def reset_data(self):
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_department.set("")
        self.var_attend_date.set("")
        self.var_attend_time.set("")
        self.var_attend_status.set("")
    

    def fetchData(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("",END,values=i)

    def importCsv(self):
        global my_data
        my_data.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)


        with open (fln) as myfile:
            csvread=csv.reader(myfile,delitem="")
            for i in csvread:
                my_data.append(i)
            self.fetchData(my_data)


    def exportCsv(self):
        try:
            if len(my_data)<1:
                messagebox.showerror("No Data","No data is found to export",parent=self.root)
                return False

            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)

            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delitem="")
                for i in my_data:
                    exp_write.writerow(i)
                    messagebox.showinfo("Data Exported","Your data exported to"+os.path.basename(fln)+"successfully")

        except Exception as e:
            messagebox.showerror("Error",f"Due to: {str(e)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        row=content["values"]
        self.var_attend_roll.set(row[0])
        self.var_attend_name.set(row[1])
        self.var_attend_department.set(row[2])
        self.var_attend_date.set(row[3])
        self.var_attend_time.set(row[4])
        self.var_attend_status.set(row[5])


if __name__=="__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()