from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.font import BOLD
from tkinter import messagebox
import mysql.connector
import cv2 as cv



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x650")
        self.root.title("Customers' Information")

        #====vars====
        self.var_lev=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_gendr=StringVar()
        self.var_phn=StringVar()


        #top left img
        img=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/student1.jpg")
        img=img.resize((440,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=430,height=170)


        # top med img
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


         # BG
        img3=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/bg1.jpg")
        img3=img3.resize((1530,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=170,width=1530,height=580)


        # title
        title_lbl=Label(bg_img, text="Customers' Care",font=("times new roman",35,"bold"),bg="white",fg="purple")
        title_lbl.place(x=8,y=8, width=1280, height=40)


        # main_frame
        main_frame=Frame(bg_img,bd=4)
        main_frame.place(x=8,y=56,width=1280,height=470)


        # left_frame
        left_frame=LabelFrame(main_frame,bd=20,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=5,width=600,height=450)



        #img_left
        img_left=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/imgleft.jpg")
        img_left=img_left.resize((560,200),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=560,height=130)



        #course_information
        course_frame=LabelFrame(left_frame,bd=4,bg="white",relief=RIDGE,text="Course Information",font=("times new roman",12,"bold"))
        course_frame.place(x=5,y=135,width=552,height=100)

        #Level
        level_label=Label(course_frame,text="Level",font=("times new roman",12,"bold"),bg="white")
        level_label.grid(row=0,column=0,padx=5)

        level_combo=ttk.Combobox(course_frame,textvariable=self.var_lev,font=("times new roman",12,"bold"),state="readonly")
        level_combo["values"]=("Choose Level","Bachelors","School","+2","Masters")
        level_combo.current(0)
        level_combo.grid(row=0,column=1,padx=2,pady=7)

        # course
        course_label=Label(course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=5)

        course_combo=ttk.Combobox(course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Choose Course","BCA","BSc.CSIT","BCS","BIT","BBA","BBS","BIM",)
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=7)

        
        #Year
        year_label=Label(course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=2)

        year_combo=ttk.Combobox(course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Choose Year","2074","2075","2076","2078")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=5)

        # semester
        sem_label=Label(course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=5)
        sem_combo=ttk.Combobox(course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly")
        sem_combo["values"]=("Choose Semester","I","III","V","VI")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=5)



        # Class_information
        class_course_frame=LabelFrame(left_frame,bd=4,bg="white",relief=RIDGE,text="Class Information",font=("times new roman",12,"bold"))
        class_course_frame.place(x=5,y=240,width=552,height=164)


        #Student_name
        stdnt_label=Label(class_course_frame,text="Student Name :",font=("times new roman",12,"bold"))
        stdnt_label.grid(row=0,column=0,padx=5)

        stdnt_combo=ttk.Entry(class_course_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        stdnt_combo.grid(row=0,column=1,padx=4,pady=7)

        # Roll No
        roll_label=Label(class_course_frame,text="Roll No:",font=("times new roman",12,"bold"))
        roll_label.grid(row=0,column=2,padx=5)
        
        roll_combo=ttk.Entry(class_course_frame,textvariable=self.var_roll,width=15,font=("times new roman",12,"bold"))
        roll_combo.grid(row=0,column=3,padx=2,pady=7)

        
        #gend
        gend_label=Label(class_course_frame,text="Gender : ",font=("times new roman",12,"bold"))
        gend_label.grid(row=1,column=0,padx=5)

        gend_combo=ttk.Combobox(class_course_frame,textvariable=self.var_gendr,font=("times new roman",12,"bold"))
        gend_combo["values"]=("Choose Gender","Female","Male")
        gend_combo.current(0)
        gend_combo.grid(row=1,column=1,padx=4,pady=5)


        #phn_num
        phn_label=Label(class_course_frame,text="Phone No :",font=("times new roman",12,"bold"))
        phn_label.grid(row=1,column=2,padx=5)
        
        phn_combo=ttk.Entry(class_course_frame,textvariable=self.var_phn,width=15,font=("times new roman",12,"bold"))
        phn_combo.grid(row=1,column=3,padx=2,pady=7)

        
        #radibtn
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_course_frame,variable=self.var_radio1,text="Take Photos",value='yes')
        radiobtn1.grid(row=2,column=2)
        
        # self.radio_btn2=StringVar()
        radiobtn2=ttk.Radiobutton(class_course_frame,variable=self.var_radio1,text="No Photos")
        radiobtn2.grid(row=2,column=3)

        #btnframe
        btn_frame=Frame(class_course_frame,bd=2,relief=RIDGE,bg='red')
        btn_frame.place(x=0,y=98,width=545,height=36)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=4,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=0)

        # b1_1=Button(btn_frame,text="Reset",font=("times new roman",15,"bold"),bg="blue",fg="white")
        # b1_1.place(x=0,y=0, width=136, height=20)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=4,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=4,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=4,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=3)

        take_btn=Button(btn_frame,command=self.generate_dataset,text="Take Photo Sample",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_btn.grid(row=0,column=4,padx=2)

        update_btn=Button(btn_frame,text="Update Photo Sample",width=int(16.8),font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=5)



        # right_frame
        right_frame=LabelFrame(main_frame,bd=20,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=640,y=5,width=600,height=450)

        #img_right
        img_right=Image.open("/home/rojan/Desktop/Face-Recognition-System/Images/imgright.jpg")
        img_right=img_right.resize((560,200),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=0,y=0,width=560,height=130)



        #****search-system****
        search_frame=LabelFrame(right_frame,bd=4,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=0,y=130,width=552,height=62)


        search_label=Label(search_frame,text="Search By :",font=("times new roman",12,"bold"),bg="red")
        search_label.grid(row=0,column=0,padx=5,pady=0)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly")
        search_combo["values"]=("Select","Name","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=0)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=0)

        search_btn=Button(search_frame,text="Search",width=5,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)

        show_btn=Button(search_frame,text="ShowAll",width=int(5.8),font=("times new roman",12,"bold"),bg="blue",fg="white")
        show_btn.grid(row=0,column=4)

        #====table frame====
        table_frame=LabelFrame(right_frame,bd=4,bg="white",relief=RIDGE)
        table_frame.place(x=0,y=195,width=552,height=208)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=["l","c","y","s","n","r","g","p","o"],xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('l',text="Level")
        self.student_table.heading('c',text="Course")
        self.student_table.heading("y",text="Year")
        self.student_table.heading('s',text="Semester")
        self.student_table.heading('n',text="Name")
        self.student_table.heading("r",text="Roll No")
        self.student_table.heading("g",text="Gender")
        self.student_table.heading("p",text="Phone No")
        self.student_table.heading("o",text="Photo Sample")

        self.student_table["show"]="headings"

        self.student_table.column("l",width=100)
        self.student_table.column("c",width=100)
        self.student_table.column("y",width=100)
        self.student_table.column("s",width=80)
        self.student_table.column("n",width=180)
        self.student_table.column("r",width=100)
        self.student_table.column("g",width=100)
        self.student_table.column("p",width=100)
        self.student_table.column("o",width=120)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fet_data()

    
    #====Functions btns====
    def add_data(self):
        try:
            if self.var_lev.get()=="Choose Department" or self.var_name.get()=="":
                messagebox.showerror("Error","All fields are compulsory",parent=self.root)
            else:
                conn=mysql.connector.connect(host="localhost", username="root",password="0422K10Jrojan88/?a",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_lev.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_sem.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_gendr.get(),
                                                                                            self.var_phn.get(),
                                                                                            self.var_radio1.get()                                                                       
                                                                                            ))

                conn.commit()
                self.fet_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error",f"Due to : {str(e)}",parent=self.root)

    
    #====Redraw data====
    def fet_data(self):
        conn=mysql.connector.connect(host="localhost", username="root",password="0422K10Jrojan88/?a",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute('select * from student')
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #==get cursor==
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_lev.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_name.set(data[4]),
        self.var_roll.set(data[5]),
        self.var_gendr.set(data[6]),
        self.var_phn.set(data[7]),
        self.var_radio1.set(data[8])


    #==Update function==
    def update_data(self):
        if self.var_lev.get()=="Choose Department" or self.var_name.get()=="":
                messagebox.showerror("Error","All fields are compulsory",parent=self.root)

        else:
            try:
                Update=messagebox.askyesno("Update",'Do you want to update this student details',parent=self.root)
                
                if Update>0:
                    conn=mysql.connector.connect(host="localhost", username="root",password="0422K10Jrojan88/?a",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set Level=%s,Course=%s,Year=%s,Sem=%s,Name=%s,Gendr=%s,Phone_no=%s,PhotoSample=%s where Roll_no=%s ",
                                                                                                                        (
                                                                                                                            self.var_lev.get(),
                                                                                                                            self.var_course.get(),
                                                                                                                            self.var_year.get(),
                                                                                                                            self.var_sem.get(),
                                                                                                                            self.var_name.get(),
                                                                                                                            self.var_gendr.get(),
                                                                                                                            self.var_phn.get(),
                                                                                                                            self.var_radio1.get(),
                                                                                                                            self.var_roll.get()
                                                                                                                        ))
                 
                
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details Successfully updated",parent=self.root)
                conn.commit()
                self.fet_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Due to: {str(e)}",parent=self.root)




    #delete function
    def delete_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Student Roll No must be required",parent=self.root)

        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", username="root",password="0422K10Jrojan88/?a",database="face_recognizer")
                    my_cursor=conn.cursor()   
                    sql="delete from student where Roll_no=%s"
                    val=(self.var_roll.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fet_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due to {str(e)}",parent=self.root)




    #reset
    def reset_data(self):
        self.var_lev.set("Select Level")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_gendr.set("")
        self.var_phn.set("")
        self.var_radio1.set("")





    #====Generate dataset to take photo samples====
    def generate_dataset(self):
        if self.var_lev.get()=="Choose Department" or self.var_name.get()=="":
                messagebox.showerror("Error","All fields are compulsory",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root",password="0422K10Jrojan88/?a",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                roll=0
                for x in myresult:
                    roll+=1
                my_cursor.execute("Update student set Level=%s,Course=%s,Year=%s,Sem=%s,Name=%s,Gendr=%s,Phone_no=%s,PhotoSample=%s where Roll_no=%s ",
                                                                                                                (
                                                                                                                    self.var_lev.get(),
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_sem.get(),
                                                                                                                    self.var_name.get(),
                                                                                                                    self.var_gendr.get(),
                                                                                                                    self.var_phn.get(),
                                                                                                                    self.var_radio1.get(),
                                                                                                                    self.var_roll.get()==roll+1
                                                                                                                ))
                conn.commit()
                self.fet_data()
                self.reset_data()
                conn.close()






                #==load predefined data on face frontals from opencv==
                face_classifier=cv.CascadeClassifier("haarcascade_profileface_default.xml")

                def face_cropped(img):
                    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor is 1.3 and min nighbor is 5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv.VideoCapture(0)
                img_id=0
                while True:
                    ret,mframe=cap.read()
                    if face_cropped(mframe) is not None:
                        img_id+=1
                        face=cv.resize(face_cropped(mframe),(450,450))
                        face=cv.cvtColor(face,cv.COLOR_BGR2GRAY)
                        file_path="croppedfaces/user."+str(roll)+"."+str(img_id)+".jpg"
                        cv.imwrite(file_path,face)
                        cv.putText(face,str(img_id),(320,420),cv.FONT_HERSHEY_COMPLEX,2,(255,0,255),2)
                        cv.imshow("Cropping.. Face",face)

                        if cv.waitKey(1)==13 or int(img_id)==200:
                            break

                cap.release()
                cv.destroyAllWindows()
                messagebox.showinfo("Result","Generating datasets completed")
            
            except Exception as e:
                messagebox.showerror("Error",f"Due to: {str(e)}",parent=self.root)





if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()




