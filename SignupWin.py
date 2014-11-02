from tkinter import *
import re
import mysql.connector
from mysql.connector import errorcode

class signup():


    def __init__(self):
        self.root = Toplevel()
        self.root.title("Регистрация")
        self.root.grid(400, 300, 200, 220)
        but0 = Button(self.root, text="Ok", width=13, height=1)
        lab0 = Label(self.root, text="login", font="Arial 14")
        lab1 = Label(self.root, text="password", font="Arial 14")
        lab2 = Label(self.root)
        lab3 = Label(self.root, text="confirm password", font="Arial 14")
        self.ent0 = Entry(self.root, width=20, bd=1)
        self.ent1 = Entry(self.root, width=20, bd=1)
        self.ent2 = Entry(self.root, width=20, bd=1)
        lab0.pack()
        self.ent0.pack()
        lab1.pack()
        self.ent1.pack()
        lab3.pack()
        self.ent2.pack()
        lab2.pack()
        but0.pack()
        but0.bind("<Button-1>", self.ok_but)
        self.root.mainloop()


    def ok_but(self, event):
        self.login = self.ent0.get()
        self.password = self.ent1.get()
        self.passc = self.ent2.get()
        regexp = re.compile(r"([a-zA-Z0-9][\w\._\-]{4,63}@[a-z]{2,8}\.(com|net|org))")
        login = regexp.search(self.login)
        if login == None:
            print("Вы ввели не валидный e-mail. Система прекращает работу.")
            raise SystemExit(1)
        else:
            login = login.group()

        if not (any(letter.isdigit() for letter in self.password) and any(letter.islower() for letter in self.password) \
                and any(letter.isupper() for letter in self.password)):
            print("Ваш пароль не соответствует условиям. Система прекращает работу.")
            raise SystemExit(1)

        if self.password!=self.passc:
            print("Ваши пароли не совпадают. Система прекращает работу.")
            raise SystemExit(1)

        try:
            con = mysql.connector.connect(user='root', password='root', host='127.0.0.1')
            cursor = con.cursor()
            cursor.execute("USE admin_b")
            cursor.execute("INSERT INTO users (name, password,role) values(%s,%s, 2)",(login, self.password))
            con.commit()
            print("Вы успешно зарегистрировались. Ваш логин: {}, ваш пароль: {}".format(login, self.password))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            else:
                print(err)
        else:
              cursor.close()
              con.close()
              self.root.destroy()





