from tkinter import *
from PIL import Image, ImageTk
from customtkinter import CTkEntry, CTkButton, CTkImage, CTkLabel,CTkComboBox
from tkinter import messagebox
from tkcalendar import Calendar
from tkinter import ttk
import tiket
import psycopg2
from datetime import datetime
import loginpage

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

class DashboardPage:
    def __init__(self, dashboard_page):
        self.counter = IntVar(value=0)
        self.counter1 = IntVar(value=0)

        self.is_calendar_open = False



        self.dashboard_page = dashboard_page
        self.dashboard_page.title("Dashboard")
        self.dashboard_page.rowconfigure(0, weight=1)
        self.dashboard_page.columnconfigure(0, weight=1)


        # Fullscreen Mode
        self.dashboard_page.attributes('-fullscreen', False)

        # Atur ukuran sesuai layar
        self.height = 720
        self.width = 1280
        x = (self.dashboard_page.winfo_screenwidth() // 2) - (self.width // 2)
        y = (self.dashboard_page.winfo_screenheight() // 4) - (self.height // 4)
        self.dashboard_page.geometry('{}x{}+{}+{}'.format(self.width, self.height, x, y))
        self.dashboard_page.resizable(0, 0)

        # Muat gambar latar belakang
        self.bg_image = Image.open("images\\dashboardpage1.png")
        self.bg_image = self.bg_image.resize((1280,720))
        self.photobg = ImageTk.PhotoImage(self.bg_image)
        self.home = Label(self.dashboard_page,image=self.photobg)
        self.home.image =self.photobg
        self.home.place(x=0,y=0)# Ganti dengan path file gambar Anda

        conn = connect_db()
        c = conn.cursor()
        c.execute("SELECT username FROM pelanggan WHERE status=1")
        customer_data = c.fetchone()
        if customer_data is not None:
            customer_name = customer_data[0]
            label_name = Label(self.dashboard_page, text=f"Hai,selamat datang {customer_name}", font=("Poppins", 13), bg="white", fg='black')
            label_name.place(x=970, y=45)




        # Navigation Buttons
        self.home_button = Button(
            self.dashboard_page,
            text="Home",
            font=("Helvetica", 12),
            bg="#8E9775",
            fg="white",
            relief="flat",
            command=self.go_home
        )
        self.home_button.place(x=540, y=40) #776 , 63 = 206

        
        self.profile_button = Button(
            self.dashboard_page,
            text="Profile",
            font=("Helvetica", 12),
            bg="#8E9775",
            fg="white",
            relief="flat", width=8,
            command=self.go_profile
        )
        self.profile_button.place(x=750, y=40) #776 , 63
       

        self.riwayat = Button(
            self.dashboard_page,
            text="Transaction",
            font=("Helvetica", 12),
            bg="#8E9775",
            fg="white",
            relief="flat",
            width=8
        )
        self.riwayat.place(x=635, y=40) #776 , 63

        imglogout =CTkImage(Image.open('images\\exit1.png'), size=(50, 30))

        self.logout_button = CTkButton(
            self.dashboard_page,
            bg_color="white",
            fg_color="white",
            command=self.logout,
            image=imglogout,
            hover=False,
            text = "",
            width=80,height=40
        )
        self.logout_button.place(x=1202, y=40) #776 , 63
    


        # self.entry_berangkat = CTkEntry(self.dashboard_page, placeholder_text="        Enter Destination City/Port", width=200,
        #                            placeholder_text_color='#545454',
        #                            height=48,
        #                            corner_radius=10,
        #                            font=("Arial", 10),
        #                            bg_color="black",
        #                            fg_color="white",
        #                            text_color="black",
        #                            border_color="#C8FF53",
        #
        #
        #
        #                            )
        # self.entry_berangkat.place(x=170, y=320)

        self.serch_image = CTkImage(Image.open("images\\back.png"),
                                       size=(10, 10))

        def data_destinasi():
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("select tujuan from kapal")
            tujuan = [i[0] for i in cur.fetchall()]
            conn.commit()
            cur.close()
            conn.close()
            return tujuan

        def update_autocomplete(event):
            value = entry_var.get().lower()
            listbox.delete(0, END)  #

            if value:
                filtered_values = list({item for item in tujuan if value in item.lower()})
                for item in filtered_values:
                    listbox.insert(END, item)
                listbox.place(x=self.entry.winfo_x(), y=self.entry.winfo_y() + self.entry.winfo_height(), width=self.entry.winfo_width())
                self.minus_button.place_forget()
                self.counter_label.place_forget()
                self.plus_button.place_forget()
            else:
                listbox.place_forget()
                self.minus_button.place(x=150, y=480)
                self.counter_label.place(x=195, y=485)
                self.plus_button.place(x=225, y=480)

        def on_listbox_select(event):
            selection = listbox.get(listbox.curselection())
            entry_var.set(selection)
            listbox.place_forget()
            self.minus_button.place(x=150, y=480)
            self.counter_label.place(x=195, y=485)
            self.plus_button.place(x=225, y=480)

        tujuan = data_destinasi()
        entry_var =StringVar()
        self.entry =CTkEntry(self.dashboard_page, textvariable=entry_var,width=200,
                                   height=48,
                                   corner_radius=10,
                                   font=("Arial", 20),
                                   bg_color="black",
                                   fg_color="white",
                                   text_color="black",
                                   border_color="#C8FF53",)
        self.entry.place(x=70, y=298)
        listbox = Listbox(self.dashboard_page)
        self.entry.bind("<KeyRelease>", update_autocomplete)
        listbox.bind("<<ListboxSelect>>", on_listbox_select)

        # self.button_searchbrgkt = CTkEntry(self.dashboard_page, image=self.serch_image,
        #                                     text='', bg_color='white',
        #                                     fg_color="white",
        #                                     width=30,
        #                                     hover_color="#545454")
        # self.button_searchbrgkt.place(x=172, y=328)

        # self.btn_switch = CTkButton(self.dashboard_page, text="↔", command=self.switch_route,width=40, height = 48,bg_color='black',fg_color='#C8FF53',text_color='black',hover_color='grey')
        # self.btn_switch.place(x=400,y=320)

        # self.entry_tujuan= CTkEntry(self.dashboard_page, placeholder_text="        Enter Destination City/Port", width=200,
        #                            placeholder_text_color='#545454',
        #                            height=48,
        #                            corner_radius=10,
        #                            font=("Arial", 10),
        #                            bg_color="black",
        #                            fg_color="white",
        #                            text_color="black",
        #                            border_color="#C8FF53",
        #
        #
        #
        #                            )
        # self.entry_tujuan.place(x=475, y=320)


        self.entrydatedash = CTkEntry(
            self.dashboard_page,
            placeholder_text="        Select Date",
            width=250,  # Panjang Entry
            placeholder_text_color='#545454',
            height=48,
            corner_radius=10,
            font=("Arial", 10),
            bg_color="black",
            fg_color="white",
            text_color="black",
            border_color="#C8FF53",
        )
        self.entrydatedash.place(x=380, y=298)

        self.entrydatedash.bind("<Button-1>", self.munculkalender)
        self.calendar_frame = Frame(self.dashboard_page, bg="white", highlightbackground="black", highlightthickness=1)
        self.calendar = Calendar(self.calendar_frame, date_pattern="yyyy-mm-dd")
        self.calendar.pack()
        self.select_button = CTkButton(
            self.calendar_frame, text="Pilih", command=self.select_date, width=50, height=30, fg_color='#C8FF53', text_color="black"
        )
        self.select_button.pack(pady=5)



        self.minus_button = CTkButton(self.dashboard_page, text="-", width=35, height=35, command=lambda: self.decrement(0), font=("Arial", 20),corner_radius=40,fg_color='#C8FF53',text_color='black',bg_color='black')
        self.minus_button.place(x=150,y=480)
        self.counter_label = CTkLabel(self.dashboard_page, textvariable=self.counter, font=("Arial", 16),wraplength=100,corner_radius=10,bg_color='black',text_color='white')
        self.counter_label.place(x=195,y=485)
        self.plus_button = CTkButton(self.dashboard_page, text="+", width=35, height=35, command=lambda: self.increment(0), font=("Arial", 16), corner_radius=40,fg_color='#C8FF53',text_color='black',bg_color='black')
        self.plus_button.place(x=225,y=480)


        self.minus_button1 = CTkButton(self.dashboard_page, text="-", width=35, height=35, command=lambda: self.decrement(1), font=("Arial", 20),corner_radius=40,fg_color='#C8FF53',text_color='black',bg_color='black')
        self.minus_button1.place(x=465,y=480)
        self.counter_label1 = CTkLabel(self.dashboard_page, textvariable=self.counter1, font=("Arial", 16),wraplength=100,corner_radius=10,bg_color='black',text_color='white')
        self.counter_label1.place(x=505,y=485)
        self.plus_button1 = CTkButton(self.dashboard_page, text="+", width=35, height=35, command=lambda: self.increment(1), font=("Arial", 16), corner_radius=40,fg_color='#C8FF53',text_color='black',bg_color='black')
        self.plus_button1.place(x=530,y=480)


        
        self.findmyticket = CTkButton(self.dashboard_page, text="Find My Ticket", command=self.tiket,width=100, height = 48,bg_color='black',fg_color='#C8FF53',text_color='black',hover_color='grey', corner_radius=10)
        self.findmyticket.place(x=270,y=580)
        def show_sch_board():
            try:
                conn = connect_db()
                cur = conn.cursor()
                query ="""
                    SELECT s.id_schedule,s.day, s.dep_time, k.nama_kapal,k.tujuan, kk.jenis_kelas
                    FROM schedule s
                    JOIN kapal k ON s.id_kapal = k.id_kapal
                    JOIN kelas kk ON s.id_kelas = kk.id_kelas
                """
                cur.execute(query)
                rows = cur.fetchall()

                if len(rows) != 0 :
                    self.tree.delete(*self.tree.get_children())
                    for row in rows :
                        self.tree.insert('','end',values=row)
                conn.commit()
                cur.close()
                conn.close()
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")

        columns = ["No.","Day", "Time", "Ship", "Destination", "Class"]
        tree_frame = Frame(self.dashboard_page, width=140, height=120)
        tree_frame.place(x=680, y=190)
        scrollbar_y = Scrollbar(tree_frame, orient="vertical")
        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x = Scrollbar(tree_frame, orient="horizontal")
        scrollbar_x.pack(side="bottom", fill="x")

        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=10,
                                 yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        self.tree.pack(fill="both", expand=True,ipady=10)

        scrollbar_y.config(command=self.tree.yview)
        scrollbar_x.config(command=self.tree.xview)

        # Gaya untuk Treeview dalam Dark Mode
        style = ttk.Style(self.tree)
        style.theme_use("clam")

        # Warna Header (Dark Mode)
        style.configure(
            "Treeview.Heading",
            background="#333333",  # Header warna abu-abu gelap
            foreground="#CFFF53",  # Teks header hijau neon
            font=("Arial", 11, "bold")
        )

        # Warna Baris Tabel (Dark Mode)
        style.configure(
            "Treeview",
            rowheight=30,
            fieldbackground="#1E1E1E",  # Latar belakang tabel abu-abu gelap
            background="#1E1E1E",  # Latar belakang default
            foreground="#E6E6E6",  # Warna teks abu-abu terang
            font=("Arial", 10)
        )
        style.map(
            "Treeview",
            background=[("selected", "#87CEEB")],  # Highlight biru muda untuk baris yang dipilih
            foreground=[("selected", "#000000")]  # Teks hitam untuk baris yang dipilih
        )

        # Tata letak Treeview
        style.layout(
            "Treeview",
            [("Treeview.treearea", {"sticky": "nswe"})]
        )

        # Pola abu-abu untuk baris bergaris (striped rows)
        self.tree.tag_configure('evenrow', background="#2E2E2E")  # Abu-abu gelap untuk baris genap
        self.tree.tag_configure('oddrow', background="#1E1E1E")  # Lebih gelap untuk baris ganjil

        # Tambahkan Header dan Kolom
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=100, stretch=YES)

        show_sch_board()
    def open_ticket(self):
        win = Toplevel()
        tiket.TicketBookingApp(win)
        self.dashboard_page.withdraw()
        win.deiconify()


    def munculkalender(self, event=None):

        # Fungsi untuk membuka/menutup kalender
            if not self.is_calendar_open:
                self.calendar_frame.place(x=170, y=460)
                  # Posisi tepat di bawah Entry
                self.calendar_frame.lift()
                self.calendar_frame.config(width=200)  # Panjang Frame sesuai Entry
                self.is_calendar_open = True
            else:
                self.calendar_frame.place_forget()
                self.is_calendar_open = False

    def select_date(self):
            # Fungsi untuk memilih tanggal dan menutup kalender
            selected_date = self.calendar.get_date()
            self.entrydatedash.delete(0, END)
            self.entrydatedash.insert(0, selected_date)
            self.calendar_frame.place_forget()
            self.is_calendar_open = False

    def increment(self, p):
        if p == 0:
            self.counter.set(self.counter.get() + 1)  # Menambah nilai counter
        else: 
            self.counter1.set(self.counter1.get() + 1)  # Menambah nilai counter1

    # Fungsi untuk mengurangi nilai counter
    def decrement(self, p):
        if p == 0:  # Jika p adalah 0, kurangi counter
            if self.counter.get() > 0:  # Pastikan nilai counter tidak negatif
                self.counter.set(self.counter.get() - 1)
        else:  # Jika p bukan 0, kurangi counter1
            if self.counter1.get() > 0:  # Pastikan nilai counter1 tidak negatif
                self.counter1.set(self.counter1.get() - 1)

    def go_home(self):
        messagebox.showinfo("Navigation", "Home button clicked!")

    def go_profile(self):
        messagebox.showinfo("Navigation", "Profile button clicked!")

    def logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure:
            connection = connect_db()
            cursor = connection.cursor()
            cursor.execute("UPDATE pelanggan SET status = 0 WHERE status = 1")
            connection.commit()
            connection.close()
            self.dashboard_page.destroy()
            win = Toplevel()
            loginpage.LoginPage(win)
            win.deiconify()

    def get_rute(self):
        conn = connect_db()
        cur = conn.cursor()

        self.tujuan = self.entry.get()
        date = self.entrydatedash.get()
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        self.day_name = date_obj.strftime("%A")

        find_rute = "SELECT id_kapal FROM kapal WHERE tujuan = %s"
        cur.execute(find_rute, (self.tujuan,))
        kapal_ids = cur.fetchall()

        if not kapal_ids:
            print("Tidak ada kapal yang ditemukan untuk tujuan ini.")
            return

        sch = []
        find_schedule = "SELECT * FROM schedule WHERE id_kapal = %s and day=%s"
        for kapal_id in kapal_ids:
            cur.execute(find_schedule, (kapal_id[0], self.day_name))
            sch.extend(cur.fetchall())

        if not sch:
            messagebox.showinfo("Tidak ada jadwal ditemukan.", parent=self.tiketpage)
        else:
            y_offset = 270
            for schedule in sch:
                frame1 = Frame(self.tiketpage, background='white', width=800,height=200)
                frame1.place(x=200, y=y_offset)

                frame1.pack_propagate(False)

                id_kapal = schedule[4]
                dep_time = schedule[2]
                arr_time = schedule[3]
                get_nama_kapal = "SELECT nama_kapal, kapasitas FROM kapal WHERE id_kapal = %s"
                cur.execute(get_nama_kapal, (str(id_kapal),))
                result = cur.fetchone()
                nama_kapal = result[0]
                kapasitas = result[1]

                # Menampilkan informasi dalam frame (bisa menambahkan label atau elemen lainnya)
                label_kapasitas = Label(frame1, text=f"Kuota tersedia: {kapasitas}", font=('Poppins', 8),background='white')
                label_kapasitas.pack(side='top',pady=5,anchor='w')

                label_nama_kapal = Label(frame1, text=nama_kapal, font=('Poppins', 14),background='white')
                label_nama_kapal.pack(side='top',pady=5,anchor='w')

                label_waktu = Label(frame1, text=f"{dep_time} - {arr_time} WIB",
                                    font=('Poppins', 12),background='white')
                label_waktu.pack(side='top',pady=20,anchor='w')

                button_pesan_tiket = Button(frame1, text="Pesan Tiket",
                                            bg='white', fg='black')
                button_pesan_tiket.pack(side='bottom',pady=20,anchor='e',ipadx=10,padx=10)

                y_offset += 230

            print(sch)

        cur.close()
        conn.close()

    def exit_fullscreen(self):
        self.dashboard_page.attributes('-fullscreen', False)

    def tiket(self):
        self.dashboard_page.withdraw()
        self.tiketpage = Toplevel(self.dashboard_page)
        self.tiketpage.resizable(False, False)
        self.tiketpage.rowconfigure(0, weight=1)
        self.tiketpage.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (self.tiketpage.winfo_screenwidth() // 2) - (width // 2)
        y = (self.tiketpage.winfo_screenheight() // 4) - (height // 4)
        self.tiketpage.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.image2 = Image.open("images\\tiket.png")
        self.image2 = self.image2.resize((1280, 720))
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.canvas1 = Canvas(self.tiketpage, width=1366, height=768, bg="#C70039")
        self.canvas1.pack()
        self.canvas1.create_image(0, 0, anchor='nw', image=self.photo2)

        tujuan = Label(self.tiketpage,text=self.entry.get(),font=('Poppins',15),fg='black',bg='white')
        tujuan.place(x=180,y=128)

        date = self.entrydatedash.get()
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        day_name = date_obj.strftime("%A")

        formatted_date = date_obj.strftime("%d %B %Y")
        tanggal = Label(self.tiketpage,text=f"{day_name}, {formatted_date}",font=('Poppins',10),fg='black',bg='white')
        tanggal.place(x=40, y=171)

        penumpang = Label(self.tiketpage,text=f"{self.counter.get()+self.counter1.get()} Penumpang",font=('Poppins',10),fg='black',bg='white')
        penumpang.place(x=40,y=200)
        self.get_rute()










    

if __name__ == "__main__":
    root = Tk()
    DashboardPage(root)
    root.mainloop()