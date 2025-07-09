from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from customtkinter import CTkButton, CTkEntry, CTkImage,CTkScrollableFrame
from  tkinter import messagebox
# import ProjectApp.LoginPage
import psycopg2


db_config = {
    'host': 'localhost',
    'port': 5432,
    'database': 'berthdb1',
    'user': 'admin',
    'password': 'admin'
}

# try:
#     connection = psycopg2.connect(**db_config)
#     print("Koneksi berhasil!")
#     cur = connection.cursor()
#     connection.commit()
#     print("done.")
#     cur.close()
#     connection.close()
#
#
# except psycopg2.Error as e:
#     print(f"Error: {e}")


class Adminpage:
    def __init__(self, admin_page):
        self.admin_page = admin_page
        admin_page.resizable(False, False)
        admin_page.rowconfigure(0, weight=1)
        admin_page.columnconfigure(0, weight=1)
        screen_width = admin_page.winfo_screenwidth()
        screen_height = admin_page.winfo_height()
        app_width = 1300
        app_height = 670
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 160) - (app_height / 160)
        admin_page.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        self.schedule_page = Frame(admin_page)
        self.report_page = Frame(admin_page)
        self.manage_page = Frame(admin_page)
        self.account = Frame(admin_page)

        for frame in ( self.schedule_page,self.report_page, self.manage_page,self.account) :
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_account()
        def logout() :
            win= Toplevel()
            # ProjectApp.LoginPage.LoginPage(win)
            admin_page.withdraw()
            win.deiconify()
#=======================================================SCHEDULE PAGE=================================================
        schedule_bgImg = Image.open('images\\dashboardetmin.png')
        schedule_bgImg = schedule_bgImg.resize((1300,670))
        photo = ImageTk.PhotoImage(schedule_bgImg)
        bg = Label(self.schedule_page, image=photo,bg='#ffffff')
        bg.image =  photo
        bg.place(x=0,y=0)

        sch_buttonImg = CTkImage(Image.open('images\\schedule button.png'), size=(50, 30))


        button_sch = CTkButton(self.schedule_page, image=sch_buttonImg, fg_color='#dddddd',
                                           bg_color='#dddddd',text="",width=20,hover=False,
                                            command=self.show_schedule,)
        button_sch.place(x=10, y=120)


        set_buttonImg = CTkImage(Image.open('images\\setting.png'), size=(50, 30))
        button_set = CTkButton(self.schedule_page, image=set_buttonImg, fg_color='#dddddd',
                               bg_color='#dddddd', text="", width=20, hover=False,
                               command=self.show_manage, )
        button_set.place(x=10, y=260)

        acc_buttonImg = CTkImage(Image.open('images\\account.png'), size=(50, 30))
        button_acc = CTkButton(self.schedule_page, image=acc_buttonImg, fg_color='#dddddd',
                               bg_color='#dddddd', text="", width=20, hover=False,
                               command=self.show_account, )
        button_acc.place(x=10, y=400)

        report_buttonImg = CTkImage(Image.open('images\\report.png'), size=(50, 30))
        button_report = CTkButton(self.schedule_page, image=report_buttonImg, fg_color='#dddddd',
                               bg_color='#dddddd', text="", width=20, hover=False,
                               command=self.show_schedule, )
        button_report.place(x=10, y=540)

        notif_buttonImg = CTkImage(Image.open('images\\notif.png'), size=(50, 30))
        button_notif = CTkButton(self.schedule_page, image=notif_buttonImg, fg_color='#122844',
                               bg_color='#122844', text="", width=20, hover=False,
                               command=self.show_schedule, )
        button_notif.place(x=1070, y=10)

        exit_buttonImg = CTkImage(Image.open('images\\exit.png'), size=(50, 30))
        button_exit = CTkButton(self.schedule_page, image=exit_buttonImg, fg_color='#122844',
                                 bg_color='#122844', text="", width=20, hover=False,
                                 command=self.show_schedule, )
        button_exit.place(x=1200, y=10)

        coverFrame = CTkScrollableFrame(self.schedule_page,width=1055, height=500,bg_color='white',fg_color='white')
        coverFrame.place(x=271, y=205)

        ids = StringVar()
        day = StringVar()
        dep_time = StringVar()
        arr_time = StringVar()
        ship = StringVar()
        # destination = StringVar()
        kelas = StringVar()

        id_lbel = Label(self.schedule_page, text=' Nomer ', bg='white', fg='black', font=('Poppins', 10))
        id_lbel.place(x=289, y=80)
        id_entry = CTkEntry(self.schedule_page, textvariable=ids, text_color='black',
                             placeholder_text_color='black', width=120, height=43, bg_color='white',
                             border_color='black', fg_color='white')
        id_entry.place(x=285, y=100)

        day_lbel = Label(self.schedule_page, text=' DAY ', bg='white', fg='black', font=('Poppins', 10))
        day_lbel.place(x=439, y=80)
        day_entry = CTkEntry(self.schedule_page, textvariable=day, text_color='black',
                             placeholder_text_color='black', width=120, height=43, bg_color='white',
                             border_color='black', fg_color='white')
        day_entry.place(x=437, y=100)
        dep_lbel = Label(self.schedule_page, text=' DEP_TIME ', bg='white', fg='black', font=('Poppins', 10))
        dep_lbel.place(x=585, y=80)
        dep_entry = CTkEntry(self.schedule_page, textvariable=dep_time, text_color='black',
                             placeholder_text_color='black', width=120, height=43, bg_color='white',
                             border_color='black', fg_color='white')
        dep_entry.place(x=583, y=100)
        arr_lbel = Label(self.schedule_page, text=' ARR_TIME ', bg='white', fg='black', font=('Poppins', 10))
        arr_lbel.place(x=735, y=80)
        arr_entry = CTkEntry(self.schedule_page, textvariable=arr_time, text_color='black',
                             placeholder_text_color='black', width=120, height=43, bg_color='white',
                             border_color='black', fg_color='white')
        arr_entry.place(x=733, y=100)
        ship_lbel = Label(self.schedule_page, text=' SHIP ', bg='white', fg='black', font=('Poppins', 10))
        ship_lbel.place(x=885, y=80)
        ship_entry = CTkEntry(self.schedule_page, placeholder_text_color="black", textvariable=ship,
                              width=120, height=43, bg_color='white', border_color='black', text_color='black',
                              fg_color='white', font=('Poppins', 12))
        ship_entry.place(x=883, y=100)
        # des_lbel = Label(self.schedule_page, text=' DESTINATION ', bg='white', fg='black', font=('Poppins', 10))
        # des_lbel.place(x=1035, y=80)
        # des_entry = CTkEntry(self.schedule_page, textvariable=destination,
        #                      placeholder_text_color='black', width=128, height=43, bg_color='white', text_color='black',
        #                      border_color='black',
        #                      fg_color='white')
        # des_entry.place(x=1033, y=100)
        kelas_lbel = Label(self.schedule_page, bg='white', fg='black', font=('Poppins', 10), text='CLASS')
        kelas_lbel.place(x=1035, y=80)
        kelas_entry = CTkEntry(self.schedule_page, textvariable=kelas,
                               placeholder_text_color='black', width=128, height=43, bg_color='white',
                               border_color='black', text_color='black',
                               fg_color='white')
        kelas_entry.place(x=1033, y=100)

        def show_all_schedule():
            try:
                connection = psycopg2.connect(**db_config)
                print("Koneksi berhasil!")
                cur = connection.cursor()

                # # Query dengan JOIN untuk mengambil nama kapal
                # query = """
                #     SELECT s.id_schedule,s.day, s.dep_time,s.arr_time, k.nama_kapal,k.tujuan, kk.jenis_kelas
                #     FROM schedule s
                #     JOIN kapal k ON s.id_kapal = k.id_kapal
                #     JOIN kelas kk ON s.id_kelas = kk.id_kelas
                #     """
                query = """select * from schedule"""
                cur.execute(query)
                rows = cur.fetchall()

                if len(rows) != 0:
                    schedule_tree.delete(*schedule_tree.get_children())
                    for row in rows:
                        schedule_tree.insert('', 'end', values=row)  # Tambahkan row ke Treeview

                connection.commit()
                cur.close()
                connection.close()
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")

        def berth_info(ev):
            viewInfo = schedule_tree.focus()
            berth_data = schedule_tree.item(viewInfo)
            row = berth_data['values']
            ids.set(row[0])
            day.set(row[1])
            dep_time.set(row[2])
            arr_time.set(row[3])
            ship.set(row[4])
            # destination.set(row[5])
            kelas.set(row[5])
        #
        def add_schedule():
            try:
                conn = psycopg2.connect(**db_config)
                print("Koneksi berhasil!")
                cur = conn.cursor()

                cur.execute(
                    "INSERT INTO schedule (day, dep_time, arr_time, id_kapal,id_kelas) VALUES (%s, %s, %s,%s, %s)",
                    (day.get(), dep_time.get(), arr_time.get(),ship.get(),kelas.get())
                )

                conn.commit()
                cur.close()
                conn.close()
                messagebox.showinfo("Sukses", f" jadwal {day.get()} telah ditambahkan ke database .")
                show_all_schedule()
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")

        def clear_all_record():
            ids.set("")
            day.set("")
            dep_time.set("")
            arr_time.set("")
            ship.set("")
            # destination.set("")
            kelas.set("")


        def delete_records_sch():
            try:
                tree_view_content = schedule_tree.focus()
                tree_view_items = schedule_tree.item(tree_view_content)
                tree_view_values = tree_view_items['values'][1]
                id_schedule_to_delete = tree_view_items['values'][0]

                ask = messagebox.askyesno("PERINGATAN",
                                          "Are you sure you want to delete records ?")
                if ask is True:
                    conn = psycopg2.connect(**db_config)
                    print("Koneksi berhasil!")
                    cur = conn.cursor()

                    cur.execute("DELETE FROM schedule WHERE id_schedule = %s", (id_schedule_to_delete,))
                    conn.commit()
                    conn.close()
                    show_all_schedule()
                    clear_all_record()

                    messagebox.showinfo("Success", f"jadwal {tree_view_values} telah dihapus.")
                else:
                    pass

            except Exception as msg:
                print(msg)
                messagebox.showerror("Error",
                                     "There was an error deleting the data. Make sure you have selected the data.")

        def update_schedule():
            try:
                tree_view_content = schedule_tree.focus()
                tree_view_items = schedule_tree.item(tree_view_content)
                tree_view_values = tree_view_items['values'][1]
                id_schedule_to_update = tree_view_items['values'][0]

                ask = messagebox.askyesno("PERINGATAN",
                                          "Are you sure you want to update the records?")
                if ask is True:
                    conn = psycopg2.connect(**db_config)
                    print("Koneksi berhasil!")
                    cur = conn.cursor()

                    cur.execute(
                        """UPDATE schedule SET day = %s, dep_time = %s, arr_time = %s ,id_kapal = %s, id_kelas = %s WHERE id_schedule = %s""",
                        (day.get(), dep_time.get(), arr_time.get(),ship.get(),kelas.get(), id_schedule_to_update)
                    )
                    conn.commit()
                    conn.close()
                    show_all_schedule()
                    messagebox.showinfo("Success", "Berth Record updated successfully!")

                else:
                    pass

            except Exception as e:
                print(f"Error: {e}")
                messagebox.showerror("Error", "There was an error updating the record.")

        def show_user_sch():
            show_schedule = Toplevel()
            show_schedule.title('Tinjau Schedule')
            show_schedule.resizable(False, False)
            height = 450
            width = 860
            x = (show_schedule.winfo_screenwidth() // 2) - (width // 2)
            y = (show_schedule.winfo_screenheight() // 4) - (height // 4)
            show_schedule.geometry('{}x{}+{}+{}'.format(width, height, x, y))

            def user_sch():
                try:
                    connection = psycopg2.connect(**db_config)
                    print("Koneksi berhasil!")
                    cur = connection.cursor()

                    query = """
                        SELECT s.id_schedule,s.day, s.dep_time, k.nama_kapal,k.tujuan, kk.jenis_kelas
                        FROM schedule s
                        JOIN kapal k ON s.id_kapal = k.id_kapal
                        JOIN kelas kk ON s.id_kelas = kk.id_kelas
                        """
                    cur.execute(query)
                    rows = cur.fetchall()

                    if len(rows) != 0:
                        schedule_tree1.delete(*schedule_tree1.get_children())
                        for row in rows:
                            schedule_tree1.insert('', 'end', values=row)

                    connection.commit()
                    cur.close()
                    connection.close()
                except Exception as e:
                    print(f"Terjadi kesalahan: {e}")

            style = ttk.Style()
            style.theme_use('clam')
            style.configure("mystyle.Treeview", rowheight=30,
                            fieldbackground="#1E1E1E",
                            background="#1E1E1E",
                            foreground="#E6E6E6",
                            font=("Arial", 10))
            style.configure("mystyle.Treeview.Heading", background="#333333", foreground="#CFFF53")
            style.map("mystyle.Treeview", background=[("selected", "#87CEEB")],
                      foreground=[("selected", "#000000")])

            style.layout("mystyle.Treeview", [('my style.Treeview.treearea', {'sticky': 'nswe'})])

            schedule_tree1 = ttk.Treeview(show_schedule, style="mystyle.Treeview")
            schedule_tree1.pack()

            schedule_tree1.configure(
                columns=(
                    "No.",
                    "day",
                    "dep_time",
                    # "arr_time",
                    "ship",
                    "destination",
                    "class"
                )
            )
            schedule_tree1.heading("No.", text="No.", anchor=N)
            schedule_tree1.heading("day", text="day", anchor=N)
            schedule_tree1.heading("dep_time", text="dep_time", anchor=N)
            # schedule_tree1.heading("arr_time", text="arr_time", anchor=N)
            schedule_tree1.heading("ship", text="ship", anchor=N)
            schedule_tree1.heading("destination", text="destination", anchor=N)
            schedule_tree1.heading("class", text="class", anchor=N)

            schedule_tree1.column("#0", stretch=NO, minwidth=0, width=0, )
            schedule_tree1.column("#1", stretch=YES, minwidth=0, width=100, anchor=N)
            schedule_tree1.column("#2", stretch=YES, minwidth=0, width=100, anchor=N)
            schedule_tree1.column("#3", stretch=YES, minwidth=0, width=100, anchor=N)
            schedule_tree1.column("#4", stretch=YES, minwidth=0, width=100, anchor=N)
            schedule_tree1.column("#5", stretch=YES, minwidth=0, width=100, anchor=N)
            schedule_tree1.column("#6", stretch=YES, minwidth=0, width=100, anchor=N)
            user_sch()



        clear_button = CTkButton(self.schedule_page, text=" CLEAR ", text_color='white',
                                 corner_radius=20, width=84, height=25, fg_color='black', bg_color='white',
                                 hover_color='#272121', command=clear_all_record)
        clear_button.place(x=640, y=184)
        update_button = CTkButton(self.schedule_page, text=" UPDATE ", text_color='white',
                                  corner_radius=20, width=84, height=25, fg_color='black', bg_color='white',
                                  hover_color='#272121', command=update_schedule)
        update_button.place(x=520, y=184)

        add_button = CTkButton(self.schedule_page, text=" ADD ", text_color='white',
                               corner_radius=20, width=84, height=25, fg_color='black', bg_color='white',
                               hover_color='#272121', command=add_schedule)
        add_button.place(x=287, y=184)

        delete_button = CTkButton(self.schedule_page, text=" DELETE ", text_color='white',
                                  corner_radius=20, width=84, height=25, fg_color='black', bg_color='white',
                                  hover_color='#272121', command=delete_records_sch)

        delete_button.place(x=400, y=184)

        tinjau_buttonImg = CTkImage(Image.open('images\\show.png'), size=(50, 30))
        button_tinjau = CTkButton(self.schedule_page, image=tinjau_buttonImg, fg_color='white',
                                 bg_color='white', text="", width=20, hover=False,
                                 command=show_user_sch, )
        button_tinjau.place(x=820, y=184)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("mystyle.Treeview",rowheight=30,
            fieldbackground="#1E1E1E",
            background="#1E1E1E",
            foreground="#E6E6E6",
            font=("Arial", 10))
        style.configure("mystyle.Treeview.Heading",background="#333333",foreground="#CFFF53")
        style.map("mystyle.Treeview",background=[("selected", "#87CEEB")],
            foreground=[("selected", "#000000")])

        style.layout("mystyle.Treeview", [('my style.Treeview.treearea', {'sticky': 'nswe'})])

        schedule_tree = ttk.Treeview(coverFrame, style="mystyle.Treeview")

        schedule_tree.grid(row=0, column=1, pady=20)
        # scrollbary1 = Scrollbar(self.schedule_page, orient=VERTICAL)
        #
        # schedule_tree.configure(yscrollcommand=scrollbary1.set)
        # scrollbary1.configure(command=schedule_tree.yview)
        # scrollbary1.place(relx=0.973, rely=0.323, width=25, height=412)


        #
        #
        schedule_tree.configure(
            columns=(
                "No.",
                "day",
                "dep_time",
                "arr_time",
                "ship",
                # "destination",
                "class"
            )
        )
        schedule_tree.heading("No.", text="No.", anchor=N)
        schedule_tree.heading("day", text="day", anchor=N)
        schedule_tree.heading("dep_time", text="dep_time", anchor=N)
        schedule_tree.heading("arr_time",text="arr_time",anchor=N)
        schedule_tree.heading("ship", text="ship", anchor=N)
        # schedule_tree.heading("destination", text="destination", anchor=N)
        schedule_tree.heading("class", text="class", anchor=N)

        schedule_tree.column("#0", stretch=NO, minwidth=0, width=0,)
        schedule_tree.column("#1", stretch=YES, minwidth=0, width=100, anchor=N)
        schedule_tree.column("#2", stretch=YES, minwidth=0, width=100, anchor=N)
        schedule_tree.column("#3", stretch=YES, minwidth=0, width=100, anchor=N)
        schedule_tree.column("#4", stretch=YES, minwidth=0, width=100, anchor=N)
        schedule_tree.column("#5", stretch=YES, minwidth=0, width=100, anchor=N)
        schedule_tree.column("#6", stretch=YES, minwidth=0, width=100, anchor=N)
        schedule_tree.bind("<ButtonRelease-1>", berth_info)
        show_all_schedule()



# #====================================================MANAGE PAGE==========================================
        schedule_bgImg = Image.open('images\\dashboardetmin.png')
        schedule_bgImg = schedule_bgImg.resize((1300,670))
        photo = ImageTk.PhotoImage(schedule_bgImg)
        bg = Label(self.manage_page, image=photo,bg='#ffffff')
        bg.image =  photo
        bg.place(x=0,y=0)

        sch_buttonImg = CTkImage(Image.open('images\\schedule button.png'), size=(50, 30))
        button_sch = CTkButton(self.manage_page, image=sch_buttonImg, fg_color='#dddddd',
                                           bg_color='#dddddd',text="",width=20,hover=False,
                                            command=self.show_schedule,)
        button_sch.place(x=10, y=120)

        set_buttonImg = CTkImage(Image.open('images\\setting.png'), size=(50, 30))
        button_set = CTkButton(self.manage_page, image=set_buttonImg, fg_color='#dddddd',
                               bg_color='#dddddd', text="", width=20, hover=False,
                               command=self.show_manage, )
        button_set.place(x=10, y=260)

        acc_buttonImg = CTkImage(Image.open('images\\account.png'), size=(50, 30))
        button_acc = CTkButton(self.manage_page, image=acc_buttonImg, fg_color='#dddddd',
                               bg_color='#dddddd', text="", width=20, hover=False,
                               command=self.show_account, )
        button_acc.place(x=10, y=400)

        report_buttonImg = CTkImage(Image.open('images\\report.png'), size=(50, 30))
        button_report = CTkButton(self.manage_page, image=report_buttonImg, fg_color='#dddddd',
                               bg_color='#dddddd', text="", width=20, hover=False,
                               command=self.show_manage, )
        button_report.place(x=10, y=540)

        notif_buttonImg = CTkImage(Image.open('images\\notif.png'), size=(50, 30))
        button_notif = CTkButton(self.manage_page, image=notif_buttonImg, fg_color='#122844',
                               bg_color='#122844', text="", width=20, hover=False,
                               command=self.show_manage, )
        button_notif.place(x=1070, y=10)

        exit_buttonImg = CTkImage(Image.open('images\\exit.png'), size=(50, 30))
        button_exit = CTkButton(self.manage_page, image=exit_buttonImg, fg_color='#122844',
                                 bg_color='#122844', text="", width=20, hover=False,
                                 command=self.show_manage, )
        button_exit.place(x=1200, y=10)

        coverFrame1 = CTkScrollableFrame(self.manage_page, bg_color='white',fg_color='white',width=1055, height=500)
        coverFrame1.place(x=271, y=265)

        id_kapal = StringVar()
        nama_kapal = StringVar()
        tujuan = StringVar()
        kapasitas = StringVar()

        id_lbel = Label(self.manage_page, text=' ID ', bg='white', fg='black', font=('Poppins', 10))
        id_lbel.place(x=289, y=80)
        id_entry = CTkEntry(self.manage_page, textvariable=id_kapal, text_color='black',
                             placeholder_text_color='black', width=120, height=43, bg_color='white',
                             border_color='black', fg_color='white')
        id_entry.place(x=287, y=100)
        nama_kapal_lbel = Label(self.manage_page, text=' Nama Kapal ', bg='white', fg='black', font=('Poppins', 10))
        nama_kapal_lbel.place(x=435, y=80)
        nama_kapal_entry = CTkEntry(self.manage_page, textvariable=nama_kapal, text_color='black',
                             placeholder_text_color='black', width=120, height=43, bg_color='white',
                             border_color='black', fg_color='white')
        nama_kapal_entry.place(x=430, y=100)
        tujuan_lbel = Label(self.manage_page, text=' Tujuan ', bg='white', fg='black', font=('Poppins', 10))
        tujuan_lbel.place(x=585, y=80)
        tujuan_entry = CTkEntry(self.manage_page, placeholder_text_color="black", textvariable=tujuan,
                              width=193, height=43, bg_color='white', border_color='black', text_color='black',
                              fg_color='white', font=('Poppins', 12))
        tujuan_entry.place(x=583, y=100)
        capacity_lbel = Label(self.manage_page, text=' Capacity ', bg='white', fg='black', font=('Poppins', 10))
        capacity_lbel.place(x=805, y=80)
        capacity_entry = CTkEntry(self.manage_page, textvariable=kapasitas,
                             placeholder_text_color='black', width=128, height=43, bg_color='white', text_color='black',
                             border_color='black',
                             fg_color='white')
        capacity_entry.place(x=803, y=100)
        
        def show_all_Ship():
            try:
                connection = psycopg2.connect(**db_config)
                print("Koneksi berhasil!")
                cur = connection.cursor()
                cur.execute('select * from kapal')
                rows = cur.fetchall()

                # Menampilkan data di Treeview
                if len(rows) != 0:
                    ship_tree.delete(*ship_tree.get_children())
                    for row in rows:
                        ship_tree.insert('', 'end', values=row)

                connection.commit()
                cur.close()
                connection.close()
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")

        def ship_info(ev):
            viewInfo = ship_tree.focus()
            berth_data = ship_tree.item(viewInfo)
            row = berth_data['values']
            id_kapal.set(row[0])
            nama_kapal.set(row[1])
            tujuan.set(row[2])
            kapasitas.set(row[3])

        def add_ship():
            try:
                    conn= psycopg2.connect(**db_config)
                    print("Koneksi berhasil!")
                    cur = conn.cursor()

                    cur.execute(
                        "INSERT INTO kapal (nama_kapal, tujuan, kapasitas) VALUES (%s, %s, %s)",
                        (nama_kapal.get(), tujuan.get(), kapasitas.get())
                    )

                    conn.commit()
                    cur.close()
                    conn.close()
                    messagebox.showinfo("Sukses",f" kapal {nama_kapal.get()} telah ditambahkan ke database .")
                    show_all_Ship()
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")

        def clear_all_ship():
            id_kapal.set("")
            nama_kapal.set("")
            tujuan.set("")
            kapasitas.set("")

        def delete_records():
            try:
                # Ambil ID kapal dari Treeview yang dipilih
                tree_view_content = ship_tree.focus()
                tree_view_items = ship_tree.item(tree_view_content)
                tree_view_values = tree_view_items['values'][1]  # Pastikan indeks ini sesuai dengan ID kapal
                id_kapal_to_delete = tree_view_items['values'][0]  # Asumsi id_kapal berada pada kolom pertama

                # Tanyakan konfirmasi kepada user
                ask = messagebox.askyesno("PERINGATAN",
                                          f"Are you sure you want to delete records of {tree_view_values}?")
                if ask is True:
                    # Koneksi ke database PostgreSQL
                    conn = psycopg2.connect(**db_config)
                    print("Koneksi berhasil!")
                    cur = conn.cursor()

                    # Query untuk menghapus data berdasarkan ID kapal
                    cur.execute("DELETE FROM kapal WHERE id_kapal = %s", (id_kapal_to_delete,))

                    # Commit perubahan dan tutup koneksi
                    conn.commit()
                    conn.close()

                    # Tampilkan data yang sudah diupdate
                    show_all_Ship()
                    clear_all_ship()

                    messagebox.showinfo("Success", f"Records of {tree_view_values} have been deleted successfully.")
                else:
                    pass

            except Exception as msg:
                print(msg)
                messagebox.showerror("Error",
                                     "There was an error deleting the data. Make sure you have selected the data.")

        def update():
            try:
                # Ambil ID kapal yang akan diupdate
                tree_view_content = ship_tree.focus()
                tree_view_items = ship_tree.item(tree_view_content)
                tree_view_values = tree_view_items['values'][1]
                id_kapal_to_update = tree_view_items['values'][0]  # ID kapal

                ask = messagebox.askyesno("PERINGATAN",
                                          f"Are you sure you want to update the records of {tree_view_values}?")
                if ask is True:
                    conn = psycopg2.connect(**db_config)
                    print("Koneksi berhasil!")
                    cur = conn.cursor()

                    cur.execute(
                        """UPDATE kapal SET nama_kapal = %s, tujuan = %s, kapasitas = %s WHERE id_kapal = %s""",
                        (nama_kapal.get(), tujuan.get(), kapasitas.get(), id_kapal_to_update)
                    )
                    conn.commit()
                    conn.close()
                    show_all_Ship()
                    messagebox.showinfo("Success", "Berth Record updated successfully!")

                else:
                    pass

            except Exception as e:
                print(f"Error: {e}")
                messagebox.showerror("Error", "There was an error updating the record.")

        def sort_id_kapal():
            try:
                # Koneksi ke database PostgreSQL
                conn = psycopg2.connect(**db_config)
                cur = conn.cursor()

                # Ambil semua data kapal dalam urutan tertentu
                cur.execute("SELECT id_kapal FROM kapal ORDER BY nama_kapal ASC")
                rows = cur.fetchall()

                # Tahap 1: Ubah semua id_kapal ke nilai sementara
                temp_id_list = []
                for index, row in enumerate(rows, start=1):
                    temp_id = f"temp-{index:03d}"  # Format ID sementara (temp-001, temp-002, ...)
                    old_id = row[0]
                    temp_id_list.append((temp_id, old_id))
                    # Update id_kapal di tabel kapal
                    cur.execute("UPDATE kapal SET id_kapal = %s WHERE id_kapal = %s", (temp_id, old_id))
                    # Update foreign key di tabel schedule
                    cur.execute("UPDATE schedule SET id_kapal = %s WHERE id_kapal = %s", (temp_id, old_id))

                # Tahap 2: Ubah nilai sementara ke nilai final
                for index, (temp_id, old_id) in enumerate(temp_id_list, start=1):
                    new_id = f"kpl-{index:03d}"  # Format ID final (kpl-001, kpl-002, ...)
                    # Update id_kapal di tabel kapal
                    cur.execute("UPDATE kapal SET id_kapal = %s WHERE id_kapal = %s", (new_id, temp_id))
                    # Update foreign key di tabel schedule
                    cur.execute("UPDATE schedule SET id_kapal = %s WHERE id_kapal = %s", (new_id, temp_id))

                # Commit perubahan dan tutup koneksi
                conn.commit()
                conn.close()

                # Refresh tampilan dan tampilkan pesan sukses
                show_all_Ship()  # Fungsi untuk refresh data di TreeView
                messagebox.showinfo("Success", "ID Kapal berhasil diurutkan kembali!")

            except Exception as e:
                print(f"Error: {e}")
                messagebox.showerror("Error", "Terjadi kesalahan saat melakukan sorting ID Kapal.")

        clear_button = CTkButton(self.manage_page, text=" CLEAR ", text_color='white',
                                 corner_radius=20, width=84, height=25, fg_color='black', bg_color='white',
                                 hover_color='#272121',command=clear_all_ship)
        clear_button.place(x=640, y=184)
        update_button = CTkButton(self.manage_page, text=" UPDATE ", text_color='white',
                                  corner_radius=20, width=84, height=25, fg_color='black', bg_color='white',
                                  hover_color='#272121', command=update)
        update_button.place(x=520, y=184)

        add_button = CTkButton(self.manage_page, text=" ADD ", text_color='white',
                               corner_radius=20, width=84, height=25, fg_color='black', bg_color='white',
                               hover_color='#272121',command=add_ship)
        add_button.place(x=287, y=184)

        delete_button = CTkButton(self.manage_page, text=" DELETE ", text_color='white',
                                  corner_radius=20, width=84, height=25, fg_color='black', bg_color='white',
                                  hover_color='#272121',command=delete_records)


        delete_button.place(x=400, y=184)

        style1= ttk.Style()
        style1.theme_use('clam')
        ship_tree = ttk.Treeview(coverFrame1, )
        ship_tree.grid(row=1,column=1)

        #
        #
        ship_tree.configure(
            columns=(
                "id",
                "Nama kapal",
                "Tujuan",
                "Kapasitas",
            )
        )
        ship_tree.heading("id", text="ID", anchor=N,command=sort_id_kapal)
        ship_tree.heading("Nama kapal", text="Nama Kapal", anchor=N)
        ship_tree.heading("Tujuan", text="Tujaun", anchor=N)
        ship_tree.heading("Kapasitas", text="Kapasitas", anchor=N)

        ship_tree.column("#0", stretch=NO, minwidth=0, width=0, )
        ship_tree.column("#1", stretch=YES, minwidth=0, width=100, anchor=N)
        ship_tree.column("#2", stretch=YES, minwidth=0, width=100, anchor=N)
        ship_tree.column("#3", stretch=YES, minwidth=0, width=100, anchor=N)
        ship_tree.column("#4", stretch=YES, minwidth=0, width=100, anchor=N)
        ship_tree.bind("<ButtonRelease-1>", ship_info)
        show_all_Ship()




#
# #==============================================Report Page==========================
#         manage_buttonImg = CTkImage(Image.open('image1\\manage.png'), size=(45, 40))
#         button_manage = CTkButton(self.report_page, image=manage_buttonImg, fg_color='#1E1D16',
#                                   bg_color='#1E1D16', text='Manage', text_color='white', hover_color='#272121',
#                                   compound=LEFT, font=('Canva Sans', 15, 'bold'), width=30, command=self.show_manage)
#         button_manage.place(x=25, y=200)
#
#         report_buttonImg = CTkImage(Image.open('image1\\report.png'), size=(50, 50))
#         button_report = CTkButton(self.report_page, image=report_buttonImg, fg_color='#1E1D16',
#                                   bg_color='#1E1D16', text='Report', text_color='white', hover_color='#272121',
#                                   compound=LEFT, font=('Canva Sans', 15, 'bold'), width=80, command=self.show_report)
#         button_report.place(x=25, y=260)
#         profile_buttonImg = CTkImage(Image.open('image1\\profile.png'), size=(50, 50))
#         button_profile = CTkButton(self.report_page, image=profile_buttonImg, fg_color='#1E1D16',
#                                    bg_color='#1E1D16', text='Account', text_color='white', hover_color='#272121',
#                                    compound=LEFT, font=('Canva Sans', 15, 'bold'), width=80, command=self.show_account)
#         button_profile.place(x=25, y=320)
#
#         exit_buttonImg = CTkImage(Image.open("./image1/exit.png"), size=(65, 50))
#         exit_button = CTkButton(self.report_page, image=exit_buttonImg, fg_color='#1E1D16', bg_color='#1E1D16',
#                                 text=' Back Home ', text_color='white', hover_color='#272121', compound=LEFT,
#                                 font=('Canva Sans', 15, 'bold'), width=80, command=logout)
#         exit_button.place(x=28, y=550)
# #===========================================Account page=================================================
#         manage_buttonImg = CTkImage(Image.open('image1\\manage.png'), size=(45, 40))
#         button_manage = CTkButton(self.account, image=manage_buttonImg, fg_color='#1E1D16',
#                                   bg_color='#1E1D16', text='Manage', text_color='white', hover_color='#272121',
#                                   compound=LEFT, font=('Canva Sans', 15, 'bold'), width=30, command=self.show_manage)
#         button_manage.place(x=25, y=200)
#
#         report_buttonImg = CTkImage(Image.open('image1\\report.png'), size=(50, 50))
#         button_report = CTkButton(self.account, image=report_buttonImg, fg_color='#1E1D16',
#                                   bg_color='#1E1D16', text='Report', text_color='white', hover_color='#272121',
#                                   compound=LEFT, font=('Canva Sans', 15, 'bold'), width=80, command=self.show_report)
#         button_report.place(x=25, y=260)
#         profile_buttonImg = CTkImage(Image.open('image1\\profile.png'), size=(50, 50))
#         button_profile = CTkButton(self.account, image=profile_buttonImg, fg_color='#1E1D16',
#                                    bg_color='#1E1D16', text='Account', text_color='white', hover_color='#272121',
#                                    compound=LEFT, font=('Canva Sans', 15, 'bold'), width=80, command=self.show_account)
#         button_profile.place(x=25, y=320)
#
#         exit_buttonImg = CTkImage(Image.open("./image1/exit.png"), size=(65, 50))
#         exit_button = CTkButton(self.account, image=exit_buttonImg, fg_color='#1E1D16', bg_color='#1E1D16',
#                                 text=' Back Home ', text_color='white', hover_color='#272121', compound=LEFT,
#                                 font=('Canva Sans', 15, 'bold'), width=80, command=logout)
#         exit_button.place(x=28, y=550)
#
#         #=========================================TREE VIEW FRAME===================================



#         coverFrame2 = Frame(self.account, bg='white')
#         coverFrame2.place(x=271, y=165, width=1055, height=500)
#




#===============================================TREE VIEW===============================



        # schedule_tree.bind("<ButtonRelease-1>", berth_info)
        # show_all()
        #
        # design_line = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
        # design_line.place(x=23, y=48)
        #
        # design_line2 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
        # design_line2.place(x=23, y=68)
        #
        # design_line3 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
        # design_line3.place(x=23, y=88)
        #
        # design_line4 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
        # design_line4.place(x=23, y=108)
        #
        # design_line5 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
        # design_line5.place(x=23, y=128)
        #
        # design_line6 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
        # design_line6.place(x=23, y=148)
        #
        # design_line7 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
        # design_line7.place(x=23, y=168)
        #
        # design_line8 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
        # design_line8.place(x=23, y=188)
        #
        # design_line9 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
        # design_line9.place(x=23, y=208)
        #
        # design_line10 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
        # design_line10.place(x=23, y=228)
        #
        # design_line11 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
        # design_line11.place(x=23, y=248)
        #
        # design_line12 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
        # design_line12.place(x=23, y=268)
        #
        # design_line13 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
        # design_line13.place(x=23, y=288)
        #
        # design_line14 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
        # design_line14.place(x=23, y=308)
        #
        # design_line15 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
        # design_line15.place(x=23, y=328)
        #
        # design_line16 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
        # design_line16.place(x=23, y=348)
        #
        # design_line17 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
        # design_line17.place(x=23, y=368)
        #
        # design_line18 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
        # design_line18.place(x=23, y=388)
        #
        # design_line19 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
        # design_line19.place(x=23, y=408)
#====================================================Report Page===============================
#         conn = sqlite3.connect("./database/Bobashop.db")
#         c = conn.cursor()
#         c.execute("SELECT SUM(total_harga) FROM transaksi_new")
#         total_pendapatan = c.fetchone()[0]
#         total_pendapatan = "{:,.0f}".format(total_pendapatan)
#
#         # Tampilkan pendapatan kotor di GUI
#         self.result_label = Label(self.report_page, text=f"GROSS PROFIT :\tRp {total_pendapatan:}",bg='white',fg='black',width=35,font=("Calibri",13,"bold"))
#         self.result_label.place(x=279, y=50)
#
#         self.modus_label = Label(self.report_page, bg='white',
#                                  fg='black', width=40, font=("Calibri", 13, "bold"))
#         self.modus_label.place(x=297, y=80)
#         c.execute('''SELECT cust_user, COUNT(cust_user) AS jumlah
#                                 FROM transaksi_new
#                                 GROUP BY cust_user
#                                 ORDER BY jumlah DESC;''')
#         result1 = c.fetchall()[0][0]
#
#         self.modus_user_label = Label(self.report_page, bg='white',text=f'User yang paling sering membeli: {result1}',
#                                  fg='black', width=40, font=("Calibri", 13, "bold"))
#         self.modus_user_label.place(x=297, y=110)
#
#         def get_modus_id() :
#             c.execute('''SELECT produk_id, COUNT(produk_id) AS jumlah
#             FROM transaksi_new
#             GROUP BY produk_id
#             ORDER BY jumlah DESC;''')
#             result = c.fetchall()[0][0]
#             return result
#         def get_produk_info(produk_id):
#             # Mendapatkan informasi produk berdasarkan ID produk
#             c.execute("SELECT Product_name FROM produk WHERE id=?", (produk_id,))
#             result = c.fetchone()
#             return result
#
#         def nama_produk(produk_name):
#             self.modus_label.config(text=f"Produk yang paling sering dibeli : {produk_name}")
#
#
#         def load_and_update_produk_info():
#             produk_id = get_modus_id()
#             produk_name1 = get_produk_info(produk_id)
#             produk_name = produk_name1[0]
#             nama_produk(produk_name)
#
#         load_and_update_produk_info()
#
#

#         schedule_tree1 = ttk.Treeview(coverFrame1)
#         schedule_tree1.place(relx=0.013, rely=0.009, width=770, height=430)
#         scrollbarx1 = Scrollbar(self.report_page, orient=HORIZONTAL)
#         scrollbary1 = Scrollbar(self.report_page, orient=VERTICAL)
#
#
#         schedule_tree1.configure(xscrollcommand=scrollbarx1.set, yscrollcommand=scrollbary1.set)
#         schedule_tree1.configure(selectmode="extended")
#
#         scrollbarx1.configure(command=schedule_tree1.xview)
#         scrollbary1.configure(command=schedule_tree1.yview)
#
#         scrollbary1.place(relx=0.973, rely=0.323, width=25, height=412)
#         scrollbarx1.place(relx=0.3, rely=0.929, width=700, height=25)
#
#
#         schedule_tree1.configure(
#             columns=(
#                 "Nomer_transaksi",
#                 "cust_user",
#                 "Produk_id",
#                 "Jumlah",
#                 "total_harga",
#                 "metode_pembayaran",
#                 "waktu_transaksi"
#             )
#         )
#
#         schedule_tree1.heading("Nomer_transaksi", text="NOMER TRANSAKSI", anchor=N)
#         schedule_tree1.heading("cust_user", text="cust_user", anchor=N)
#         schedule_tree1.heading("Produk_id", text="PRODUK ID", anchor=N)
#         schedule_tree1.heading("Jumlah", text="JUMLAH", anchor=N)
#         schedule_tree1.heading("total_harga", text="TOTAL HARGA", anchor=N)
#         schedule_tree1.heading("metode_pembayaran", text="PEMBAYARAN", anchor=N)
#         schedule_tree1.heading("waktu_transaksi", text="WAKTU TRANSAKSI ", anchor=N)
#
#         schedule_tree1.column("#0", stretch=NO, minwidth=0, width=0)
#         schedule_tree1.column("#1", stretch=NO, minwidth=0, width=130, anchor=N)
#         schedule_tree1.column("#2", stretch=NO, minwidth=0, width=130, anchor=N)
#         schedule_tree1.column("#3", stretch=NO, minwidth=0, width=130, anchor=N)
#         schedule_tree1.column("#4", stretch=NO, minwidth=0, width=130, anchor=N)
#         schedule_tree1.column("#5", stretch=NO, minwidth=0, width=130, anchor=N)
#         schedule_tree1.column("#6", stretch=NO, minwidth=0, width=130, anchor=N)
#         schedule_tree1.column("#7", stretch=NO, minwidth=0, width=130, anchor=N)
#         show_all_transaksi()
#

# #=============================================Account Info ===============================================

        acc_bgImg = Image.open('images\\dashboardetmin.png')
        acc_bgImg = acc_bgImg.resize((1300, 670))
        photo = ImageTk.PhotoImage(acc_bgImg)
        bg = Label(self.account, image=photo, bg='#ffffff')
        bg.image = photo
        bg.place(x=0, y=0)

        sch_buttonImg = CTkImage(Image.open('images\\schedule button.png'), size=(50, 30))

        button_sch = CTkButton(self.account, image=sch_buttonImg, fg_color='#dddddd',
                               bg_color='#dddddd', text="", width=20, hover=False,
                               command=self.show_schedule, )
        button_sch.place(x=10, y=120)

        set_buttonImg = CTkImage(Image.open('images\\setting.png'), size=(50, 30))
        button_set = CTkButton(self.account, image=set_buttonImg, fg_color='#dddddd',
                               bg_color='#dddddd', text="", width=20, hover=False,
                               command=self.show_manage, )
        button_set.place(x=10, y=260)

        acc_buttonImg = CTkImage(Image.open('images\\account.png'), size=(50, 30))
        button_acc = CTkButton(self.account, image=acc_buttonImg, fg_color='#dddddd',
                               bg_color='#dddddd', text="", width=20, hover=False,
                               command=self.show_account, )
        button_acc.place(x=10, y=400)

        report_buttonImg = CTkImage(Image.open('images\\report.png'), size=(50, 30))
        button_report = CTkButton(self.account, image=report_buttonImg, fg_color='#dddddd',
                                  bg_color='#dddddd', text="", width=20, hover=False,
                                   )
        button_report.place(x=10, y=540)

        notif_buttonImg = CTkImage(Image.open('images\\notif.png'), size=(50, 30))
        button_notif = CTkButton(self.account, image=notif_buttonImg, fg_color='#122844',
                                 bg_color='#122844', text="", width=20, hover=False,
                                  )
        button_notif.place(x=1070, y=10)

        exit_buttonImg = CTkImage(Image.open('images\\exit.png'), size=(50, 30))
        button_exit = CTkButton(self.account, image=exit_buttonImg, fg_color='#122844',
                                bg_color='#122844', text="", width=20, hover=False,
                                 )
        button_exit.place(x=1200, y=10)

        coverFrame2 = CTkScrollableFrame(self.account, width=1055, height=500, bg_color='white', fg_color='white')
        coverFrame2.place(x=271, y=205)

        cus_id = StringVar()
        username = StringVar()
        password = StringVar()
        fullname = StringVar()
        email = StringVar()
        birthdate = StringVar()
        nik = StringVar()
        status = StringVar()
        # try:
        #     connection = psycopg2.connect(**db_config)
        #     print("Koneksi berhasil!")
        #     cur = connection.cursor()
        #     cur.execute('select * from kapal')
        #     rows = cur.fetchall()
        #
        #     # Menampilkan data di Treeview
        #     if len(rows) != 0:
        #         ship_tree.delete(*ship_tree.get_children())
        #         for row in rows:
        #             ship_tree.insert('', 'end', values=row)
        #
        #     connection.commit()
        #     cur.close()
        #     connection.close()
        # except Exception as e:
        #     print(f"Terjadi kesalahan: {e}")

        def show_all_account():
            try:
                conn = psycopg2.connect(**db_config)
                cur = conn.cursor()
                cur.execute("select * from pelanggan")
                rows = cur.fetchall()
                if len(rows) != 0 :
                    acc_tree.delete(*acc_tree.get_children())
                    for row in rows :
                        acc_tree.insert('','end',values=row)
                conn.commit()
                cur.close()
                conn.close()
            except Exception as e :
                print(f"Terjadi kesalahan: {e}")


        style = ttk.Style()
        style.theme_use("clam")
        acc_tree = ttk.Treeview(coverFrame2,height=200)
        acc_tree.grid(row=1,column=1)
        acc_tree.configure(columns=(
            "Id",
            "Phone Number",
            "Username",
            "Password",
            "Status",
            "Fullname",
            "Birthdate",
            "Email",
            "nik",

        ))

        acc_tree.heading("Id", text="Id", anchor=N)
        acc_tree.heading("Phone Number", text="No. HP",anchor=N)
        acc_tree.heading("Username", text="Username", anchor=N)
        acc_tree.heading("Password", text="Password", anchor=N)
        acc_tree.heading("Status", text="Status", anchor=N)
        acc_tree.heading("Fullname", text="fullname", anchor=N)
        acc_tree.heading("Birthdate", text="Birthdate", anchor=N)
        acc_tree.heading("Email", text="Last seen", anchor=N)
        acc_tree.heading("nik", text="NIK", anchor=N)


        acc_tree.column("#0", stretch=YES, minwidth=0, width=0)
        acc_tree.column("#1", stretch=YES, minwidth=0, width=100, anchor=N)
        acc_tree.column("#2", stretch=YES, minwidth=0, width=100, anchor=N)
        acc_tree.column("#3", stretch=YES, minwidth=0, width=100, anchor=N)
        acc_tree.column("#4", stretch=YES, minwidth=0, width=100, anchor=N)
        acc_tree.column("#5", stretch=YES, minwidth=0, width=100, anchor=N)
        acc_tree.column("#6", stretch=YES, minwidth=0, width=100, anchor=N)
        acc_tree.column("#7", stretch=YES, minwidth=0, width=100, anchor=N)
        acc_tree.column("#8", stretch=YES, minwidth=0, width=100, anchor=N)
        acc_tree.column("#9", stretch=YES, minwidth=0, width=100, anchor=N)

        show_all_account()

    def show_schedule(self):
        self.schedule_page.tkraise()
    def show_report(self):
        self.report_page.tkraise()
    def show_manage(self):
        self.manage_page.tkraise()
    def show_account(self):
        self.account.tkraise()


if __name__ == '__main__':
    win = Tk()
    Adminpage(win)
    win.mainloop()