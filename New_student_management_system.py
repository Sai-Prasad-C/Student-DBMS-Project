import mysql.connector as sql
from tkinter import ttk
import webbrowser as wb
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkcalendar import *
import STUDENT_DATABASE_MANAGEMENT_SYSTEM_Backend as stdbck
import random as ran

#################################################Functions#####################################################

def personal(self):
    # =========================================BackEnd-Functions===============================================

    def add_student():

        if Roll_No_var.get() == "" or name_var.get() == "":
            tk.messagebox.showerror("Entries Missing", "All Fields are Required!! ")
        else:
            try:
                con = sql.connect(
                    host="localhost",
                    user="root",
                    passwd="",
                    database="stm"
                )
                cur = con.cursor()
                #print(Roll_No_var.get(), name_var.get(), email_var.get(), gender_var.get(),
                #          contact_var.get(), dob_No_var.get(), txt_Address.get(1.0, END))
                query = "insert into students(roll_no,name,email,gender,contact,dob,address) values(%s,%s,%s,%s,%s,%s,%s)"
                input = [(Roll_No_var.get(), name_var.get(), email_var.get(), gender_var.get(),
                          contact_var.get(), dob_No_var.get(), txt_Address.get(1.0, END))]
                cur.executemany(query, input)
                con.commit()
                fetch_data()
                tk.messagebox.showinfo("Your Status", "Entered Particulars Successfully!")
                clear()
                con.close()
            except Exception:
                tk.messagebox.showerror("Your Status", "This Roll Has Been Already Taken!")

    def fetch_data():

        con = sql.connect(
            host="localhost",
            user="root",
            passwd="",
            database="stm"
        )
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert("", END, values=row)
        con.close()

    def clear():
        txt_Roll.delete(0, END)
        txt_name.delete(0, END)
        txt_Email.delete(0, END)
        txt_dob.delete(0, END)
        gender_var.set("")
        txt_Contact.delete(0, END)
        txt_Address.delete(1.0, END)

    def get_cursor(self):
        cursor_row = student_table.focus()
        content = student_table.item(cursor_row)
        row = content["values"]
        Roll_No_var.set(row[0])
        name_var.set(row[1])
        email_var.set(row[2])
        gender_var.set(row[3])
        contact_var.set(row[4])
        dob_No_var.set(row[5])
        txt_Address.delete(1.0, END)
        txt_Address.insert(END, row[6])

    def update_data():
        con = sql.connect(
            host="localhost",
            user="root",
            passwd="",
            database="stm"
        )
        cur = con.cursor()
        query = "update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s"
        input = [(name_var.get(), email_var.get(), gender_var.get(),
                  contact_var.get(), dob_No_var.get(), txt_Address.get(1.0, END), Roll_No_var.get())]
        cur.executemany(query, input)
        con.commit()
        fetch_data()
        clear()
        con.close()

    def delete_data():
        con = sql.connect(
            host="localhost",
            user="root",
            passwd="",
            database="stm"
        )
        cur = con.cursor()
        cur.execute("delete from students where roll_no = {}".format(Roll_No_var.get()))
        con.commit()
        con.close()
        fetch_data()
        clear()
        tk.messagebox.showinfo("Your Status", "Record Deleted Successfully!")

    def search_data():
        con = sql.connect(
            host="localhost",
            user="root",
            passwd="",
            database="stm"
        )
        cur = con.cursor()
        cur.execute("select * from students where " + str(search_by.get()) + " LIKE '%" + str(search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert("", END, values=row)
        con.close()
    #===========================================Front End===================================

    root = Tk()
    root.title("Student Management System")
    root.geometry("1350x700+0+0")

    title = Label(root,text = "Student Management System",font = ("times new roman",40,"bold"),
                  bd=10,relief = GROOVE,bg="yellow",fg="red" )
    title.pack(side=TOP,fill=X)

    #============================Variables==============================================

    Roll_No_var = StringVar()
    name_var = StringVar()
    email_var = StringVar()
    gender_var = StringVar()
    contact_var = StringVar()
    dob_No_var = StringVar()

    search_by = StringVar()
    search_txt = StringVar()


    #============================Manage Frame===========================================

    Manage_frame=Frame(root,bd=4,relief=RIDGE,bg="crimson")
    Manage_frame.place(x=20,y=100,width=450,height=595)

    m_title=Label(Manage_frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman",30,"bold"))
    m_title.grid(row=0, columnspan=2,pady=20)

    lbl_roll=Label(Manage_frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
    lbl_roll.grid(row=1, column=0,pady=10,padx=20,sticky="w")

    txt_Roll=Entry(Manage_frame,textvariable=Roll_No_var,bd=5,relief=GROOVE,font=("times new roman",15,"bold"))
    txt_Roll.grid(row=1, column=1,pady=10,padx=20,sticky="w")

    lbl_name=Label(Manage_frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
    lbl_name.grid(row=2, column=0,pady=10,padx=20,sticky="w")

    txt_name=Entry(Manage_frame,textvariable=name_var,bd=5,relief=GROOVE,font=("times new roman",15,"bold"))
    txt_name.grid(row=2, column=1,pady=10,padx=20,sticky="w")

    lbl_Email=Label(Manage_frame,text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold"))
    lbl_Email.grid(row=3, column=0,pady=10,padx=20,sticky="w")

    txt_Email=Entry(Manage_frame,textvariable=email_var,bd=5,relief=GROOVE,font=("times new roman",15,"bold"))
    txt_Email.grid(row=3, column=1,pady=10,padx=20,sticky="w")

    lbl_Gender=Label(Manage_frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
    lbl_Gender.grid(row=4, column=0,pady=10,padx=20,sticky="w")

    combo_gender=ttk.Combobox(Manage_frame,textvariable=gender_var,font=("times new roman",13,"bold"),state="readonly")
    combo_gender['values']=("Male","Female","Others")
    combo_gender.grid(row=4, column=1,pady=10,padx=20)

    lbl_Contact=Label(Manage_frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
    lbl_Contact.grid(row=5, column=0,pady=10,padx=20,sticky="w")

    txt_Contact=Entry(Manage_frame,textvariable=contact_var,bd=5,relief=GROOVE,font=("times new roman",15,"bold"))
    txt_Contact.grid(row=5, column=1,pady=10,padx=20,sticky="w")

    lbl_dob=Label(Manage_frame,text="D.O.B",bg="crimson",fg="white",font=("times new roman",20,"bold"))
    lbl_dob.grid(row=6, column=0,pady=10,padx=20,sticky="w")

    txt_dob=Entry(Manage_frame,textvariable=dob_No_var,bd=5,relief=GROOVE,font=("times new roman",15,"bold"))
    txt_dob.grid(row=6, column=1,pady=10,padx=20,sticky="w")

    lbl_Address=Label(Manage_frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
    lbl_Address.grid(row=7, column=0,pady=10,padx=20,sticky="w")

    txt_Address=Text(Manage_frame,bd=5,relief=GROOVE,width=29,height=4,font=("times new roman",10,"bold"))
    txt_Address.grid(row=7, column=1,pady=10,padx=20,sticky="w")

    #=============================Button Frame===========================================

    btn_frame=Frame(Manage_frame,bd=4,relief=RIDGE,bg="crimson")
    btn_frame.place(x=15,y=530,width=410)

    Addbtn = Button(btn_frame,text="Add",width=10,command = add_student)
    Addbtn.grid(row=0,column=0,padx=10,pady=10)

    updatebtn = Button(btn_frame,text="Update",width=10,command = update_data)
    updatebtn.grid(row=0,column=1,padx=10,pady=10)

    deletebtn = Button(btn_frame,text="Delete",width=10,command = delete_data)
    deletebtn.grid(row=0,column=2,padx=10,pady=10)

    Clearbtn = Button(btn_frame,text="Clear",width=10,command = clear)
    Clearbtn.grid(row=0,column=3,padx=10,pady=10)

    #============================Detail Frame===========================================


    Detail_frame=Frame(root,bd=4,relief=RIDGE,bg="crimson")
    Detail_frame.place(x=500,y=100,width=800,height=595)

    lblSearch=Label(Detail_frame,text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold"))
    lblSearch.grid(row=0, column=0,pady=10,padx=20,sticky="w")

    combo_search=ttk.Combobox(Detail_frame,textvariable = search_by,width=10,font=("times new roman",12,"bold"),state="readonly")
    combo_search['values']=("roll_no","name","contact")
    combo_search.grid(row=0, column=1,pady=10,padx=20)

    txt_Search=Entry(Detail_frame,textvariable = search_txt,bd=5,relief=GROOVE,width=20,font=("times new roman",13,"bold"))
    txt_Search.grid(row=0, column=2,pady=10,padx=20,sticky="w")

    Searchbtn = Button(Detail_frame,text="Search",width=10,pady=5,command = search_data)
    Searchbtn.grid(row=0,column=3,padx=10,pady=10)

    Showallbtn = Button(Detail_frame,text="Show All",width=10,pady=5,command = fetch_data)
    Showallbtn.grid(row=0,column=4,padx=10,pady=10)

    #===============================Table Frame==============================

    Table_Frame=Frame(Detail_frame,bd=4,relief=RIDGE,bg="crimson")
    Table_Frame.place(x=10,y=70,width=760,height=500)

    scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

    student_table=ttk.Treeview(Table_Frame,
                               columns=("roll","name","email","gender","contact","dob","Address"),
                               xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=student_table.xview)
    scroll_y.config(command=student_table.yview)

    student_table.heading("roll",text="Roll No.")
    student_table.heading("name",text="Name")
    student_table.heading("email",text="Email")
    student_table.heading("gender",text="Gender")
    student_table.heading("contact",text="Contact")
    student_table.heading("dob",text="D.O.B")
    student_table.heading("Address",text="Address")

    student_table["show"]="headings"

    student_table.column('roll',width=100)
    student_table.column('name',width=100)
    student_table.column('email',width=100)
    student_table.column('gender',width=100)
    student_table.column('contact',width=100)
    student_table.column('dob',width=100)
    student_table.column('Address',width=150)
    student_table.bind("<ButtonRelease->",get_cursor)

    student_table.pack(fill=BOTH,expand=1)
    fetch_data()

    root.mainloop()

personal(NONE)