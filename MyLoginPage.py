from tkinter import *
import tkinter as tk
from tkinter import messagebox
import webbrowser as wb
import STUDENT_DATABASE_MANAGEMENT_SYSTEM_Backend as stdbck



google_url = "www.myaccount.google.com"
facebook_url = "www.facebook.com"

def google():
    wb.open_new(google_url)
def facebook():
    wb.open_new(facebook_url)

def forgotpass():
    """forgpass = So What!?
    its non of my Business!
    """
    tk.messagebox.showerror("Forgot Password??","So What!?\nIts non of my Business!\nGet off here!!")



def loginpage(self):
    root1 = Tk()
    root1.title("Login ~Sai Prasad & Aditya Mishra & Hritik Sharma")
    root1.geometry("965x619+206+70")
    root1.configure(background="#ffffff")
    root1.configure(highlightbackground="#d9d9d9")
    root1.configure(highlightcolor="black")

    font11 = "-family Shrewsbury -size 11 -weight bold -slant " \
             "roman -underline 0 -overstrike 0"
    font13 = "-family {Segoe UI} -size 13 -weight normal -slant " \
             "roman -underline 0 -overstrike 0"
    font15 = "-family {Segoe UI} -size 11 -weight normal -slant " \
             "roman -underline 0 -overstrike 0"

    def login_now():
        data = {}
        a = stdbck.showdata()
        for i in a:
            data[i[-3]] = i[-1]
        user = txtuser.get()
        passwd = txtpass.get()
        try:
            if passwd == data[user]:
                txtuser.delete(0,END)
                txtpass.delete(0,END)
                tk.messagebox.showinfo("LOGIN STATUS", "Login successful")
                # print("Login successful")
            if passwd != data[user]:
                #txtuser.delete(0,END)
                txtpass.delete(0,END)
                tk.messagebox.showinfo("LOGIN STATUS", "Incorrect password")
                # print("Incorrect password")
        except Exception:
            #txtuser.delete(0,END)
            txtpass.delete(0,END)# print("username-INCORRECT/CASE SENSITIVE")
            tk.messagebox.showwarning("Incorrect credentials", "Username and Password not detected!")

    username = StringVar()
    password = StringVar()

    logo = PhotoImage(file="Images\Logo.png")
    user_logo = PhotoImage(file="Images\man-user.png")
    pass_logo = PhotoImage(file="Images\Password.png")
    google_login = PhotoImage(file="Images\googlenew.png")
    facebook_login = PhotoImage(file="Images\Facebooknew.png")

    Frame1 = Frame(root1)
    Frame1.place(relx=0.01, rely=0.065, relheight=0.929, relwidth=0.979)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="6")
    Frame1.configure(relief="groove")
    Frame1.configure(background="#d8cbcb")
    Frame1.configure(highlightbackground="#d9d9d9")
    Frame1.configure(highlightcolor="black")

    Frame3 = tk.Frame(Frame1)
    Frame3.place(relx=0.005, rely=0.017, relheight=0.113,relwidth=0.989)
    Frame3.configure(relief='groove')
    Frame3.configure(borderwidth="2")
    Frame3.configure(relief="groove")
    Frame3.configure(background="#d89595")
    Frame3.configure(highlightbackground="#d9d9d9")
    Frame3.configure(highlightcolor="black")

    Label1 = tk.Label(Frame3)
    Label1.place(relx=-0.021, rely=0.0, height=61, width=184)
    Label1.configure(activebackground="#f9f9f9")
    Label1.configure(activeforeground="black")
    Label1.configure(background="#d89595")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(font="-family {Agency} -size 30 -weight bold")
    Label1.configure(foreground="#000000")
    Label1.configure(highlightbackground="#d9d9d9")
    Label1.configure(highlightcolor="black")
    Label1.configure(text='''Welcome..''')

    Frame2 = tk.Frame(Frame1)
    Frame2.place(relx=0.011, rely=0.139, relheight=0.843
                 , relwidth=0.386)
    Frame2.configure(relief='groove')
    Frame2.configure(borderwidth="2")
    Frame2.configure(relief="groove")
    Frame2.configure(background="#d8cbcb")

    lbldont = Label(Frame2)
    lbldont.place(relx=0.219, rely=0.082, height=41, width=204)
    lbldont.configure(background="#d8cbcb")
    lbldont.configure(disabledforeground="#a3a3a3")
    lbldont.configure(font=font13)
    lbldont.configure(foreground="#000000")
    lbldont.configure(text='''Don't have an account?''')

    lblor1 = Label(Frame2)
    lblor1.place(relx=0.356, rely=0.206, height=21, width=84)
    lblor1.configure(background="#d8cbcb")
    lblor1.configure(disabledforeground="#a3a3a3")
    lblor1.configure(foreground="#000000")
    lblor1.configure(text='''OR''')

    btnsignup = Button(Frame2)
    btnsignup.place(relx=0.301, rely=0.165, height=24, width=137)
    btnsignup.configure(activebackground="#ececec")
    btnsignup.configure(activeforeground="#000000")
    btnsignup.configure(background="#d8cbcb")
    btnsignup.configure(borderwidth="0")
    btnsignup.configure(disabledforeground="#a3a3a3")
    btnsignup.configure(font=font15)
    btnsignup.configure(foreground="#0d4dff")
    btnsignup.configure(highlightbackground="#0da2d8")
    btnsignup.configure(highlightcolor="black")
    btnsignup.configure(pady="0")
    btnsignup.configure(text='''Sign Up''')

    imagefacebook = Button(Frame2,image = facebook_login)
    imagefacebook.place(relx=0.137, rely=0.309, height=44, width=247)
    imagefacebook.configure(activebackground="#ececec")
    imagefacebook.configure(activeforeground="#000000")
    imagefacebook.configure(background="#ffffff")
    imagefacebook.configure(borderwidth="0")
    imagefacebook.configure(disabledforeground="#a3a3a3")
    imagefacebook.configure(foreground="#000000")
    imagefacebook.configure(highlightbackground="#0da2d8")
    imagefacebook.configure(highlightcolor="black")
    imagefacebook.configure(pady="0")
    imagefacebook.configure(text='''facebook''',command = facebook)

    imagegoogle = Button(Frame2,image = google_login)
    imagegoogle.place(relx=0.137, rely=0.495, height=44, width=247)
    imagegoogle.configure(activebackground="#ececec")
    imagegoogle.configure(activeforeground="#000000")
    imagegoogle.configure(background="#ffffff")
    imagegoogle.configure(borderwidth="0")
    imagegoogle.configure(disabledforeground="#a3a3a3")
    imagegoogle.configure(foreground="#000000")
    imagegoogle.configure(highlightbackground="#0da2d8")
    imagegoogle.configure(highlightcolor="black")
    imagegoogle.configure(pady="0")
    imagegoogle.configure(text='''google''',command = google)

    Frame4 = tk.Frame(Frame1)
    Frame4.place(relx=0.402, rely=0.139, relheight=0.843, relwidth=0.598)
    Frame4.configure(relief='groove')
    Frame4.configure(borderwidth="2")
    Frame4.configure(relief="groove")
    Frame4.configure(background="#d8cbcb")

    loginicon_label = Label(Frame4,image = logo)
    loginicon_label.place(relx=0.324, rely=0.124)
    loginicon_label.configure(background="#d8cbcb")
    loginicon_label.configure(disabledforeground="#a3a3a3")
    loginicon_label.configure(foreground="#000000")

    lbluser = Label(Frame4, text="Username", image=user_logo, compound=LEFT,font=("times new roman", 20, "bold"), bg="#0da2d8")
    lbluser.place(relx=0.18, rely=0.474)

    txtuser = Entry(Frame4, bd=5, textvariable=username, relief=GROOVE, font=("", 15))
    txtuser.place(relx=0.468, rely=0.474,height=40, relwidth=0.404)

    lblpass = Label(Frame4, text="Password", image=pass_logo, compound=LEFT,font=("times new roman", 20, "bold"), bg="#0da2d8")
    lblpass.place(relx=0.18, rely=0.598)

    txtpass = Entry(Frame4, bd=5, relief=GROOVE, textvariable=password, font=("", 15),show="*")
    txtpass.place(relx=0.468, rely=0.598,height=40, relwidth=0.404)

    btn_login = Button(Frame4)
    btn_login.place(relx=0.396, rely=0.763, height=44, width=147)
    btn_login.configure(activebackground="#ececec")
    btn_login.configure(activeforeground="#000000")
    btn_login.configure(background="#ffffff")
    btn_login.configure(disabledforeground="#a3a3a3")
    btn_login.configure(foreground="#000000")
    btn_login.configure(highlightbackground="#0da2d8")
    btn_login.configure(highlightcolor="black")
    btn_login.configure(pady="0")
    btn_login.configure(text='''Login''',command = login_now)

    lbllogin = Label(Frame4)
    lbllogin.place(relx=0.288, rely=0.021, height=41, width=244)
    lbllogin.configure(background="#d8cbcb")
    lbllogin.configure(disabledforeground="#a3a3a3")
    lbllogin.configure(font=font11)
    lbllogin.configure(foreground="#000000")
    lbllogin.configure(text='''Login Here''')

    btnforgot = Button(Frame4)
    btnforgot.place(relx=0.568, rely=0.701, height=24, width=107)
    btnforgot.configure(activebackground="#ececec")
    btnforgot.configure(activeforeground="#000000")
    btnforgot.configure(background="#d8cbcb")
    btnforgot.configure(borderwidth="0")
    btnforgot.configure(disabledforeground="#a3a3a3")
    btnforgot.configure(foreground="#0d4dff")
    btnforgot.configure(highlightbackground="#0da2d8")
    btnforgot.configure(highlightcolor="black")
    btnforgot.configure(pady="0")
    btnforgot.configure(text='''Forgot Password''',command = forgotpass)

    lblforgot = Label(Frame4)
    lblforgot.place(relx=0.279, rely=0.701)
    lblforgot.configure(background="#d8cbcb")
    lblforgot.configure(disabledforeground="#a3a3a3")
    lblforgot.configure(foreground="#000000")
    lblforgot.configure(text='''Having problem logging in?''')

    lblcont = Label(Frame2)
    lblcont.place(relx=0.274, rely=0.237, height=31, width=154)
    lblcont.configure(background="#d8cbcb")
    lblcont.configure(disabledforeground="#a3a3a3")
    lblcont.configure(foreground="#000000")
    lblcont.configure(text='''Continue with''')

    lblor2 = Label(Frame2)
    lblor2.place(relx=0.411, rely=0.412, height=31, width=44)
    lblor2.configure(background="#d8cbcb")
    lblor2.configure(disabledforeground="#a3a3a3")
    lblor2.configure(foreground="#000000")
    lblor2.configure(text='''OR''')

    '''title = Label(root, text="Login Page", font=("times new roman", 40, "bold"), bg="yellow", fg="red", bd=10,relief=GROOVE)
    title.place(x=0, y=0, relwidth=1)

    l1 = Label(root,image = logo).grid()
    l2 = Label(root, image=user_logo).grid()
    l3 = Label(root, image=pass_logo).grid()'''
    root1.mainloop()

loginpage(None)
