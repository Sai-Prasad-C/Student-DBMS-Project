import tkinter as tk
from tkinter import *
from tkinter import messagebox

def dashboard(self):

    _bgcolor = '#0da2d8'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9'
    _ana2color = '#ececec'
    font11 = "-family Arial -size 18 -weight bold -slant roman " \
             "-underline 0 -overstrike 0"
    font12 = "-family {Segoe UI} -size 15 -weight bold -slant " \
             "roman -underline 0 -overstrike 0"
    font13 = "-family {Segoe UI} -size 12 -weight bold -slant " \
             "roman -underline 0 -overstrike 0"

    root5 = Tk()
    root5.geometry("1353x691+-3+2")
    root5.title("Dashboard")
    root5.configure(background="#0a0093")
    root5.configure(highlightbackground="#d9d9d9")
    root5.configure(highlightcolor="black")

    personal = PhotoImage(file="Images\personal.png")
    details = PhotoImage(file="Images\details.png")
    analysis = PhotoImage(file="Images\Analysis.png")

    welcomeframe = tk.Frame(root5)
    welcomeframe.place(relx=0.007, rely=0.043, relheight=0.08
                       , relwidth=0.987)
    welcomeframe.configure(relief='groove')
    welcomeframe.configure(borderwidth="2")
    welcomeframe.configure(relief="groove")
    welcomeframe.configure(background="white")
    welcomeframe.configure(highlightbackground="#d9d9d9")
    welcomeframe.configure(highlightcolor="black")

    welcomelbl = tk.Label(welcomeframe)
    welcomelbl.place(relx=0.315, rely=0.182, height=41, width=404)
    welcomelbl.configure(activebackground="#f9f9f9")
    welcomelbl.configure(activeforeground="black")
    welcomelbl.configure(background="white")
    welcomelbl.configure(disabledforeground="#a3a3a3")
    welcomelbl.configure(font="-family {Arial Nova Cond} -size 16 -weight bold")
    welcomelbl.configure(foreground="#000000")
    welcomelbl.configure(highlightbackground="#d9d9d9")
    welcomelbl.configure(highlightcolor="black")
    welcomelbl.configure(text='''Welcome To Our Software''')

    btnlogout = tk.Button(welcomeframe)
    btnlogout.place(relx=0.831, rely=0.182, height=34, width=177)
    btnlogout.configure(activebackground="#ececec")
    btnlogout.configure(activeforeground="#000000")
    btnlogout.configure(background="white")
    btnlogout.configure(borderwidth="1")
    btnlogout.configure(disabledforeground="#a3a3a3")
    btnlogout.configure(foreground="#000000")
    btnlogout.configure(highlightbackground="#0da2d8")
    btnlogout.configure(highlightcolor="black")
    btnlogout.configure(pady="0")
    btnlogout.configure(relief="groove")
    btnlogout.configure(text='''Logout''')

    dash_frame1 = tk.Frame(root5)
    dash_frame1.place(relx=0.007, rely=0.232, relheight=0.745
                      , relwidth=0.403)
    dash_frame1.configure(relief='groove')
    dash_frame1.configure(borderwidth="2")
    dash_frame1.configure(relief="groove")
    dash_frame1.configure(background="#0eafea")
    dash_frame1.configure(highlightbackground="#d9d9d9")
    dash_frame1.configure(highlightcolor="black")

    lblpersonaldetails = tk.Label(dash_frame1)
    lblpersonaldetails.place(relx=0.22, rely=0.039, height=61
                             , width=264)
    lblpersonaldetails.configure(background="#0eafea")
    lblpersonaldetails.configure(disabledforeground="#a3a3a3")
    lblpersonaldetails.configure(font=font12)
    lblpersonaldetails.configure(foreground="#000000")
    lblpersonaldetails.configure(text='''Personal Details''')

    txtpersonal = tk.Label(dash_frame1,image = personal)
    txtpersonal.place(relx=0.257, rely=0.311, relheight=0.416
                      , relwidth=0.466)
    txtpersonal.configure(background="white")
    txtpersonal.configure(font=font11)
    txtpersonal.configure(foreground="black")

    btndetailpanel = tk.Button(dash_frame1)
    btndetailpanel.place(relx=0.257, rely=0.757, height=64, width=257)
    btndetailpanel.configure(activebackground="#ececec")
    btndetailpanel.configure(activeforeground="#000000")
    btndetailpanel.configure(background="#000000")
    btndetailpanel.configure(disabledforeground="#a3a3a3")
    btndetailpanel.configure(font=font13)
    btndetailpanel.configure(foreground="#ffffff")
    btndetailpanel.configure(highlightbackground="#0da2d8")
    btndetailpanel.configure(highlightcolor="black")
    btndetailpanel.configure(pady="0")
    btndetailpanel.configure(text='''Click to Proceed''')

    dash_frame = tk.Frame(root5)
    dash_frame.place(relx=0.007, rely=0.13, relheight=0.094
                     , relwidth=0.987)
    dash_frame.configure(relief='groove')
    dash_frame.configure(borderwidth="2")
    dash_frame.configure(relief="groove")
    dash_frame.configure(background="#0668d8")
    dash_frame.configure(highlightbackground="#d9d9d9")
    dash_frame.configure(highlightcolor="black")

    dashboardlbl = tk.Label(dash_frame)
    dashboardlbl.place(relx=0.33, rely=0.154, height=51, width=204)
    dashboardlbl.configure(background="#0668d8")
    dashboardlbl.configure(disabledforeground="#a3a3a3")
    dashboardlbl.configure(font=font11)
    dashboardlbl.configure(foreground="#000000")
    dashboardlbl.configure(text='''DASHBOARD''')

    developerslbl = tk.Label(dash_frame)
    developerslbl.place(relx=0.637, rely=0.154, height=41, width=414)
    developerslbl.configure(background="#0668d8")
    developerslbl.configure(disabledforeground="#a3a3a3")
    developerslbl.configure(font="-family {Arial Nova Cond} -size 14")
    developerslbl.configure(foreground="#000000")
    developerslbl.configure(text='''Developers ~ Sai Prasad & Aditya Mishra & Hritik Sharma''')

    dash_frame2 = tk.Frame(root5)
    dash_frame2.place(relx=0.414, rely=0.232, relheight=0.745
                      , relwidth=0.58)
    dash_frame2.configure(relief='groove')
    dash_frame2.configure(borderwidth="2")
    dash_frame2.configure(relief="groove")
    dash_frame2.configure(background="white")
    dash_frame2.configure(highlightbackground="#d9d9d9")
    dash_frame2.configure(highlightcolor="black")

    lblperformancerec = tk.Label(dash_frame2)
    lblperformancerec.place(relx=0.268, rely=0.058, height=51
                            , width=404)
    lblperformancerec.configure(background="white")
    lblperformancerec.configure(disabledforeground="#a3a3a3")
    lblperformancerec.configure(font=font12)
    lblperformancerec.configure(foreground="#000000")
    lblperformancerec.configure(text='''Performance Records''')

    txtperformancerec = tk.Label(dash_frame2,image = details)
    txtperformancerec.place(relx=0.115, rely=0.33, relheight=0.377
                            , relwidth=0.336)
    txtperformancerec.configure(background="#0eafea")
    txtperformancerec.configure(font=font11)
    txtperformancerec.configure(foreground="black")


    txtviewrec = tk.Label(dash_frame2,image = analysis)
    txtviewrec.place(relx=0.586, rely=0.33, relheight=0.377
                     , relwidth=0.324)
    txtviewrec.configure(background="#0eafea")
    txtviewrec.configure(font=font11)
    txtviewrec.configure(foreground="black")

    btnrecpanel = tk.Button(dash_frame2)
    btnrecpanel.place(relx=0.115, rely=0.738, height=64, width=267)
    btnrecpanel.configure(activebackground="#ececec")
    btnrecpanel.configure(activeforeground="#000000")
    btnrecpanel.configure(background="#000000")
    btnrecpanel.configure(disabledforeground="#a3a3a3")
    btnrecpanel.configure(font=font13)
    btnrecpanel.configure(foreground="#0da2d8")
    btnrecpanel.configure(highlightbackground="#0da2d8")
    btnrecpanel.configure(highlightcolor="black")
    btnrecpanel.configure(pady="0")
    btnrecpanel.configure(text='''Click to Proceed''')

    btnrecview = tk.Button(dash_frame2)
    btnrecview.place(relx=0.586, rely=0.738, height=64, width=257)
    btnrecview.configure(activebackground="#ececec")
    btnrecview.configure(activeforeground="#000000")
    btnrecview.configure(background="#000000")
    btnrecview.configure(disabledforeground="#a3a3a3")
    btnrecview.configure(font=font13)
    btnrecview.configure(foreground="#0da2d8")
    btnrecview.configure(highlightbackground="#0da2d8")
    btnrecview.configure(highlightcolor="black")
    btnrecview.configure(pady="0")
    btnrecview.configure(text='''Click to Proceed''')

    root5.mainloop()

dashboard(NONE)