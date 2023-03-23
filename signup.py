from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector
import os
class signupClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x690+0+0")
        self.root.title("Equipment Leasing System | Developed By Priya Anoop")
        self.root.config(bg="white")
        self.root.focus_force()
        self.phone_image = ImageTk.PhotoImage(file="images/phone.png")
        self.lbl_phone_image = Label(self.root, image=self.phone_image, bd=0).place(x=600, y=10)
        # All variables

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()

        self.im1 = ImageTk.PhotoImage(file="images/im1.png")
        self.im2 = ImageTk.PhotoImage(file="images/im2.png")
        self.im3 = ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_change_image = Label(self.root, bg="white")
        self.lbl_change_image.place(x=767, y=118, width=240, height=428)

        self.animate()



        # title
        title = Label(self.root, text="Sign Up Page", font=("times new roman", 15), bg="#0f4d7d", fg="white").pack(side=TOP,fill=X)

        # content
        # row1
        lbl_empid = Label(self.root, text="Emp ID", font=("times new roman", 15), bg="white").place(x=50, y=40)
        lbl_gender = Label(self.root, text="Gender", font=("times new roman", 15), bg="white").place(x=50, y=80)
        lbl_contact = Label(self.root, text="Contact", font=("times new roman", 15), bg="white").place(x=50, y=120)

        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=("times new roman", 15), bg="lightgreen").place(
            x=150, y=40, width=300)

        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female", "Other"),
                                  state='readonly', justify=CENTER, font=("times new roman", 15))
        cmb_gender.place(x=150, y=80, width=300)
        cmb_gender.current(0)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("times new roman", 15),
                            bg="lightgreen").place(x=150, y=120, width=300)
        #4 - 5 - 6
        lbl_name = Label(self.root, text="Name", font=("times new roman", 15), bg="white").place(x=50, y=160)
        lbl_dob = Label(self.root, text="D.O.B", font=("times new roman", 15), bg="white").place(x=50, y=200)
        lbl_doj = Label(self.root, text="D.O.J", font=("times new roman", 15), bg="white").place(x=50, y=240)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("times new roman", 15), bg="lightgreen").place(
            x=150, y=160, width=300)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("times new roman", 15), bg="lightgreen").place(
            x=150, y=200, width=300)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("times new roman", 15), bg="lightgreen").place(
            x=150, y=240, width=300)

        #7-8-9
        lbl_email = Label(self.root, text="Email", font=("times new roman", 15), bg="white").place(x=50, y=280)
        lbl_pass = Label(self.root, text="Password", font=("times new roman", 15), bg="white").place(x=50, y=320)
        lbl_utype = Label(self.root, text="User Type", font=("times new roman", 15), bg="white").place(x=50, y=360)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("times new roman", 15), bg="lightgreen").place(
            x=150, y=280, width=300)
        txt_pass = Entry(self.root, textvariable=self.var_pass, font=("times new roman", 15), bg="lightgreen").place(
            x=150, y=320, width=300)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Select", "Lessor", "Lessee"),
                                 state='readonly', justify=CENTER, font=("times new roman", 15))
        cmb_utype.place(x=150, y=360, width=300)
        cmb_utype.current(0)
        #10 - 11
        lbl_address = Label(self.root, text="Address", font=("times new roman", 15), bg="white").place(x=50, y=400)
        self.txt_address = Text(self.root, font=("times new roman", 15), bg="lightgreen")
        self.txt_address.place(x=150, y=400, width=300, height=60)

        #Buttons
        btn_sign_up = Button(self.root, text="Sign Up", command=self.add, font=("goudy old style", 15), bg="#2196f3",
                         fg="white", cursor="hand2").place(x=50, y=470, width=110, height=28)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#a334ac",
                           fg="white", cursor="hand2").place(x=180, y=470, width=110, height=28)
        btn_login = Button(self.root, text="Go Back To Log In", command=self.login, font=("goudy old style", 15), bg="#2196f3",
                             fg="white", cursor="hand2").place(x=300, y=470, height=28)


    def add(self):
        con = mysql.connector.connect(host='localhost', user='root', password='', db='ims')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=%s", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Employee ID already assigned, try different", parent=self.root)
                else:
                    cur.execute(
                        "Insert into pending (eid,employee_name,email,gender,contact,dob,doj,pass,utype,address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_emp_id.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0', END),
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Waiting for approval", parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Select")
        self.txt_address.delete('1.0', END)

    def animate(self):
        self.im = self.im1
        self.im1 = self.im2
        self.im2 = self.im3
        self.im3 = self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000, self.animate)

    def login(self):
        self.root.destroy()
        os.system("python login.py")


if __name__ == "__main__":
    root = Tk()
    obj = signupClass(root)
    root.mainloop()