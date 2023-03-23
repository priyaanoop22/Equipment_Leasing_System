from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import mysql.connector
import os


class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x768+0+0")
        self.root.title("Equipment Leasing System | Developed By Priya Anoop")
        self.root.config(bg="white")
        # ---------------
        self.phone_image = ImageTk.PhotoImage(file="images/phone.png")
        self.lbl_phone_image = Label(self.root, image=self.phone_image, bd=0).place(x=200, y=50)

        # -------------------LOGIN FRAME------------------------------
        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        login_frame.place(x=650, y=90, width=350, height=460)

        title = Label(login_frame, text="Login System", font=("Elephant", 30, "bold"), bg='white').place(x=0, y=30,
                                                                                                         relwidth=1)

        lbl_user = Label(login_frame, text="Employee ID", font=("Andalus", 15), bg="white", fg="#767171").place(x=50,
                                                                                                                y=100)
        self.employee_id = StringVar()
        txt_employee_id = Entry(login_frame, textvariable=self.employee_id, font=("times new roman", 15),
                                bg="lightgreen").place(x=50, y=140, width=250)

        lbl_pass = Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg="#767171").place(x=50,
                                                                                                             y=200)
        self.password = StringVar()
        txt_pass = Entry(login_frame, textvariable=self.password, show="*", font=("times new roman", 15),
                         bg="lightgreen").place(x=50, y=240, width=250)

        btn_login = Button(login_frame, text="Log In", command=self.login, font=("Arial Rounded MT Bold", 15),
                           bg="#00B0F0", activebackground="#00B0F0", fg="white", activeforeground="white",
                           cursor="hand2").place(x=50, y=300, width=250, height=35)

        hr = Label(login_frame, bg="lightgray").place(x=50, y=370, width=250, height=2)
        or_ = Label(login_frame, text="OR", bg="white", fg="lightgray", font=("times new roman", 15)).place(x=150,
                                                                                                            y=357)

        btn_forget = Button(login_frame, text="Admin? Go to Admin sign in", command=self.adminlogin,
                            font=("times new roman", 13), bg="white", fg="blue", bd=0, activebackground="white",
                            activeforeground="blue", cursor="hand2").place(x=60, y=390)

        register_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        register_frame.place(x=650, y=570, width=350, height=60)

        lbl_reg = Label(register_frame, text="Don't have an account?", font=("times new roman", 13), bg="white").place(
            x=40, y=15)
        btn_signup = Button(register_frame, text="Sign Up",command=self.signup, font=("times new roman", 13, "bold"), bg="white", fg="blue",
                            bd=0, activebackground="white", activeforeground="blue", cursor="hand2").place(x=200, y=12)


        # Animation Images
        self.im1 = ImageTk.PhotoImage(file="images/im1.png")
        self.im2 = ImageTk.PhotoImage(file="images/im2.png")
        self.im3 = ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_change_image = Label(self.root, bg="white")
        self.lbl_change_image.place(x=367, y=153, width=240, height=428)

        self.animate()

    # ----------------All Functions--------------------

    def animate(self):
        self.im = self.im1
        self.im1 = self.im2
        self.im2 = self.im3
        self.im3 = self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000, self.animate)

    def login(self):
        con = mysql.connector.connect(host='localhost', user='root', password='', db='ims')
        cur = con.cursor()
        try:
            if self.employee_id.get() == "" or self.password.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("select utype from employee where eid=%s AND pass=%s",
                            (self.employee_id.get(), self.password.get(),))
                user = cur.fetchone()
                if user == None:
                    messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
                else:
                    if user[0] == "Lessor":
                        self.root.destroy()
                        os.system("python lessordash.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def adminlogin(self):
        self.root.destroy()
        os.system("python adminlogin.py")

    def signup(self):
        self.root.destroy()
        os.system("python signup.py")



root = Tk()
obj = Login_System(root)
root.mainloop()