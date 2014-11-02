from tkinter import *
import SignupWin
import mysql.connector
from mysql.connector import errorcode
import string
import random
import smtplib
 
class logwin():
 
    def send_mail(self, login_u, password_u):
        fromaddr = 'smtp.python.bh@gmail.com'
        toaddrs = login_u
        msg ="\r\n".join(["From: smtp.python.bh@gmail.com",
                          "To: {}",
                          "Subject: test subject",
                          "",
                          "Ваш логин: {}",
                          "Ваш пароль: {}".format(login_u, login_u, password_u)])
        username = 'smtp.python.bh@gmail.com'
        password = 'smtp.python.bh2014'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
 
    def signupb(self, event):
        SignupWin.signup()
 
    def signin(self,event):
        login = self.ent0.get()
        password = self.ent1.get()
        try:
            con = mysql.connector.connect(user='root', password='root', host='127.0.0.1')
            cursor = con.cursor()
            cursor.execute("USE admin_b")
            try:
                cursor.execute("SELECT name, password, id FROM users WHERE name = '{}'".format(login))
                result = cursor.fetchall()
                id = result[0][2]
                print ("id = " + str(id))
                con.commit()
                if password != result[0][1]:
                    print("Вы ввели неверный пароль. Система прекращает работу.")
                    raise SystemExit(1)
            except mysql.connector.Error as err:
                print(err)
 
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            else:
                print(err)
        else:
              cursor.close()
              con.close()
 
    def remind_password(self, event):
        pas = False
        while pas!=True:
            new_passowrd ="".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                                  for x in range(random.randint(8,16)))
            if (any(letter.isdigit() for letter in new_passowrd) and any(letter.islower() for letter in new_passowrd) \
                and any(letter.isupper() for letter in new_passowrd)):
                pas = True
        login = self.ent0.get()
        try:
            con = mysql.connector.connect(user='root', password='root', host='127.0.0.1')
            cursor = con.cursor()
            cursor.execute("USE admin_b")
            try:
                cursor.execute("UPDATE users SET password = '{}' WHERE name = '{}'".format(new_passowrd,login))
                con.commit()
                print("На ваш email отправлено письмо с новым паролем")
 
            except mysql.connector.Error as err:
                print(err)
 
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            else:
                print(err)
        else:
              cursor.close()
              con.close()
 
 
 
 
    def __init__(self):
        root = Tk()
        root.title("Авторизация")
        root.grid(400, 300, 200, 170)
        but0 = Button(root, text="sign in", width=13, height=1)
        but1 = Button(root, text="sign up", width=13, height=1)
        but2 = Button(root, text="remind password", width=13, height=1)
        lab0 = Label(root,text="login", font="Arial 14")
        lab1 = Label(root,text="password", font="Arial 14")
        lab2=Label(root)
        self.ent0 = Entry(root,width=20, bd=1)
        self.ent1 = Entry(root,width=20, bd=1)
        lab0.grid(row=1,column=2)
        self.ent0.grid(row=2,column=2)
        lab1.grid(row=3,column=2)
        self.ent1.grid(row=4,column=2)
        lab2.grid(row=5,column=3)
        but0.grid(row=6,column=3)
        but1.grid(row=6,column=1)
        but2.grid(row=6,column=2)
        but1.bind("<Button-1>", self.signupb)
        but0.bind("<Button-1>", self.signin)
        but2.bind("<Button-1>",self.remind_password)
        root.mainloop()
