import customtkinter as ctk
from tkinter import *

# Inisialisasi aplikasi
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class TicketBookingApp:
    def __init__(self, ticketpage):
        self.ticketpage = ticketpage
        self.ticketpage.title("Tiket Kapal - Seaventures")
        self.ticketpage.attributes('-fullscreen', True)

        # Atur ukuran sesuai layar
        self.height = self.ticketpage.winfo_screenheight()
        self.width = self.ticketpage.winfo_screenwidth()

        # Muat gambar latar belakang
        self.bg_image1 = PhotoImage(file="tiketdash.png")  # Ganti dengan path file gambar Anda

        # Canvas untuk latar belakang
        self.canvas = Canvas(self.ticketpage, width=self.width, height=self.height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image1)

        # Header
        self.header = ctk.CTkLabel(self.canvas, text="Booking Ticket", 
                                   font=("Arial", 20, "bold"), text_color="white", bg_color='#1C1827')
        self.header.place(x=self.width // 2 - 150, y=50)

        # Scrollable Frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self.canvas, width=700, height=500, fg_color="white")
        self.scrollable_frame.place(x=self.width // 2 - 350, y=275)

        # Menampilkan tiket
        self.create_tickets()

        # Bind tombol ESC untuk keluar dari aplikasi
        self.ticketpage.bind('<Escape>', self.exit_application)

    def create_tickets(self):
        # Contoh data tiket
        tickets = [
            {"from": "Surabaya", "to": "Makassar", 
             "airport_from": "Juanda Airport", 
             "airport_to": "Sultan Hasanuddin International Airport",
             "date": "16 June 2023, Fri", "seat": 238, "price": "Rp. 576.000", "capacity": 1000},
             
            {"from": "Jakarta", "to": "Medan", 
             "airport_from": "Soekarno-Hatta Airport", 
             "airport_to": "Kualanamu International Airport",
             "date": "17 June 2023, Sat", "seat": 120, "price": "Rp. 850.000", "capacity": 1200},
             
            {"from": "Bali", "to": "Lombok", 
             "airport_from": "Ngurah Rai Airport", 
             "airport_to": "Zainuddin Abdul Madjid International Airport",
             "date": "18 June 2023, Sun", "seat": 50, "price": "Rp. 450.000", "capacity": 800},
        ]


        for ticket in tickets:
            self.add_ticket_card(ticket)

    def add_ticket_card(self, ticket):
        # Frame untuk tiket dengan padding dan border lebih besar
        ticket_frame = ctk.CTkFrame(self.scrollable_frame, corner_radius=10, fg_color="#f8f8f8", 
                                    border_color="#d1d1d1", border_width=2)
        ticket_frame.pack(pady=15, padx=15, fill="x")

        # Grid layout dengan lebih banyak spacing antar elemen
        from_label = ctk.CTkLabel(ticket_frame, text=ticket['from'], 
                                  font=("Arial", 16, "bold"), text_color="#333")
        from_label.grid(row=0, column=0, padx=15, pady=10, sticky="w")
        
        from_airport_label = ctk.CTkLabel(ticket_frame, text=ticket['airport_from'], 
                                          font=("Arial", 12), text_color="#666", width=50)  # Batasi lebar
        from_airport_label.grid(row=1, column=0, padx=15, pady=0, sticky="w")

        arrow_label = ctk.CTkLabel(ticket_frame, text="➜", font=("Arial", 16, "bold"), text_color="#4CAF50")
        arrow_label.grid(row=0, column=1, rowspan=2, padx=25)

        to_label = ctk.CTkLabel(ticket_frame, text=ticket['to'], 
                                font=("Arial", 16, "bold"), text_color="#333")
        to_label.grid(row=0, column=2, padx=15, pady=10, sticky="w")
        
        to_airport_label = ctk.CTkLabel(ticket_frame, text=ticket['airport_to'], 
                                        font=("Arial", 12), text_color="#666", width=200)  # Batasi lebar
        to_airport_label.grid(row=1, column=2, padx=15, pady=0, sticky="w")

        # Harga di pojok kanan bawah dengan lebih banyak padding
        capacity_label = ctk.CTkLabel(ticket_frame, text=f"Alvailable Capacity: {ticket['capacity']} seats", 
                                      font=("Arial", 12, 'bold'), text_color="#333")
        capacity_label.grid(row=2, column=0, padx=15, pady=10, sticky="w")

        price_label = ctk.CTkLabel(ticket_frame, text=f"{ticket['price']}", 
                                   font=("Arial", 14, "bold"), text_color="red")
        price_label.place(x=500,y=100)

        # Tombol Pesan di pojok kanan bawah
        book_button = ctk.CTkButton(ticket_frame, text="Book Ticket", fg_color="#4CAF50", 
                                    hover_color="#45a049", text_color="white", width=150)
        book_button.place(x=500, y = 130)

        # Tanggal di bawah kiri
        date_label = ctk.CTkLabel(ticket_frame, text=f"Date: {ticket['date']}", 
                                  font=("Arial", 12), text_color="#333")
        date_label.grid(row=3, column=0, padx=15, pady=15, sticky="sw")

    def exit_application(self, event=None):
        """Fungsi untuk keluar dari aplikasi ketika tombol ESC ditekan."""
        self.ticketpage.quit()

if __name__ == "__main__":
    ticket = Tk()
    app = TicketBookingApp(ticket)
    ticket.mainloop()
