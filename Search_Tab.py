from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as sql

def search_page(self):

    def clear_sel():
        searchall_var.set("")
        detailentry2.delete(0,END)

    def devp():
        tk.messagebox.showwarning("Status","This Field is Still Under Development")

    def kill():
        root3.destroy()

    def nextstud():
        searchby_var.set("")
        detailentry1.delete(0,END)

    def value():
        global val
        Result_Frame = Toplevel(bg="blue")
        Result_Frame.geometry("400x500+0+0")

        scroll_x = Scrollbar(Result_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Result_Frame, orient=VERTICAL)

        result_table = ttk.Treeview(Result_Frame,
                                    columns=("name", "attend", "maths", "phy", "chem", "cs", "eng"),
                                    xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=result_table.xview)
        scroll_y.config(command=result_table.yview)

        result_table.heading("name", text="Name")
        result_table.heading("attend", text="Attendence")
        result_table.heading("maths", text="Maths")
        result_table.heading("phy", text="Phy")
        result_table.heading("chem", text="Chem")
        result_table.heading("cs", text="CS")
        result_table.heading("eng", text="Eng")

        result_table["show"] = "headings"

        result_table.column('name', width=50)
        result_table.column('attend', width=50)
        result_table.column('maths', width=50)
        result_table.column('phy', width=50)
        result_table.column('chem', width=50)
        result_table.column('cs', width=50)
        result_table.column('eng', width=50)
        #result_table.bind("<ButtonRelease->", get_cursor)

        result_table.pack(fill=BOTH, expand=1)
        con = sql.connect(host = "localhost",
                          user = "root",
                          passwd = "",
                          database = "stm")
        cur = con.cursor()
        cur.execute("select name,attend,maths,physics,chemistry,comp_sci,english from students where {} = '{}'".format(searchby_var.get(),detailentry1.get()))
        rows = cur.fetchall()
        val = []
        for i in rows:
            for j in i:
                val.append(j)
        if len(rows) != 0:
            result_table.delete(*result_table.get_children())
            for row in rows:
                result_table.insert("", END, values=row)
        con.close()

    def graph():
        import matplotlib.pyplot as pt
        import numpy as np
        con = sql.connect(host = "localhost",
                          user = "root",
                          passwd = "",
                          database = "stm")
        cur = con.cursor()
        cur.execute("select name,attend,maths,physics,chemistry,comp_sci,english from students where {} = '{}'".format(searchby_var.get(),detailentry1.get()))
        rows = cur.fetchall()
        val = []
        for i in rows:
            for j in i:
                val.append(j)
        p = []
        for i in range(2,len(val)):
            p.append(val[i])
        marks = ['Maths', 'Phy', 'Chem', 'CS',"Eng"]

        x = np.arange(len(p))

        pt.bar(x, p, width=0.35, color='b', align="center")
        title = "Marks Analysis of " + (val[0])
        pt.title(title)
        pt.ylabel("Marks->")
        pt.xticks(x, marks)
        #pt.ylim(100)
        pt.show()

    root3 = Tk()
    root3.geometry("793x564+300+102")
    root3.title("New Toplevel")
    root3.configure(background="#ffff2e")
    root3.configure(highlightbackground="#d9d9d9")
    root3.configure(highlightcolor="black")

    _bgcolor = '#0da2d8'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'

#==================================VARIABLES===============================================

    searchby_var = StringVar()
    search1 = StringVar()
    searchall_var = StringVar()
    search2 = StringVar()

#============================================Mainframe=================================================

    mainframe = tk.Frame(root3)
    mainframe.place(relx=0.0, rely=0.009, relheight=0.984
                , relwidth=0.99)

    mainframe.configure(relief='groove')
    mainframe.configure(borderwidth="2")
    mainframe.configure(relief="groove")
    mainframe.configure(background="#0da2d8")
    mainframe.configure(highlightbackground="#d9d9d9")
    mainframe.configure(highlightcolor="black")

    lblHeading = tk.Label(mainframe)
    lblHeading.place(relx=0.006, rely=0.01, height=51, width=774)
    lblHeading.configure(activebackground="#f9f9f9")
    lblHeading.configure(activeforeground="black")
    lblHeading.configure(background="#d8bec0")
    lblHeading.configure(disabledforeground="#a3a3a3")
    lblHeading.configure(font="-family {Modern No. 20} -size 20 -weight bold")
    lblHeading.configure(foreground="#000000")
    lblHeading.configure(highlightbackground="#d9d9d9")
    lblHeading.configure(highlightcolor="black")
    lblHeading.configure(text='''Student Marks Portal''')

#===============================1st SubFrame===================================================

    frame1 = tk.Frame(mainframe)
    frame1.place(relx=0.025, rely=0.126, relheight=0.766
                , relwidth=0.541)
    frame1.configure(relief='groove')
    frame1.configure(borderwidth="2")
    frame1.configure(relief="groove")
    frame1.configure(background="#d80606")
    frame1.configure(highlightbackground="#d9d9d9")
    frame1.configure(highlightcolor="black")

    lblsearchindi = tk.Label(frame1)
    lblsearchindi.place(relx=0.282, rely=0.047, height=41, width=184)
    lblsearchindi.configure(activebackground="#f9f9f9")
    lblsearchindi.configure(activeforeground="black")
    lblsearchindi.configure(background="#d80606")
    lblsearchindi.configure(disabledforeground="#a3a3a3")
    lblsearchindi.configure(font="-family {Segoe UI} -size 12 -weight bold")
    lblsearchindi.configure(foreground="#000000")
    lblsearchindi.configure(highlightbackground="#d9d9d9")
    lblsearchindi.configure(highlightcolor="black")
    lblsearchindi.configure(text='''Search Individual''')

    lblsearchby1 = tk.Label(frame1)
    lblsearchby1.place(relx=0.047, rely=0.235, height=31, width=94)
    lblsearchby1.configure(activebackground="#f9f9f9")
    lblsearchby1.configure(activeforeground="black")
    lblsearchby1.configure(background="#d80606")
    lblsearchby1.configure(disabledforeground="#a3a3a3")
    lblsearchby1.configure(font="-family {Segoe UI} -size 10 -weight bold")
    lblsearchby1.configure(foreground="#000000")
    lblsearchby1.configure(highlightbackground="#d9d9d9")
    lblsearchby1.configure(highlightcolor="black")
    lblsearchby1.configure(text='''Search By :''')

    '''searchbymenu1 = tk.Entry(frame1)
    searchbymenu1.place(relx=0.376, rely=0.235, height=30
                        , relwidth=0.48)
    searchbymenu1.configure(background="white")
    searchbymenu1.configure(disabledforeground="#a3a3a3")
    searchbymenu1.configure(font="-family {Courier New} -size 10")
    searchbymenu1.configure(foreground="#000000")
    searchbymenu1.configure(highlightbackground="#d9d9d9")
    searchbymenu1.configure(highlightcolor="black")
    searchbymenu1.configure(insertbackground="black")
    searchbymenu1.configure(selectbackground="#c4c4c4")
    searchbymenu1.configure(selectforeground="black")'''

    searchbymenu1 = ttk.Combobox(frame1,textvariable=searchby_var,font=("times new roman",13,"bold"),state="readonly")
    searchbymenu1['values']=("roll_no","name")
    searchbymenu1.place(relx=0.376, rely=0.235, height=30
                        , relwidth=0.48)

    lbldetail1 = tk.Label(frame1)
    lbldetail1.place(relx=0.071, rely=0.376, height=31, width=124)
    lbldetail1.configure(activebackground="#f9f9f9")
    lbldetail1.configure(activeforeground="black")
    lbldetail1.configure(background="#d80606")
    lbldetail1.configure(disabledforeground="#a3a3a3")
    lbldetail1.configure(font="-family {Segoe UI} -size 10 -weight bold")
    lbldetail1.configure(foreground="#000000")
    lbldetail1.configure(highlightbackground="#d9d9d9")
    lbldetail1.configure(highlightcolor="black")
    lbldetail1.configure(text='''Enter Detail Here :''')

    detailentry1 = tk.Entry(frame1,textvariable = search1)
    detailentry1.place(relx=0.376, rely=0.376, height=30, relwidth=0.48)

    detailentry1.configure(background="white")
    detailentry1.configure(disabledforeground="#a3a3a3")
    detailentry1.configure(font="-family {Courier New} -size 10")
    detailentry1.configure(foreground="#000000")
    detailentry1.configure(highlightbackground="#d9d9d9")
    detailentry1.configure(highlightcolor="black")
    detailentry1.configure(insertbackground="black")
    detailentry1.configure(selectbackground="#c4c4c4")
    detailentry1.configure(selectforeground="black")

    btnshow1 = tk.Button(frame1)
    btnshow1.place(relx=0.329, rely=0.518, height=44, width=167)
    btnshow1.configure(activebackground="#ececec")
    btnshow1.configure(activeforeground="#000000")
    btnshow1.configure(background="#0da2d8")
    btnshow1.configure(disabledforeground="#a3a3a3")
    btnshow1.configure(font="-family {Segoe UI} -size 12")
    btnshow1.configure(foreground="#000000")
    btnshow1.configure(highlightbackground="#0da2d8")
    btnshow1.configure(highlightcolor="black")
    btnshow1.configure(pady="0")
    btnshow1.configure(text='''Show Details''',command = value)

    btngraph1 = tk.Button(frame1)
    btngraph1.place(relx=0.329, rely=0.647, height=44, width=167)
    btngraph1.configure(activebackground="#ececec")
    btngraph1.configure(activeforeground="#000000")
    btngraph1.configure(background="#0da2d8")
    btngraph1.configure(disabledforeground="#a3a3a3")
    btngraph1.configure(font="-family {Segoe UI} -size 12")
    btngraph1.configure(foreground="#000000")
    btngraph1.configure(highlightbackground="#0da2d8")
    btngraph1.configure(highlightcolor="black")
    btngraph1.configure(pady="0")
    btngraph1.configure(text='''Analyse Performance''',command = graph)

    btnclr1 = tk.Button(frame1)
    btnclr1.place(relx=0.353, rely=0.824, height=44, width=147)
    btnclr1.configure(activebackground="#ececec")
    btnclr1.configure(activeforeground="#000000")
    btnclr1.configure(background="#0da2d8")
    btnclr1.configure(disabledforeground="#a3a3a3")
    btnclr1.configure(font="-family {Segoe UI} -size 9 -weight bold")
    btnclr1.configure(foreground="#000000")
    btnclr1.configure(highlightbackground="#0da2d8")
    btnclr1.configure(highlightcolor="black")
    btnclr1.configure(pady="0")
    btnclr1.configure(text='''Next Student''',command = nextstud)

#===============================1st SubFrame===================================================

    frame2 = tk.Frame(mainframe)
    frame2.place(relx=0.586, rely=0.126, relheight=0.766
                , relwidth=0.376)
    frame2.configure(relief='groove')
    frame2.configure(borderwidth="2")
    frame2.configure(relief="groove")
    frame2.configure(background="#d80606")
    frame2.configure(highlightbackground="#d9d9d9")
    frame2.configure(highlightcolor="black")

    lblsearchall = tk.Label(frame2)
    lblsearchall.place(relx=0.271, rely=0.047, height=41, width=154)
    lblsearchall.configure(activebackground="#f9f9f9")
    lblsearchall.configure(activeforeground="black")
    lblsearchall.configure(background="#d80606")
    lblsearchall.configure(disabledforeground="#a3a3a3")
    lblsearchall.configure(font="-family {Segoe UI} -size 12 -weight bold")
    lblsearchall.configure(foreground="#000000")
    lblsearchall.configure(highlightbackground="#d9d9d9")
    lblsearchall.configure(highlightcolor="black")
    lblsearchall.configure(text='''Search All''')

    lblsearchby2 = tk.Label(frame2)
    lblsearchby2.place(relx=0.034, rely=0.235, height=31, width=84)
    lblsearchby2.configure(activebackground="#f9f9f9")
    lblsearchby2.configure(activeforeground="black")
    lblsearchby2.configure(background="#d80606")
    lblsearchby2.configure(disabledforeground="#a3a3a3")
    lblsearchby2.configure(font="-family {Segoe UI} -size 10 -weight bold")
    lblsearchby2.configure(foreground="#000000")
    lblsearchby2.configure(highlightbackground="#d9d9d9")
    lblsearchby2.configure(highlightcolor="black")
    lblsearchby2.configure(text='''Search By:''')

    '''searchbymenu2 = tk.Entry(frame2)
    searchbymenu2.place(relx=0.305, rely=0.235, height=30
                        , relwidth=0.556)
    searchbymenu2.configure(background="white")
    searchbymenu2.configure(disabledforeground="#a3a3a3")
    searchbymenu2.configure(font="-family {Courier New} -size 10")
    searchbymenu2.configure(foreground="#000000")
    searchbymenu2.configure(highlightbackground="#d9d9d9")
    searchbymenu2.configure(highlightcolor="black")
    searchbymenu2.configure(insertbackground="black")
    searchbymenu2.configure(selectbackground="#c4c4c4")
    searchbymenu2.configure(selectforeground="black")'''

    searchbymenu2 = ttk.Combobox(frame2,textvariable=searchall_var,font=("times new roman",13,"bold"),state="readonly")
    searchbymenu2['values']=("Class","Subject","Result")
    searchbymenu2.place(relx=0.305, rely=0.235, height=30
                        , relwidth=0.556)

    lbldetail2 = tk.Label(frame2)
    lbldetail2.place(relx=0.068, rely=0.376, height=41, width=64)
    lbldetail2.configure(activebackground="#f9f9f9")
    lbldetail2.configure(activeforeground="black")
    lbldetail2.configure(background="#d80606")
    lbldetail2.configure(disabledforeground="#a3a3a3")
    lbldetail2.configure(font="-family {Segoe UI} -size 10 -weight bold")
    lbldetail2.configure(foreground="#000000")
    lbldetail2.configure(highlightbackground="#d9d9d9")
    lbldetail2.configure(highlightcolor="black")
    lbldetail2.configure(text='''Detail :''')

    detailentry2 = tk.Entry(frame2,textvariable = search2)
    detailentry2.place(relx=0.305, rely=0.388, height=30
                       , relwidth=0.556)
    detailentry2.configure(background="white")
    detailentry2.configure(disabledforeground="#a3a3a3")
    detailentry2.configure(font="-family {Courier New} -size 10")
    detailentry2.configure(foreground="#000000")
    detailentry2.configure(highlightbackground="#d9d9d9")
    detailentry2.configure(highlightcolor="black")
    detailentry2.configure(insertbackground="black")
    detailentry2.configure(selectbackground="#c4c4c4")
    detailentry2.configure(selectforeground="black")

    btnshow2 = tk.Button(frame2)
    btnshow2.place(relx=0.237, rely=0.518, height=44, width=167)
    btnshow2.configure(activebackground="#ececec")
    btnshow2.configure(activeforeground="#000000")
    btnshow2.configure(background="#0da2d8")
    btnshow2.configure(disabledforeground="#a3a3a3")
    btnshow2.configure(font="-family {Segoe UI} -size 12")
    btnshow2.configure(foreground="#000000")
    btnshow2.configure(highlightbackground="#0da2d8")
    btnshow2.configure(highlightcolor="black")
    btnshow2.configure(pady="0")
    btnshow2.configure(text='''Show Details''',command = devp)

    btngraph2 = tk.Button(frame2)
    btngraph2.place(relx=0.237, rely=0.659, height=44, width=167)
    btngraph2.configure(activebackground="#ececec")
    btngraph2.configure(activeforeground="#000000")
    btngraph2.configure(background="#0da2d8")
    btngraph2.configure(disabledforeground="#a3a3a3")
    btngraph2.configure(font="-family {Segoe UI} -size 12")
    btngraph2.configure(foreground="#000000")
    btngraph2.configure(highlightbackground="#0da2d8")
    btngraph2.configure(highlightcolor="black")
    btngraph2.configure(pady="0")
    btngraph2.configure(text='''Analyse Performance''',command = devp)

    btnclr2 = tk.Button(frame2)
    btnclr2.place(relx=0.288, rely=0.835, height=44, width=147)
    btnclr2.configure(activebackground="#ececec")
    btnclr2.configure(activeforeground="#000000")
    btnclr2.configure(background="#0da2d8")
    btnclr2.configure(disabledforeground="#a3a3a3")
    btnclr2.configure(font="-family {Segoe UI} -size 9 -weight bold")
    btnclr2.configure(foreground="#000000")
    btnclr2.configure(highlightbackground="#0da2d8")
    btnclr2.configure(highlightcolor="black")
    btnclr2.configure(pady="0")
    btnclr2.configure(text='''Clear Selection''',command = clear_sel)

    btngoback = tk.Button(mainframe)
    btngoback.place(relx=0.331, rely=0.901, height=44, width=137)
    btngoback.configure(activebackground="#ececec")
    btngoback.configure(activeforeground="#000000")
    btngoback.configure(background="#d80606")
    btngoback.configure(disabledforeground="#a3a3a3")
    btngoback.configure(foreground="#ffffff")
    btngoback.configure(highlightbackground="#0da2d8")
    btngoback.configure(highlightcolor="black")
    btngoback.configure(pady="0")
    btngoback.configure(text='''Go Back''',command = kill)

    btnlogout = tk.Button(mainframe)
    btnlogout.place(relx=0.522, rely=0.901, height=44, width=137)
    btnlogout.configure(activebackground="#ececec")
    btnlogout.configure(activeforeground="#000000")
    btnlogout.configure(background="#d80606")
    btnlogout.configure(disabledforeground="#a3a3a3")
    btnlogout.configure(foreground="#ffffff")
    btnlogout.configure(highlightbackground="#0da2d8")
    btnlogout.configure(highlightcolor="black")
    btnlogout.configure(pady="0")
    btnlogout.configure(text='''Logout''',command = kill)

    root3.mainloop()

search_page(NONE)