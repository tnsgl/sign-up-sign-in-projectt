import json
import tkinter
islogin=False
login_user=""
def jread():
    try:
        with open("info.json") as f:
            users=json.load(f)
    except:
        print("this file is damaged!!trying to make a new one")
        users={"admin":"123456789"}
        jwrite(users)
    return users
def jwrite(users):
    with open("info.json","w") as f:
        json.dump(users,f)
def login():
    global islogin,login_user
    if(islogin==True):
        lbl.configure(text="you are already logged in!!",fg="red")
        return
    user=txt_user.get()
    passw=txt_passw.get()
    users=jread()
    if((user in users)and(users[user]==passw)):
        lbl.configure(text="welcome:)",fg="green")
        islogin=True
        login_user=user
        lst=[]
        lst.append(user)
        with open("log.json","w") as f:
            json.dump(lst,f)
        return lst
    
    else:
        lbl.configure(text="wrong username or password",fg="red")

def submit():
    user=txt_user.get()
    passw=txt_passw.get()
    if(len(passw)<8):
        lbl.configure(text="passw length not enough!!!",fg="red")
        return
    users=jread()
    if(user in users):
        lbl.configure(text="username already exist!!!",fg="red")
        return
    users={"admin":"123456789"}
    users[user]=passw
    jwrite(users)
    lbl.configure(text="you have submitted!!!",fg="green")
    islogin=True
    login_user=user
def logout():
    global islogin,login_user
    islogin=False
    login_user=""
    lbl.configure(text="you are now logged out!!!",fg="blue")

def delete():
    global islogin,login_user
    if(islogin==False):
        lbl.configure(text="please login first",fg="red")
        return
    if(login_user=="admin"):
        lbl.configure(text="admin account is not removable",fg="red")
        return
    users=jread()
    win1=tkinter.Tk()
    win1.title("delete account")
    win1.geometry("200x200")
    win1.configure(bg="blue")
    lbl11=tkinter.Label(win1,text="are you sure?")
    lbl11.pack()
    lbl11.place(x=60,y=30)

    def yes():
        global login_user,islogin
        users.pop(login_user)
        jwrite(users)
        islogin=False
        login_user=""
        lbl.configure(text="your account has been deleted",fg="blue")
        win1.destroy()
        return
    def no():
        lbl.configure(text="cancelled by user",fg="blue")
        win1.destroy()
        return
    
    btn_yes=tkinter.Button(win1,text="yes",fg="green",command=yes).place(x=60,y=110)
    btn_no=tkinter.Button(win1,text="no",fg="red",command=no).place(x=120,y=110)
def userslist():
    global login_user
    if(login_user!="admin"):
        lbl.configure(text="only admin can access this information!",fg="red")
        return
    with open("log.json") as f:
        logins=json.load(f)
    for user in logins:
        lstbx.insert("end",user)
    lbl.configure(text="here is the list of users logged in")

########making window
win=tkinter.Tk()
win.title("win_account")
win.geometry("345x500")
win.configure(bg="spring green")
########making label
lbl=tkinter.Label(win,text="Hello:)",fg="magenta",font="roman")
lbl.pack()
lbl.place(x=100,y=20)

lbl1=tkinter.Label(win,text="username")
lbl1.pack()
lbl1.place(x=40,y=60)

lbl2=tkinter.Label(win,text="password")
lbl2.pack()
lbl2.place(x=40,y=100)

lstbx=tkinter.Listbox(win)
lstbx.pack()
lstbx.place(x=100,y=200)
########making entry
txt_user=tkinter.Entry(win,width=25)
txt_user.place(x=100,y=60)
txt_passw=tkinter.Entry(win,width=25)
txt_passw.place(x=100,y=100)

########making button
btn_login=tkinter.Button(win,text="log in",command=login).place(x=40,y=130)
btn_submit=tkinter.Button(win,text="submit",command=submit).place(x=100,y=130)
btn_logout=tkinter.Button(win,text="log out",command=logout).place(x=160,y=130)
btn_delete=tkinter.Button(win,text="delete account",command=delete).place(x=220,y=130)
btn_userslist=tkinter.Button(win,text="users list",command=userslist).place(x=135,y=170)






win.mainloop()
