import mysql.connector as sql
from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random as ran

def personal(self):
    #=========================================BackEnd-Functions===============================================

    def add_res():

        if name_var.get() == "":
            tk.messagebox.showerror("Error", "Select Student First")
        else:
            try:
                con = sql.connect(
                    host="localhost",
                    user="root",
                    passwd="",
                    database="stm"
                )
                cur = con.cursor()
                query = "update studets set maths = %s,physics = %s,chemistry = %s,comp_sci = %s,english = %s,attend = %s  where name = %s"
                input = [(maths_var.get(), physics_var.get(), chemistry_var.get(), compsci_var.get(),
                          english_var.get(), Attend_var.get(), name_var.get())]
                cur.executemany(query, input)
                con.commit()
                fetch_rec()
                tk.messagebox.showinfo("Your Status", "Entered Particulars Successfully!")
                clear_data()
                con.close()
            except Exception:
                tk.messagebox.showerror("Your Status", "Please Rectify Your Error!")

    def fetch_rec():

        con = sql.connect(
            host="localhost",
            user="root",
            passwd="",
            database="stm"
        )
        cur = con.cursor()
        cur.execute("select name,attend,maths,physics,chemistry,comp_sci,english from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            result_table.delete(*result_table.get_children())
            for row in rows:
                result_table.insert("", END, values=row)
        con.close()

    def clear_data():
        Attend_var.set("")
        name_var.set("")
        maths_var.set("")
        physics_var.set("")
        chemistry_var.set("")
        compsci_var.set("")
        english_var.set("")
        avg_var.set("")
        perc_var.set("")
        res_var.set("")

    def get_cursor(self):
        cursor_row = result_table.focus()
        content = result_table.item(cursor_row)
        row = content["values"]
        Attend_var.set(row[1])
        name_var.set(row[0])
        maths_var.set(row[2])
        physics_var.set(row[3])
        chemistry_var.set(row[4])
        compsci_var.set(row[5])
        english_var.set(row[6])

    def update_rec():
        con = sql.connect(
            host="localhost",
            user="root",
            passwd="",
            database="stm"
        )
        cur = con.cursor()
        query = "update students set maths=%s,physics=%s,chemistry=%s,comp_sci=%s,english=%s,attend=%s where name=%s"
        input = [(maths_var.get(), physics_var.get(), chemistry_var.get(),
                  compsci_var.get(), english_var.get(), Attend_var.get(), name_var.get())]
        cur.executemany(query, input)
        con.commit()
        fetch_rec()
        clear_data()
        con.close()

    def delete_rec():
        con = sql.connect(
            host="localhost",
            user="root",
            passwd="",
            database="stm"
        )
        cur = con.cursor()
        cur.execute("update students set maths= NULL,physics= NULL,chemistry= NULL,comp_sci= NULL,english= NULL,attend= NULL where name = '{}'".format(name_var.get()))
        con.commit()
        con.close()
        fetch_rec()
        clear_data()
        tk.messagebox.showinfo("Your Status", "Record Deleted Successfully!")

    def gen_data():
        avg = (maths_var.get() + physics_var.get() + chemistry_var.get() + compsci_var.get() + english_var.get())/5
        perc = ((maths_var.get() + physics_var.get() + chemistry_var.get() + compsci_var.get() + english_var.get())/500)*100
        perc = str(perc) + "%"
        if maths_var.get() <= 33 or physics_var.get() <= 33 or chemistry_var.get() <= 33 or compsci_var.get() <= 33 or english_var.get() <= 33:
            result = "Fail"
        else:
            result = "Pass"
        avg_var.set(avg)
        perc_var.set(perc)
        res_var.set(result)

    #===========================================Front End===================================
    vals = []
    con = sql.connect(
        host="localhost",
        user="root",
        passwd="",
        database="stm"
    )
    cur = con.cursor()
    cur.execute("select name from students")
    rows = cur.fetchall()
    for row in rows:
        vals.append(row[0])

    root = Tk()
    root.title("Student Records Management System")
    root.geometry("1350x700+0+0")

    title = Label(root,text = "Student Records Management System",font = ("times new roman",40,"bold"),
                  bd=10,relief = GROOVE,bg="crimson",fg="white" )
    title.pack(side=TOP,fill=X)

    #============================Variables==============================================

    Attend_var = IntVar()
    name_var = StringVar()
    maths_var = IntVar()
    physics_var = IntVar()
    chemistry_var = IntVar()
    compsci_var = IntVar()
    english_var = IntVar()
    avg_var = StringVar()
    perc_var = StringVar()
    res_var = StringVar()


    #============================Manage Frame===========================================

    Manage_frame=Frame(root,bd=4,relief=RIDGE,bg="blue")
    Manage_frame.place(x=10,y=100,width=450,height=595)

    m_title=Label(Manage_frame,text="Manage Students",bg="blue",fg="white",font=("times new roman",30,"bold"))
    m_title.grid(row=0, columnspan=2,pady=20)

    lbl_attend=Label(Manage_frame,text="Attendance(365*)",bg="blue",fg="white",font=("times new roman",15,"bold"))
    lbl_attend.grid(row=2, column=0,pady=10,padx=20,sticky="w")

    txt_attend = Spinbox(Manage_frame,textvariable=Attend_var,width = 33,from_=1.0, to=365.0)
    txt_attend.grid(row=2, column=1,pady=10,padx=20,sticky="w")

    #txt_attend=Entry(Manage_frame,textvariable=Roll_No_var,bd=5,relief=GROOVE,font=("times new roman",15,"bold"))
    #txt_attend.grid(row=2, column=1,pady=10,padx=20,sticky="w")

    lbl_name=Label(Manage_frame,text="Name",bg="blue",fg="white",font=("times new roman",15,"bold"))
    lbl_name.grid(row=1, column=0,pady=10,padx=20,sticky="w")

    combo_name=ttk.Combobox(Manage_frame,textvariable=name_var,font=("times new roman",13,"bold"),state="readonly")
    combo_name['values']=vals
    combo_name.grid(row=1, column=1,pady=10,padx=20)

    '''txt_name=Entry(Manage_frame,textvariable=name_var,bd=5,relief=GROOVE,font=("times new roman",15,"bold"))
    txt_name.grid(row=2, column=1,pady=10,padx=20,sticky="w")'''

    lbl_Maths=Label(Manage_frame,text="Maths(100*)",bg="blue",fg="white",font=("times new roman",15,"bold"))
    lbl_Maths.grid(row=3, column=0,pady=10,padx=20,sticky="w")

    txt_Maths=Entry(Manage_frame,textvariable=maths_var,bd=5,relief=GROOVE,font=("times new roman",15,"bold"))
    txt_Maths.grid(row=3, column=1,pady=10,padx=20,sticky="w")

    lbl_Phy=Label(Manage_frame,text="Physics(100*)",bg="blue",fg="white",font=("times new roman",15,"bold"))
    lbl_Phy.grid(row=4, column=0,pady=10,padx=20,sticky="w")

    txt_Phy=Entry(Manage_frame,textvariable=physics_var,bd=5,relief=GROOVE,font=("times new roman",15,"bold"))
    txt_Phy.grid(row=4, column=1,pady=10,padx=20,sticky="w")

    '''combo_gender=ttk.Combobox(Manage_frame,textvariable=gender_var,font=("times new roman",13,"bold"),state="readonly")
    combo_gender['values']=("Male","Female","Others")
    combo_gender.grid(row=4, column=1,pady=10,padx=20)'''

    lbl_Chem=Label(Manage_frame,text="Chemistry(100*)",bg="blue",fg="white",font=("times new roman",15,"bold"))
    lbl_Chem.grid(row=5, column=0,pady=10,padx=20,sticky="w")

    txt_Chem=Entry(Manage_frame,textvariable=chemistry_var,bd=5,relief=GROOVE,font=("times new roman",15,"bold"))
    txt_Chem.grid(row=5, column=1,pady=10,padx=20,sticky="w")

    lbl_compsci=Label(Manage_frame,text="Comp. Sci.(100*)",bg="blue",fg="white",font=("times new roman",15,"bold"))
    lbl_compsci.grid(row=6, column=0,pady=10,padx=20,sticky="w")

    txt_compsci=Entry(Manage_frame,textvariable=compsci_var,bd=5,relief=GROOVE,font=("times new roman",15,"bold"))
    txt_compsci.grid(row=6, column=1,pady=10,padx=20,sticky="w")

    lbl_english=Label(Manage_frame,text="English(100*)",bg="blue",fg="white",font=("times new roman",15,"bold"))
    lbl_english.grid(row=7, column=0,pady=10,padx=20,sticky="w")

    txt_english=Entry(Manage_frame,bd=5,relief=GROOVE,textvariable=english_var,font=("times new roman",15,"bold"))
    txt_english.grid(row=7, column=1,pady=10,padx=20,sticky="w")

    #=============================Button Frame===========================================

    btn_frame=Frame(Manage_frame,bd=4,relief=RIDGE,bg="blue")
    btn_frame.place(x=15,y=530,width=410)

    Addbtn = Button(btn_frame,text="Add",width=10,command = add_res)
    Addbtn.grid(row=0,column=0,padx=10,pady=10)

    updatebtn = Button(btn_frame,text="Update",width=10,command = update_rec)
    updatebtn.grid(row=0,column=1,padx=10,pady=10)

    deletebtn = Button(btn_frame,text="Delete",width=10,command = delete_rec)
    deletebtn.grid(row=0,column=2,padx=10,pady=10)

    Clearbtn = Button(btn_frame,text="Clear",width=10,command = clear_data)
    Clearbtn.grid(row=0,column=3,padx=10,pady=10)

    #============================Detail Frame===========================================


    Detail_frame=Frame(root,bd=4,relief=RIDGE,bg="blue")
    Detail_frame.place(x=890,y=100,width=450,height=595)

    '''lblSearch=Label(Detail_frame,text="Search By",bg="blue",fg="white",font=("times new roman",20,"bold"))
    lblSearch.grid(row=0, column=0,pady=10,padx=20,sticky="w")

    combo_search=ttk.Combobox(Detail_frame,textvariable = search_by,width=10,font=("times new roman",12,"bold"),state="readonly")
    combo_search['values']=("roll_no","name","contact")
    combo_search.grid(row=0, column=1,pady=10,padx=20)

    txt_Search=Entry(Detail_frame,textvariable = search_txt,bd=5,relief=GROOVE,width=20,font=("times new roman",13,"bold"))
    txt_Search.grid(row=0, column=2,pady=10,padx=20,sticky="w")

    Searchbtn = Button(Detail_frame,text="Search",width=10,pady=5,command = search_data)
    Searchbtn.grid(row=0,column=3,padx=10,pady=10)

    Showallbtn = Button(Detail_frame,text="Show All",width=10,pady=5,command = fetch_data)
    Showallbtn.grid(row=0,column=4,padx=10,pady=10)'''

    #===============================Table Frame==============================

    Result_Frame=Frame(Detail_frame,bd=4,relief=RIDGE,bg="blue")
    Result_Frame.place(x=25,y=70,width=400,height=500)

    scroll_x=Scrollbar(Result_Frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(Result_Frame,orient=VERTICAL)

    result_table=ttk.Treeview(Result_Frame,
                               columns=("name","attend","maths","phy","chem","cs","eng"),
                               xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=result_table.xview)
    scroll_y.config(command=result_table.yview)

    result_table.heading("name",text="Name")
    result_table.heading("attend",text="Attendence")
    result_table.heading("maths",text="Maths")
    result_table.heading("phy",text="Phy")
    result_table.heading("chem",text="Chem")
    result_table.heading("cs",text="CS")
    result_table.heading("eng",text="Eng")

    result_table["show"]="headings"

    result_table.column('name',width=50)
    result_table.column('attend',width=50)
    result_table.column('maths',width=50)
    result_table.column('phy',width=50)
    result_table.column('chem',width=50)
    result_table.column('cs',width=50)
    result_table.column('eng',width=50)
    result_table.bind("<ButtonRelease->",get_cursor)

    result_table.pack(fill=BOTH,expand=1)
    fetch_rec()

    #=================================================Result Frame=====================================

    result_Frame=Frame(root,bd=4,relief=RIDGE,bg="blue")
    result_Frame.place(x=475,y=100,width=400,height=595)

    lbl_result = Label(result_Frame,text = "Marks Overview",bg="blue",fg="white",font=("times new roman",30,"bold"))
    lbl_result.grid(row=0, columnspan=2,pady=20)

    lbl_Avg = Label(result_Frame,text="Average",bg="blue",fg="white",font=("times new roman",20,"bold"))
    lbl_Avg.grid(row=1, column=0,pady=10,padx=20,sticky="w")

    txt_Avg = Entry(result_Frame,textvariable=avg_var,bd=5,relief=GROOVE,font=("times new roman",10,"bold"))
    txt_Avg.grid(row=1, column=1,pady=10,padx=20,sticky="w")

    lbl_perc = Label(result_Frame,text="Percentage",bg="blue",fg="white",font=("times new roman",20,"bold"))
    lbl_perc.grid(row=2, column=0,pady=10,padx=20,sticky="w")

    txt_perc = Entry(result_Frame,textvariable=perc_var,bd=5,relief=GROOVE,font=("times new roman",10,"bold"))
    txt_perc.grid(row=2, column=1,pady=10,padx=20,sticky="w")

    lbl_result = Label(result_Frame,text="Result",bg="blue",fg="white",font=("times new roman",20,"bold"))
    lbl_result.grid(row=3, column=0,pady=10,padx=20,sticky="w")

    txt_result = Entry(result_Frame,textvariable=res_var,bd=5,relief=GROOVE,font=("times new roman",10,"bold"))
    txt_result.grid(row=3, column=1,pady=10,padx=20,sticky="w")

    genframe = Frame(result_Frame,bd=4,relief=RIDGE,bg="blue")
    genframe.place(x=20,y=510,width=350)

    genover = Button(genframe,text="Generate Overview",width=30,height = 2,command = gen_data)
    genover.grid(row=0,column=0,padx=65,pady=10)

    root.mainloop()

personal(NONE)