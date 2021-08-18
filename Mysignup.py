from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import webbrowser as wb
from tkcalendar import *
import STUDENT_DATABASE_MANAGEMENT_SYSTEM_Backend as stdbck



google_url = "www.myaccount.google.com"
facebook_url = "www.facebook.com"

def google():
    wb.open_new(google_url)

def facebook():
    wb.open_new(facebook_url)



def signup(self):
    def create():
        userids = []
        userdetail = stdbck.showdata()
        for a in userdetail:
            userids.append(a[3])

        if len(entername.get()) == 0 or len(enteremail.get()) == 0 or len(enteruser.get()) == 0 or len(
                enterpass.get()) == 0 or len(Gender_var.get()) == 0 or len(dobentry.get()) == 0:
            tk.messagebox.showerror("Error!", "All fields are required!")
        else:
            if enterpass.get() != enterrepass.get():
                tk.messagebox.showerror("Error!", "Passwords Doesn't Match!")
                enterpass.delete(0, END)
                enterrepass.delete(0, END)
            elif (enteruser.get()) in userids:
                tk.messagebox.showerror("Error!", "Username Already Taken!")
                enteruser.delete(0, END)
            else:
                stdbck.create(entername.get(), dobentry.get(), enteremail.get(), enteruser.get(), Gender_var.get(),
                              enterpass.get())
                tk.messagebox.showinfo("Your Status", "Account Successfully Created")

    root4 = Tk()
    root4.geometry("1207x580+-30+115")
    root4.title("Sign Up Page")
    root4.configure(background="#231c8c")
    root4.configure(highlightbackground="#d9d9d9")
    root4.configure(highlightcolor="black")

    _bgcolor = '#0da2d8'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font11 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
        "roman -underline 0 -overstrike 0"
    font12 = "-family {Segoe UI} -size 12 -weight bold -slant "  \
         "roman -underline 0 -overstrike 0"

    '''logo = PhotoImage(file="Images\Logo.png")
    user_logo = PhotoImage(file="Images\man-user.png")
    pass_logo = PhotoImage(file="Images\Password.png")
    google_login = PhotoImage(file="Images\googlenew.png")
    facebook_login = PhotoImage(file="Images\Facebooknew.png")'''
    google_login = PhotoImage(file="Images\googlenew.png")
    facebook_login = PhotoImage(file="Images\Facebooknew.png")

    Gender_var = StringVar()

    rightframe = tk.Frame(root4)
    rightframe.place(relx=0.166, rely=0.121, relheight=1.06
                     , relwidth=0.493)
    rightframe.configure(relief='groove')
    rightframe.configure(borderwidth="2")
    rightframe.configure(relief="groove")
    rightframe.configure(background="#0da2d8")
    rightframe.configure(highlightbackground="#d9d9d9")
    rightframe.configure(highlightcolor="black")

    lblname = tk.Label(rightframe)
    lblname.place(relx=0.076, rely=0.13, height=41, width=94)
    lblname.configure(activebackground="#f9f9f9")
    lblname.configure(activeforeground="black")
    lblname.configure(background="#0da2d8")
    lblname.configure(disabledforeground="#a3a3a3")
    lblname.configure(font="-family {Georgia} -size 13 -weight bold")
    lblname.configure(foreground="#000000")
    lblname.configure(highlightbackground="#d9d9d9")
    lblname.configure(highlightcolor="black")
    lblname.configure(text='''Name :''')

    lblemail = tk.Label(rightframe)
    lblemail.place(relx=0.076, rely=0.22, height=31, width=174)
    lblemail.configure(activebackground="#f9f9f9")
    lblemail.configure(activeforeground="black")
    lblemail.configure(background="#0da2d8")
    lblemail.configure(disabledforeground="#a3a3a3")
    lblemail.configure(font="-family {Georgia} -size 13 -weight bold")
    lblemail.configure(foreground="#000000")
    lblemail.configure(highlightbackground="#d9d9d9")
    lblemail.configure(highlightcolor="black")
    lblemail.configure(text='''Email Address :''')

    lblgender = tk.Label(rightframe)
    lblgender.place(relx=0.101, rely=0.309, height=26, width=84)
    lblgender.configure(activebackground="#f9f9f9")
    lblgender.configure(activeforeground="black")
    lblgender.configure(background="#0da2d8")
    lblgender.configure(disabledforeground="#a3a3a3")
    lblgender.configure(font="-family {Georgia} -size 13 -weight bold")
    lblgender.configure(foreground="#000000")
    lblgender.configure(highlightbackground="#d9d9d9")
    lblgender.configure(highlightcolor="black")
    lblgender.configure(text='''Gender :''')

    lbldob = tk.Label(rightframe)
    lbldob.place(relx=0.101, rely=0.39, height=26, width=75)
    lbldob.configure(activebackground="#f9f9f9")
    lbldob.configure(activeforeground="black")
    lbldob.configure(background="#0da2d8")
    lbldob.configure(disabledforeground="#a3a3a3")
    lbldob.configure(font="-family {Georgia} -size 13 -weight bold")
    lbldob.configure(foreground="#000000")
    lbldob.configure(highlightbackground="#d9d9d9")
    lbldob.configure(highlightcolor="black")
    lbldob.configure(text='''D.O.B. :''')

    lbluser = tk.Label(rightframe)
    lbluser.place(relx=0.067, rely=0.472, height=21, width=214)
    lbluser.configure(activebackground="#f9f9f9")
    lbluser.configure(activeforeground="black")
    lbluser.configure(background="#0da2d8")
    lbluser.configure(disabledforeground="#a3a3a3")
    lbluser.configure(font="-family {Georgia} -size 13 -weight bold")
    lbluser.configure(foreground="#000000")
    lbluser.configure(highlightbackground="#d9d9d9")
    lbluser.configure(highlightcolor="black")
    lbluser.configure(text='''Choose Username :''')

    lblpass = tk.Label(rightframe)
    lblpass.place(relx=0.084, rely=0.553, height=31, width=194)
    lblpass.configure(activebackground="#f9f9f9")
    lblpass.configure(activeforeground="black")
    lblpass.configure(background="#0da2d8")
    lblpass.configure(disabledforeground="#a3a3a3")
    lblpass.configure(font="-family {Georgia} -size 13 -weight bold")
    lblpass.configure(foreground="#000000")
    lblpass.configure(highlightbackground="#d9d9d9")
    lblpass.configure(highlightcolor="black")
    lblpass.configure(text='''Choose Password :''')

    lblrepass = tk.Label(rightframe)
    lblrepass.place(relx=0.084, rely=0.626, height=41, width=204)
    lblrepass.configure(activebackground="#f9f9f9")
    lblrepass.configure(activeforeground="black")
    lblrepass.configure(background="#0da2d8")
    lblrepass.configure(disabledforeground="#a3a3a3")
    lblrepass.configure(font="-family {Georgia} -size 13 -weight bold")
    lblrepass.configure(foreground="#000000")
    lblrepass.configure(highlightbackground="#d9d9d9")
    lblrepass.configure(highlightcolor="black")
    lblrepass.configure(text='''Re-Enter Password :''')

    entername = tk.Entry(rightframe)
    entername.place(relx=0.437, rely=0.146, height=30, relwidth=0.343)
    entername.configure(background="white")
    entername.configure(disabledforeground="#a3a3a3")
    entername.configure(font="-family {Courier New} -size 10")
    entername.configure(foreground="#000000")
    entername.configure(insertbackground="black")

    enteremail = tk.Entry(rightframe)
    enteremail.place(relx=0.437, rely=0.228, height=30, relwidth=0.343)
    enteremail.configure(background="white")
    enteremail.configure(disabledforeground="#a3a3a3")
    enteremail.configure(font="-family {Courier New} -size 10")
    enteremail.configure(foreground="#000000")
    enteremail.configure(insertbackground="black")

    '''entergender = tk.Entry(rightframe)
    entergender.place(relx=0.437, rely=0.309, height=30, relwidth=0.343)
    
    entergender.configure(background="white")
    entergender.configure(disabledforeground="#a3a3a3")
    entergender.configure(font="-family {Courier New} -size 10")
    entergender.configure(foreground="#000000")
    entergender.configure(insertbackground="black")'''

    _gender=ttk.Combobox(rightframe,textvariable=Gender_var,font=("times new roman",13,"bold"),state="readonly")
    _gender['values']=("Male","Female","Others")
    _gender.place(relx=0.437, rely=0.309, height=30, relwidth=0.343)

    '''enterdob = tk.Entry(rightframe)
    enterdob.place(relx=0.437, rely=0.39, height=30, relwidth=0.343)
    enterdob.configure(background="white")
    enterdob.configure(disabledforeground="#a3a3a3")
    enterdob.configure(font="-family {Courier New} -size 10")
    enterdob.configure(foreground="#000000")
    enterdob.configure(insertbackground="black")'''

    dateframe = Frame(rightframe)
    dateframe.place(relx=0.437, rely=0.39, height=30, relwidth=0.343)
    dateframe.configure(relief='groove')
    dateframe.configure(borderwidth="2")
    dateframe.configure(relief="groove")
    dateframe.configure(background="white")

    dobentry = DateEntry(dateframe, width=40, background="blue", foreground="white", borderwidth=2)
    dobentry.pack(padx=5, pady=5)

    enteruser = tk.Entry(rightframe)
    enteruser.place(relx=0.437, rely=0.472, height=30, relwidth=0.343)
    enteruser.configure(background="white")
    enteruser.configure(disabledforeground="#a3a3a3")
    enteruser.configure(font="-family {Courier New} -size 10")
    enteruser.configure(foreground="#000000")
    enteruser.configure(insertbackground="black")

    enterpass = tk.Entry(rightframe,show = "*")
    enterpass.place(relx=0.437, rely=0.553, height=30, relwidth=0.343)
    enterpass.configure(background="white")
    enterpass.configure(disabledforeground="#a3a3a3")
    enterpass.configure(font="-family {Courier New} -size 10")
    enterpass.configure(foreground="#000000")
    enterpass.configure(insertbackground="black")

    enterrepass = tk.Entry(rightframe,show = "*")
    enterrepass.place(relx=0.437, rely=0.634, height=30, relwidth=0.343)

    enterrepass.configure(background="white")
    enterrepass.configure(disabledforeground="#a3a3a3")
    enterrepass.configure(font="-family {Courier New} -size 10")
    enterrepass.configure(foreground="#000000")
    enterrepass.configure(insertbackground="black")

    btncreate = tk.Button(rightframe)
    btncreate.place(relx=0.303, rely=0.764, height=44, width=227)
    btncreate.configure(activebackground="#ececec")
    btncreate.configure(activeforeground="#000000")
    btncreate.configure(background="green")
    btncreate.configure(disabledforeground="#a3a3a3")
    btncreate.configure(font=font12)
    btncreate.configure(foreground="#ffffff")
    btncreate.configure(highlightbackground="#0da2d8")
    btncreate.configure(highlightcolor="black")
    btncreate.configure(pady="0")
    btncreate.configure(text='''Confirm & Create''',command = create)

    leftframe = tk.Frame(root4)
    leftframe.place(relx=0.655, rely=0.121, relheight=1.06
                    , relwidth=0.302)
    leftframe.configure(relief='groove')
    leftframe.configure(borderwidth="2")
    leftframe.configure(relief="groove")
    leftframe.configure(background="#ffffff")
    leftframe.configure(highlightbackground="#d9d9d9")
    leftframe.configure(highlightcolor="black")

    lbltry = tk.Label(leftframe)
    lbltry.place(relx=0.219, rely=0.13, height=31, width=214)
    lbltry.configure(background="#ffffff")
    lbltry.configure(disabledforeground="#a3a3a3")
    lbltry.configure(font=font11)
    lbltry.configure(foreground="#000000")
    lbltry.configure(text='''or Try Signing Up Using''')

    btnfacebook = tk.Button(leftframe,image = facebook_login)
    btnfacebook.place(relx=0.164, rely=0.211, height=54, width=267)
    btnfacebook.configure(activebackground="#ececec")
    btnfacebook.configure(activeforeground="#000000")
    btnfacebook.configure(background="#ffffff")
    btnfacebook.configure(borderwidth="2")
    btnfacebook.configure(disabledforeground="#a3a3a3")
    btnfacebook.configure(foreground="#ffffff")
    btnfacebook.configure(highlightbackground="#0da2d8")
    btnfacebook.configure(highlightcolor="black")
    btnfacebook.configure(pady="0",command = facebook)

    lblor = tk.Label(leftframe)
    lblor.place(relx=0.438, rely=0.309, height=31, width=64)
    lblor.configure(background="#ffffff")
    lblor.configure(disabledforeground="#a3a3a3")
    lblor.configure(font=font11)
    lblor.configure(foreground="#000000")
    lblor.configure(text='''Or''')

    btnloginpage = tk.Button(leftframe)
    btnloginpage.place(relx=0.192, rely=0.764, height=44, width=257)
    btnloginpage.configure(activebackground="#ececec")
    btnloginpage.configure(activeforeground="#000000")
    btnloginpage.configure(background="#ff0000")
    btnloginpage.configure(disabledforeground="#a3a3a3")
    btnloginpage.configure(foreground="#ffffff")
    btnloginpage.configure(highlightbackground="#0da2d8")
    btnloginpage.configure(highlightcolor="black")
    btnloginpage.configure(pady="0")
    btnloginpage.configure(text='''Login Here''')

    btngoogle = tk.Button(leftframe,image = google_login)
    btngoogle.place(relx=0.164, rely=0.374, height=54, width=267)
    btngoogle.configure(activebackground="#ececec")
    btngoogle.configure(activeforeground="#000000")
    btngoogle.configure(background="#ffffff")
    btngoogle.configure(borderwidth="2")
    btngoogle.configure(disabledforeground="#a3a3a3")
    btngoogle.configure(foreground="#000000")
    btngoogle.configure(highlightbackground="#0da2d8")
    btngoogle.configure(highlightcolor="black")
    btngoogle.configure(pady="0",command = google)

    lbllogin = tk.Label(leftframe)
    lbllogin.place(relx=0.247, rely=0.667, height=41, width=224)
    lbllogin.configure(background="#ffffff")
    lbllogin.configure(disabledforeground="#a3a3a3")
    lbllogin.configure(font=font11)
    lbllogin.configure(foreground="#000000")
    lbllogin.configure(text='''Already Have An Account?''')

    lblsignup = tk.Label(root4)
    lblsignup.place(relx=0.331, rely=0.017, height=41, width=474)
    lblsignup.configure(activebackground="#f9f9f9")
    lblsignup.configure(activeforeground="black")
    lblsignup.configure(background="#231c8c")
    lblsignup.configure(disabledforeground="#a3a3a3")
    lblsignup.configure(font="-family {Segoe UI} -size 24 -weight bold")
    lblsignup.configure(foreground="#ffffff")
    lblsignup.configure(highlightbackground="#d9d9d9")
    lblsignup.configure(highlightcolor="black")
    lblsignup.configure(text='''Sign Up Here''')

    root4.mainloop()

signup(NONE)