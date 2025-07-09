from tkinter import *
from PIL import Image, ImageTk
from customtkinter import CTkEntry, CTkButton, CTkImage
from tkinter import messagebox
from tkcalendar import Calendar
import etmin
import dashboard
import psycopg2

db_config = {
    'host': 'localhost',
    'port': 5432,
    'database': 'berthdb1',
    'user': 'admin',
    'password': 'admin'
}



def connect_db():
    conn = psycopg2.connect(**db_config)
    return conn
class LoginPage:
    def __init__(self,loginpage):
        self.loginpage = loginpage
        self.admin_menu = None
        self.sign_up_menu = None
        self.loginpage.title("berth")
        self.loginpage.rowconfigure(0, weight=1)
        self.loginpage.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (loginpage.winfo_screenwidth() // 2) - (width // 2)
        y = (loginpage.winfo_screenheight() // 4) - (height // 4)
        loginpage.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        loginpage.resizable(0, 0)
        # self.loginpage.iconbitmap("icon.ico")
        self.loginpage.config(bg="#B28C6E")
        def exitt2():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=self.loginpage)
            if sure == True:
                self.loginpage.destroy()
        self.loginpage.protocol("WM_DELETE_WINDOW", exitt2)

        self.image1 = Image.open("images\\Silaju.png")
        self.image1 = self.image1.resize((1280, 720))
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.canvas = Canvas(self.loginpage, width=1366, height=768, bg="#C70039")
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor='nw', image=self.photo1)

        self.username_loginpage = CTkEntry(self.loginpage, width=450,
                                           corner_radius=30,
                                           height=50,
                                           placeholder_text='masukkan username anda',
                                           font=("Helvetica", 17, "italic"),
                                           placeholder_text_color='#545454',
                                           bg_color="white",
                                           fg_color="white",
                                           text_color="black",
                                           border_color="#545454",
                                           border_width= 1,
                                           )
        self.username_loginpage.place(x=95, y=340)


        self.password_loginpage = CTkEntry(self.loginpage, width=450,
                                           height=50,
                                           corner_radius=50,
                                           placeholder_text = 'Password',
                                           font=("Helvetica", 17, "italic"),
                                           placeholder_text_color='#545454',
                                           bg_color="white",
                                           fg_color="white",
                                           text_color="black",
                                           border_color= "#545454",
                                           border_width=1
                                           )
        self.password_loginpage.place(x=95, y=460)

        # def show():
        #     try:
        #         self.show_password_button.configure(image=self.show_image, command=hide)
        #         self.password_loginpage.configure(show='')
        #         self.field_password.configure(show='')
        #         self.field_cpassword.configure(show='')
        #     except AttributeError as e:
        #         pass
        #
        # def hide():
        #     try:
        #         self.show_password_button.configure(image=self.hide_image, command=show)
        #         self.password_loginpage.configure(show='*')
        #         self.field_password.configure(show='*')
        #         self.field_cpassword.configure(show='*')
        #     except AttributeError as e:
        #         pass
        # self.hide_image = CTkImage(Image.open("hide.png"),
        #                            size=(20, 20))
        # self.show_image = CTkImage(Image.open("show.png"),
        #                            size=(20, 20))
        # self.show_password_button = CTkButton(self.loginpage, command=hide, text=""
        #                                       , bg_color="white",fg_color="white",width=20,
        #                                       image=self.hide_image,hover_color= 'white')
        # self.show_password_button.place(x= 321, y=350)

        sign_up_label = Label(self.loginpage,text='dont have an account ?', font=("Microsoft YaHei UI Light",10,'bold'),bg="white",fg="black")
        sign_up_label.place(x=284, y=520)
        sign_up_button = Button(self.loginpage, text='sign up',cursor="hand2", font=("Microsoft YaHei UI Light",10,'bold'),bg="white",fg="blue",border=0,activebackground='white',command=self.signup)
        sign_up_button.place(x=464, y=519)



        button_login = CTkButton(self.loginpage,
                                 text="Sign In ",
                                 font=("Nunito", 25, 'bold'),
                                 width=200,
                                 height=55,
                                 corner_radius=10,
                                 bg_color="white",
                                 fg_color="black",
                                 hover_color="#302E2B",
                                 command=self.login)
        button_login.place(x=340, y=550)

    def login(self):
        username = self.username_loginpage.get()
        password = self.password_loginpage.get()

        user_type, username = login(username, password)

        if user_type == "customer":
            messagebox.showinfo("Success", f'Welcome {username}')
            self.loginpage.withdraw()
            self.mainmenu()
        elif user_type == "admin":
            messagebox.showinfo("Success", f"Welcome Admin")
            self.adminmenu()
            self.loginpage.withdraw()

        else:
            messagebox.showerror("Error", "Invalid username or password")

    def signup(self):
        self.loginpage.withdraw()
        self.sign_up_menu = Toplevel(self.loginpage)
        self.sign_up_menu.title("Sign Up")
        self.sign_up_menu.resizable(False,False)
        self.sign_up_menu.rowconfigure(0, weight=1)
        self.sign_up_menu.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (self.sign_up_menu.winfo_screenwidth() // 2) - (width // 2)
        y = (self.sign_up_menu.winfo_screenheight() // 4) - (height // 4)
        self.sign_up_menu.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        def submit():
            check_counter = 0
            warn = ""
            if self.field_name_signup.get() == "":
                warn = "Please enter your full name"
            else:
                check_counter += 1

            if self.field_email_signup.get() == "":
                warn = "Please make sure your email field are not empty"
            else:
                check_counter += 1

            if self.nik_signup.get() == "":
                warn = 'please fill the NIK field'

            else:
                check_counter += 1

            if self.entry_date.get() == "":
                warn = 'Please fill your birthdate'
            else :
                check_counter += 1

            if self.phone.get() == "":
                warn = "Please enter yout phone number"
            else :
                check_counter += 1

            if check_counter == 0 :
                warn = 'fill all the field before'

            if check_counter == 5:
                try:
                    self.show_register2()
                except Exception as e:
                    messagebox.showerror('', e)
            else:
                messagebox.showerror('Error', warn)

        self.register1 = Frame(self.sign_up_menu)
        self.register2 = Frame(self.sign_up_menu)

        for frame in(self.register1, self.register2):
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_register1()
        self.image2 = Image.open("images\\signup.png")
        self.image2 = self.image2.resize((1280, 720))
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.canvas1 = Canvas(self.register1, width=1366, height=768, bg="#C70039")
        self.canvas1.pack()
        self.canvas1.create_image(0, 0, anchor='nw', image=self.photo2)
        label_signup_page = Label(self.register1,
                                  text="Nama Lengkap",
                                  font=("Helvetica", 15),
                                  bg="white",
                                  fg="#545454", )
        # label_signup_page.place(x=160, y=160)
        self.field_name_signup = CTkEntry(self.register1, width=350,
                                          height=40,
                                          corner_radius=30,
                                          font=("Arial", 17, "italic"),
                                          placeholder_text='nama',
                                          placeholder_text_color='#545454',
                                          bg_color="white",
                                          fg_color="white",
                                          border_color="#545454",
                                          text_color="black",
                                          border_width=1
                                          )
        self.field_name_signup.place(x=50, y=240)
        label_phonenumber_page = Label(self.register1,
                                  text="Nomor Telepon",
                                  font=("Helvetica", 15),
                                  bg="white",
                                  fg="#545454", )
        # label_phonenumber_page.place(x=500, y=160)
        self.nik_signup = CTkEntry(self.register1, width=350,
                                          height=40,
                                          corner_radius=30,
                                   placeholder_text='nik',
                                          font=("Arial", 17, "italic"),
                                          placeholder_text_color='#545454',
                                          bg_color="white",
                                          fg_color="white",
                                          border_color="#545454",
                                          text_color="black",
                                          border_width=1
                                          )
        self.nik_signup.place(x=50, y=395)
        label_email_page = Label(self.register1,
                                          text="Email",
                                          font=("Helvetica", 15),
                                          bg="white",
                                          fg="#545454", )
        # label_email_page.place(x=160, y=250)

        self.field_email_signup = CTkEntry(self.register1, width=350,
                                              height=40,
                                              corner_radius=30,
                                           placeholder_text='email',
                                              placeholder_text_color='#545454',
                                              font=("Arial", 17, "italic"),
                                              bg_color="white",
                                              fg_color="white",
                                              text_color="black",
                                              border_color="#545454",
                                              border_width=1,
                                              )

        self.field_email_signup.place(x=50, y=315)

        def open_date_picker():
            def select_date():
                selected_date = calendar.get_date()
                self.entry_date.delete(0, END)
                self.entry_date.insert(0, selected_date)
                date_picker_window.destroy()

            date_picker_window = Toplevel(self.register1)
            date_picker_window.title("Pilih Tanggal")
            calendar = Calendar(date_picker_window, date_pattern="yyyy-mm-dd")
            calendar.pack(pady=10)

            select_button = CTkButton(date_picker_window, text="Pilih", command=select_date)
            select_button.pack(pady=5)

        self.entry_date = CTkEntry(self.register1, width=350,
                                   placeholder_text='tgl lahir',
                                   placeholder_text_color='#545454',
                                   height=40,
                                   corner_radius=30,
                                   font=("Arial", 17, "italic"),
                                   bg_color="white",
                                   fg_color="white",
                                   text_color="black",
                                   border_color="#545454",
                                   border_width=1,
                                   )
        self.entry_date.place(x=50, y=475)
        self.calendar_image = CTkImage(Image.open("images\\calendar.png"),
                                       size=(20, 20))

        self.button_open_picker = CTkButton(self.register1, command=open_date_picker,image=self.calendar_image,
                                            text='', bg_color='white',
                                            fg_color="white",
                                            width=30,
                                            hover_color="#545454")
        self.button_open_picker.place(x=55, y=480)

        self.phone = CTkEntry(self.register1, width=350,
                                       height=40,
                                       corner_radius=30,
                              placeholder_text="nomer hp",
                                       placeholder_text_color='#545454',
                                       font=("Arial", 17, "italic"),
                                       bg_color="white",
                                       fg_color="white",
                                       text_color="black",
                                       border_color="#545454",
                                       border_width=1,
                                       )

        self.phone.place(x=50, y=555)
        sign_in_label = Label(self.register1, text='Already have an account ?',
                              font=("Microsoft YaHei UI Light", 10, 'bold'), bg="white", fg="black")
        sign_in_label.place(x=240, y=145)
        sign_in_button = Button(self.register1, text='sign in', font=("Microsoft YaHei UI Light", 10, 'bold'),
                                bg="white", fg="blue", border=0, activebackground="white",cursor="hand2", command=self.close_signup)
        sign_in_button.place(x=430, y=143)

        button_signup = CTkButton(self.register1,
                                  text="Sumbit",
                                  font=("ITC Avant Garde Gothic", 25, 'bold'),
                                  width=180,
                                  height=35,
                                  corner_radius=10,
                                  bg_color="black",
                                  fg_color="black",
                                  hover_color="#302E2B",
                                  command=submit
                                  )
        button_signup.place(x=1045, y=660)

        self.image3 = Image.open("images\\submit.png")
        self.image3 = self.image3.resize((1280, 720))
        self.photo3 = ImageTk.PhotoImage(self.image3)
        self.canvas2 = Canvas(self.register2, width=1366, height=768, bg="#C70039")
        self.canvas2.pack()
        self.canvas2.create_image(0, 0, anchor='nw', image=self.photo3)

        self.field_username_signup = CTkEntry(self.register2, width=350,
                                          height=40,
                                          corner_radius=30,
                                          font=("Arial", 17, "italic"),
                                          placeholder_text_color='#545454',
                                          bg_color="white",
                                          fg_color="white",
                                          border_color="#545454",
                                          text_color="black",
                                          border_width=1
                                          )
        self.field_username_signup.place(x=50, y=290)

        self.field_password_signup = CTkEntry(self.register2, width=350,
                                              height=40,
                                              corner_radius=30,
                                              font=("Arial", 17, "italic"),
                                              placeholder_text_color='#545454',
                                              bg_color="white",
                                              fg_color="white",
                                              border_color="#545454",
                                              text_color="black",
                                              border_width=1
                                              )
        self.field_password_signup.place(x=50, y=404)

        self.field_cpassword_signup = CTkEntry(self.register2, width=350,
                                              height=40,
                                              corner_radius=30,
                                              font=("Arial", 17, "italic"),
                                              placeholder_text_color='#545454',
                                              bg_color="white",
                                              fg_color="white",
                                              border_color="#545454",
                                              text_color="black",
                                              border_width=1
                                              )
        self.field_cpassword_signup.place(x=50, y=514)
        back_image = CTkImage(Image.open("images\\back.png"),size=(40, 40))
        def back():
            self.show_register1()
        button_back = CTkButton(self.register2,
                                text= "",
                                font=("ITC Avant Garde Gothic", 25, 'bold'),

                                width=50,
                                height=55,
                                image=back_image,
                                corner_radius=10,
                                bg_color="white",
                                fg_color="white",
                                hover= False,
                                command=back
                                )
        button_back.place(x=25,y=180)
        def yes():
            check_counter = 0
            warn = ""
            if self.field_username_signup.get() == "":
                warn = 'create your username'
            else :
                check_counter +=1
            if self.field_password_signup.get() == "":
                warn = 'fill the passford field'
            else:
                check_counter += 1
            if self.field_cpassword_signup.get() == "":
                warn = 'please confirm your password'
            else :
                check_counter +=1
            if not self.field_cpassword_signup.get() == self.field_password_signup.get():
                warn = "your passowrd not same bro"
            else :
                check_counter += 1

            if check_counter == 4:
                try:
                    conn = connect_db()
                    cur = conn.cursor()
                    query = "insert into pelanggan (username,password,fullname,email,phone_number,birthdate,nik) values(%s,%s,%s,%s,%s,%s,%s)"
                    cur.execute(query, (self.field_username_signup.get(),
                                        self.field_password_signup.get(),
                                        self.field_name_signup.get(),
                                        self.field_email_signup.get(),
                                        self.phone.get(),
                                        self.entry_date.get(),
                                        self.nik_signup.get()
                                        ))
                    conn.commit()
                    cur.close()
                    conn.close()
                    messagebox.showinfo("got it!", "login berhasil", parent=self.register2)
                    self.close_signup()
                except Exception as e:
                    print(f'terjadi kesalahan {e}')
            else :
                messagebox.showerror("Error",warn)

        button_submit = CTkButton(self.register2,
                                  text="Sign Up",
                                  font=("ITC Avant Garde Gothic", 25, 'bold'),
                                  width=200,
                                  height=55,
                                  corner_radius=10,
                                  bg_color="white",
                                  fg_color="black",
                                  hover_color="#302E2B",
                                  command=yes,

                                  )
        button_submit.place(x=210, y=600)
        #         def show():
        #             try:
        #                 self.show_password_button.configure(image=self.show_image, command=hide)
        #                 self.password_loginpage.configure(show='')
        #                 self.field_password.configure(show='')
        #                 self.field_cpassword.configure(show='')
        #             except AttributeError as e:
        #                 pass
        #
        #         def hide():
        #             try:
        #                 self.show_password_button.configure(image=self.hide_image, command=show)
        #                 self.password_loginpage.configure(show='*')
        #                 self.field_password.configure(show='*')
        #                 self.field_cpassword.configure(show='*')
        #             except AttributeError as e:
        #                 pass
        #         self.show_password_button = CTkButton(self.sign_up_menu, command=show, text=""
        #                                               , bg_color="white", fg_color="white", width=20,
        #                                                image=self.hide_image, hover= False)
        #         self.show_password_button.place(relx= 0.1 , rely= 0.665)

    def close_signup(self):
        self.loginpage.deiconify()
        self.sign_up_menu.withdraw()
    def show_register1(self):
        self.register1.tkraise()

    def show_register2(self):
        self.register2.tkraise()



    def mainmenu(self):
        win = Toplevel()
        dashboard.DashboardPage(win)
        self.loginpage.withdraw()
        win.deiconify()
#
    def adminmenu(self):
        win = Toplevel()
        etmin.Adminpage(win)
        self.loginpage.withdraw()
        win.deiconify()
#
#
def login(username, password):
    connection = connect_db()
    cursor = connection.cursor()


    find_customer = 'SELECT * FROM pelanggan WHERE username = %s AND password = %s'
    cursor.execute(find_customer, (username, password))
    customer_result = cursor.fetchall()

    find_admin = 'SELECT * FROM admin WHERE username = %s AND password = %s'
    cursor.execute(find_admin, (username, password))
    admin_result = cursor.fetchall()

    if customer_result:

        cursor.execute("UPDATE pelanggan SET status = 1 WHERE username = %s",
                       (username,))
        connection.commit()
        connection.close()
        return "customer", username
    elif admin_result:
        connection.close()
        return 'admin','admin'

    else:
        connection.close()
        return None, None


def get_login_info(username):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT status FROM pelanggan WHERE username = %s", (username,))
    customer_info = cursor.fetchone()

    connection.close()
    return customer_info


def tampilkan_info_login(username):
    login_info = get_login_info(username)
    if login_info:
        status = login_info
        if status:
            print(f"Pengguna {username} .")
        else:
            print(f"Pengguna {username} tidak sedang login.")
    else:
        print(f"Tidak ada pengguna dengan username {username}.")



if __name__ == "__main__":
    root = Tk()
    LoginPage(root)
    root.mainloop()