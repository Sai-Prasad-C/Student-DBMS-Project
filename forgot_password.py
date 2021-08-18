import mysql.connector as sql
from tkinter import ttk
import webbrowser as wb
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkcalendar import *
import STUDENT_DATABASE_MANAGEMENT_SYSTEM_Backend as stdbck
import random as ran

check = False
htext = ""

def forgotpage(self):
    def click():
        if check:
            passwd =  "Your Password : '" + str(a[5]) + "'"
            tk.messagebox.showinfo("Your Password",passwd)  #
        else:
            tk.messagebox.showerror("Your Status", "One or More Pariculars Not Entered")

    def verify():
        global a
        global check
        userdeatils = stdbck.showdata()
        for a in userdeatils:
            if a[0] == Name.get():
                if a[1] == dobent.get():
                    if a[2] == Email.get():
                        if a[3] == Userid.get():
                            if a[4] == Gender.get():
                                check = True
                                break
            else:
                check = False
        if cap.get() == htext and not check :  # captchaentry.get(0.0,END) #and len(Name.get()) != 0 and len(dobent.get()) != 0 and len(Email.get()) != 0 and len(Userid.get()) != 0 and len(Gender.get()) == 0
            tk.messagebox.showerror("Something Went Wrong", "Credentials Mismatch!")#
        elif len(Name.get()) == 0 or len(dobent.get()) == 0 or len(Email.get()) == 0 or len(Userid.get()) == 0 or len(Gender.get()) == 0:
            tk.messagebox.showerror("Your Status", "One or More Pariculars Not Entered")
        elif len(cap.get()) == 0:
            tk.messagebox.showinfo("CAPTCHA!!", "Please Enter Captcha")  #
        elif cap.get() != htext:
            tk.messagebox.showerror("CAPTCHA!!", "Incorrect Captcha")
        else:
            tk.messagebox.showinfo("Your Status","Credentials Matched!")  #

    def capfun():
        global htext
        htext = ""
        captcha.delete("all")
        h = []
        fnt = ["Verdana", "Arial", "Papyrus", "Calibri"]
        colours = ["yellow", "red", "blue", "green", "grey"]
        for i in range(5):
            h.append(chr(ran.randint(65, 90)))
        text1 = captcha.create_text(40 + ran.randint(0, 10), 40 + ran.randint(0, 10), text=h[0],
                                      font=fnt[ran.randint(0, 3)] + " 32 bold", fill=colours[ran.randint(0, 4)])
        text2 = captcha.create_text(80 + ran.randint(0, 10), 40 + ran.randint(0, 10), text=h[1],
                                      font=fnt[ran.randint(0, 3)] + " 32 bold", fill=colours[ran.randint(0, 4)])
        text3 = captcha.create_text(120 + ran.randint(0, 10), 40 + ran.randint(0, 10), text=h[2],
                                      font=fnt[ran.randint(0, 3)] + " 32 bold", fill=colours[ran.randint(0, 4)])
        text4 = captcha.create_text(160 + ran.randint(0, 10), 40 + ran.randint(0, 10), text=h[3],
                                      font=fnt[ran.randint(0, 3)] + " 32 bold", fill=colours[ran.randint(0, 4)])
        text5 = captcha.create_text(200 + ran.randint(0, 10), 40 + ran.randint(0, 10), text=h[4],
                                      font=fnt[ran.randint(0, 3)] + " 32 bold", fill=colours[ran.randint(0, 4)])

        for i in range(10):
            line = captcha.create_line(ran.randint(5, 295), ran.randint(5, 195), ran.randint(5, 295), ran.randint(5, 195),
                                       fill = colours[ran.randint(0, 4)], width = ran.randint(0,3))

        for i in h:
            htext = htext + i


    root2 = Tk()
    root2.geometry("687x629+363+63")
    root2.title("Forgot Password??")
    root2.configure(background="#09d8a8")

    _bgcolor = '#0da2d8'  # Closest X11 color: 'DeepSkyBlue3'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9'  # X11 color: 'gray85'
    _ana1color = '#d9d9d9'  # X11 color: 'gray85'
    _ana2color = '#ececec'  # Closest X11 color: 'gray92'
    font11 = "-family {Segoe UI} -size 18 -weight bold -slant " \
             "roman -underline 0 -overstrike 0"
    font13 = "-family {Segoe UI} -size 15 -weight normal -slant " \
             "roman -underline 0 -overstrike 0"
    font14 = "-family {Segoe UI} -size 16 -weight bold -slant " \
             "roman -underline 0 -overstrike 0"
    font15 = "-family {Segoe UI} -size 9 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
    font16 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"


    Name = StringVar()
    TnC = StringVar()
    Email = StringVar()
    Userid = StringVar()
    Gender = StringVar()
    cap = StringVar()

    headinglbl = tk.Label(root2)
    headinglbl.place(relx=0.007, rely=0.016, height=61, width=674)
    headinglbl.configure(background="#0da2d8")
    headinglbl.configure(disabledforeground="#a3a3a3")
    headinglbl.configure(font=font11)
    headinglbl.configure(foreground="#000000")
    headinglbl.configure(text='''Enter The Particulars Correctly!''')

    mainframe = tk.Frame(root2)
    mainframe.place(relx=0.015, rely=0.127, relheight=0.866
                , relwidth=0.677)
    mainframe.configure(relief='groove')
    mainframe.configure(borderwidth="2")
    mainframe.configure(relief="groove")
    mainframe.configure(background="#09d8c8")

    lblname = tk.Label(mainframe)
    lblname.place(relx=0.043, rely=0.037, height=41, width=114)
    lblname.configure(background="#0da2d8")
    lblname.configure(disabledforeground="#a3a3a3")
    lblname.configure(foreground="#000000")
    lblname.configure(text='''Name''')

    lbldob = tk.Label(mainframe)
    lbldob.place(relx=0.043, rely=0.128, height=41, width=114)
    lbldob.configure(background="#0da2d8")
    lbldob.configure(disabledforeground="#a3a3a3")
    lbldob.configure(foreground="#000000")
    lbldob.configure(text='''D.O.B''')

    lblemail = tk.Label(mainframe)
    lblemail.place(relx=0.043, rely=0.22, height=41, width=114)
    lblemail.configure(background="#0da2d8")
    lblemail.configure(disabledforeground="#a3a3a3")
    lblemail.configure(foreground="#000000")
    lblemail.configure(text='''E-Mail Address''')

    userlbl = tk.Label(mainframe)
    userlbl.place(relx=0.043, rely=0.312, height=41, width=114)
    userlbl.configure(background="#0da2d8")
    userlbl.configure(disabledforeground="#a3a3a3")
    userlbl.configure(foreground="#000000")
    userlbl.configure(text='''Username''')


    namentry = tk.Entry(mainframe,textvariable = Name)
    namentry.place(relx=0.301, rely=0.037,height=40, relwidth=0.654)
    namentry.configure(background="white")
    namentry.configure(disabledforeground="#a3a3a3")
    namentry.configure(font="-family {Courier New} -size 10")
    namentry.configure(foreground="#000000")
    namentry.configure(insertbackground="black")

    dateframe = tk.Frame(mainframe)
    dateframe.place(relx=0.301, rely=0.128,height=40, relwidth=0.654)
    dateframe.configure(background="white")

    dobent = DateEntry(dateframe, width=40, background="blue", foreground="white", borderwidth=2)
    dobent.pack(padx=10, pady=10)

    emailentry = tk.Entry(mainframe,textvariable = Email)
    emailentry.place(relx=0.301, rely=0.22,height=40, relwidth=0.654)
    emailentry.configure(background="white")
    emailentry.configure(disabledforeground="#a3a3a3")
    emailentry.configure(font="-family {Courier New} -size 10")
    emailentry.configure(foreground="#000000")
    emailentry.configure(insertbackground="black")

    userentry = tk.Entry(mainframe,textvariable = Userid)
    userentry.place(relx=0.301, rely=0.312,height=40, relwidth=0.654)
    userentry.configure(background="white")
    userentry.configure(disabledforeground="#a3a3a3")
    userentry.configure(font="-family {Courier New} -size 10")
    userentry.configure(foreground="#000000")
    userentry.configure(insertbackground="black")



    #===========================================CAPTCHA=================================


    lblcaptcha = tk.Label(mainframe)
    lblcaptcha.place(relx=0.215, rely=0.477, height=41, width=264)
    lblcaptcha.configure(background="#09d8c8")
    lblcaptcha.configure(disabledforeground="#a3a3a3")
    lblcaptcha.configure(font=font11)
    lblcaptcha.configure(foreground="#000000")
    lblcaptcha.configure(text='''Enter Captcha Below''')

    verifybtn = tk.Button(mainframe)
    verifybtn.place(relx=0.29, rely=0.881, height=44, width=187)
    verifybtn.configure(activebackground="#ececec")
    verifybtn.configure(activeforeground="#000000")
    verifybtn.configure(background="#3a00d8")
    verifybtn.configure(disabledforeground="#a3a3a3")
    verifybtn.configure(font=font14)
    verifybtn.configure(foreground="#ffffff")
    verifybtn.configure(highlightbackground="#0da2d8")
    verifybtn.configure(highlightcolor="black")
    verifybtn.configure(pady="0")
    verifybtn.configure(text='''VERIFY!''', command = verify)

    captchaentry = tk.Entry(mainframe,textvariable = cap)
    captchaentry.place(relx=0.108, rely=0.807, relheight=0.062
                , relwidth=0.417)
    captchaentry.configure(background="white")
    captchaentry.configure(font=font13)
    captchaentry.configure(foreground="black")
    captchaentry.configure(highlightbackground="#0da2d8")
    captchaentry.configure(highlightcolor="black")
    captchaentry.configure(insertbackground="black")
    captchaentry.configure(selectbackground="#c4c4c4")
    captchaentry.configure(selectforeground="black")
    #captchaentry.configure(wrap="word")

    btncapt = tk.Button(mainframe)
    btncapt.place(relx=0.581, rely=0.807, height=34, width=157)
    btncapt.configure(activebackground="#ececec")
    btncapt.configure(activeforeground="#000000")
    btncapt.configure(background="#3a00d8")
    btncapt.configure(disabledforeground="#a3a3a3")
    btncapt.configure(font=font15)
    btncapt.configure(foreground="#ffffff")
    btncapt.configure(highlightbackground="#0da2d8")
    btncapt.configure(highlightcolor="black")
    btncapt.configure(pady="0",command = capfun)
    btncapt.configure(text='''Generate/New Captcha''')

    """captchalbl = tk.Label(mainframe,image = captcha)
    captchalbl.place(relx=0.258, rely=0.569, height=121, width=236)#, height=121, width=234
    captchalbl.configure(background="#ffffff")
    captchalbl.configure(disabledforeground="#a3a3a3")
    captchalbl.configure(foreground="#000000")"""

    captcha = Canvas(mainframe,width = 280,height = 100,bg = "white")
    captcha.place(relx=0.172, rely=0.569)#, height=121, width=234

    genderlbl = tk.Label(mainframe)
    genderlbl.place(relx=0.043, rely=0.404, height=41, width=114)
    genderlbl.configure(background="#0da2d8")
    genderlbl.configure(disabledforeground="#a3a3a3")
    genderlbl.configure(foreground="#000000")
    genderlbl.configure(text='''Gender''')

    genderframe = tk.Frame(mainframe)
    genderframe.place(relx=0.301, rely=0.404,height=40, relwidth=0.654)
    genderframe.configure(background="white")

    rdbtn1 = Radiobutton(genderframe)
    rdbtn1.place(relx=0.032, rely=0.111, relheight=0.778
                 , relwidth=0.406)
    rdbtn1.configure(activebackground="#ececec")
    rdbtn1.configure(activeforeground="#000000")
    rdbtn1.configure(background="white")
    rdbtn1.configure(disabledforeground="#a3a3a3")
    rdbtn1.configure(font=font13)
    rdbtn1.configure(foreground="#000000")
    rdbtn1.configure(highlightbackground="#0da2d8")
    rdbtn1.configure(highlightcolor="black")
    rdbtn1.configure(justify='left')
    rdbtn1.configure(text='Male')
    rdbtn1.configure(variable=Gender, value="male")

    rdbtn2 = Radiobutton(genderframe)
    rdbtn2.place(relx=0.508, rely=0.111, relheight=0.778
                 , relwidth=0.438)
    rdbtn2.configure(activebackground="#ececec")
    rdbtn2.configure(activeforeground="#000000")
    rdbtn2.configure(background="white")
    rdbtn2.configure(disabledforeground="#a3a3a3")
    rdbtn2.configure(font=font13)
    rdbtn2.configure(foreground="#000000")
    rdbtn2.configure(highlightbackground="#0da2d8")
    rdbtn2.configure(highlightcolor="black")
    rdbtn2.configure(justify='left')
    rdbtn2.configure(text='Female')
    rdbtn2.configure(variable=Gender, value="female")

    #=========================================SideFrame========================================================

    sideframe = tk.Frame(root2)
    sideframe.place(relx=0.699, rely=0.127, relheight=0.866
                    , relwidth=0.298)
    sideframe.configure(relief='groove')
    sideframe.configure(borderwidth="2")
    sideframe.configure(relief="groove")
    sideframe.configure(background="#09d8c8")

    lblmakesure = tk.Label(sideframe)
    lblmakesure.place(relx=0.049, rely=0.0, height=31, width=189)
    lblmakesure.configure(background="#09d8c8")
    lblmakesure.configure(disabledforeground="#a3a3a3")
    lblmakesure.configure(font=font16)
    lblmakesure.configure(foreground="#000000")
    lblmakesure.configure(text='''Make Sure You have Entered''')

    lblcorrectname = tk.Label(sideframe)
    lblcorrectname.place(relx=0.098, rely=0.055, height=31, width=104)
    lblcorrectname.configure(background="#09d8c8")
    lblcorrectname.configure(disabledforeground="#a3a3a3")
    lblcorrectname.configure(foreground="#000000")
    lblcorrectname.configure(text='''Correct Name*''')

    lblcorrectdob = tk.Label(sideframe)
    lblcorrectdob.place(relx=0.098, rely=0.128, height=31, width=94)
    lblcorrectdob.configure(background="#09d8c8")
    lblcorrectdob.configure(disabledforeground="#a3a3a3")
    lblcorrectdob.configure(foreground="#000000")
    lblcorrectdob.configure(text='''Correct D.O.B.*''')

    lblcorrectemail = tk.Label(sideframe)
    lblcorrectemail.place(relx=0.122, rely=0.22, height=31, width=94)
    lblcorrectemail.configure(background="#09d8c8")
    lblcorrectemail.configure(disabledforeground="#a3a3a3")
    lblcorrectemail.configure(foreground="#000000")
    lblcorrectemail.configure(text='''Correct E-Mail*''')

    lblcorrectuser = tk.Label(sideframe)
    lblcorrectuser.place(relx=0.122, rely=0.312, height=41, width=114)
    lblcorrectuser.configure(background="#09d8c8")
    lblcorrectuser.configure(disabledforeground="#a3a3a3")
    lblcorrectuser.configure(foreground="#000000")
    lblcorrectuser.configure(text='''Correct Username*''')

    lblcorrectgender = tk.Label(sideframe)
    lblcorrectgender.place(relx=0.049, rely=0.404, height=41
                               , width=124)
    lblcorrectgender.configure(background="#09d8c8")
    lblcorrectgender.configure(disabledforeground="#a3a3a3")
    lblcorrectgender.configure(foreground="#000000")
    lblcorrectgender.configure(text='''Correct Gender*''')

    checktnc = Checkbutton(sideframe,offvalue = "disabled",onvalue = "enabled",font = font16, background="#09d8c8",foreground="#000000",text='''I'm aware of T. & C.''',variable= TnC)
    checktnc.place(relx=0.098, rely=0.624, relheight=0.101, relwidth=0.737)

    '''checktnc = tk.Checkbutton(sideframe,offvalue = "disabled",onvalue = "enabled")
    checktnc.place(relx=0.098, rely=0.624, relheight=0.101
                   , relwidth=0.737)
    checktnc.configure(activebackground="#ececec")
    checktnc.configure(activeforeground="#000000")
    checktnc.configure(background="#09d8c8")
    checktnc.configure(disabledforeground="#a3a3a3")
    checktnc.configure(font=font16)
    checktnc.configure(foreground="#000000")
    checktnc.configure(highlightbackground="#0da2d8")
    checktnc.configure(highlightcolor="black")
    checktnc.configure(offrelief="flat")
    checktnc.configure(justify='left')
    checktnc.configure(text='I'm aware of T. & C.')
    checktnc.configure(variable= TnC)'''

    btncreate = tk.Button(sideframe)
    btncreate.place(relx=0.098, rely=0.789, height=44, width=167)
    btncreate.configure(activebackground="#ececec")
    btncreate.configure(activeforeground="#000000")
    btncreate.configure(background="#3a00d8")
    btncreate.configure(disabledforeground="#a3a3a3")
    btncreate.configure(font="-family {Segoe UI} -size 16 -weight bold")
    btncreate.configure(foreground="#ffffff")
    btncreate.configure(highlightbackground="#0da2d8")
    btncreate.configure(highlightcolor="black")
    btncreate.configure(pady="0")
    #btncreate.configure(state= TnC.get())
    btncreate.configure(text='''Get Password!''',command = click)

    root2.mainloop()

def personal(self):
    # =========================================BackEnd-Functions===============================================

    def createdb():
        con = sql.connect(
            host="localhost",
            user="root",
            passwd="",
        )

        cur = con.cursor()

        cur.execute("create database if not exists stm")
        cur.execute("use stm")
        cur.execute("create table if not exists students(roll_no int(100) primary key,name text,email text,gender text,contact text,dob text,address text,maths int,physics int,chemistry int,comp_sci int,english int,attend int)")
        con.commit()
        con.close()

    def add_student():
        createdb()

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
        createdb()

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
        createdb()

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
        createdb()

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
        createdb()

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
forgotpage(NONE)