import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MaliyetHesaplayiciApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maliyet Hesaplayıcı")

        # Girdi alanları
        self.create_widgets()

    def create_widgets(self):
        # Alış maliyeti
        ttk.Label(self.root, text="Alış Maliyeti:").grid(row=0, column=0)
        self.alis_maliyeti_entry = ttk.Entry(self.root)
        self.alis_maliyeti_entry.grid(row=0, column=1)
        self.alis_maliyeti_entry.insert(0, "100")

        # Kargo ücreti
        ttk.Label(self.root, text="Kargo Ücreti:").grid(row=1, column=0)
        self.kargo_ucreti_entry = ttk.Entry(self.root)
        self.kargo_ucreti_entry.grid(row=1, column=1)
        self.kargo_ucreti_entry.insert(0, "15")

        # Komisyon oranı
        ttk.Label(self.root, text="Komisyon Oranı:").grid(row=2, column=0)
        self.komisyon_orani_entry = ttk.Entry(self.root)
        self.komisyon_orani_entry.grid(row=2, column=1)
        self.komisyon_orani_entry.insert(0, "0.03")

        # KDV oranı
        ttk.Label(self.root, text="KDV Oranı:").grid(row=3, column=0)
        self.kdv_orani_entry = ttk.Entry(self.root)
        self.kdv_orani_entry.grid(row=3, column=1)
        self.kdv_orani_entry.insert(0, "0.18")

        # Kar oranı
        ttk.Label(self.root, text="Kar Oranı:").grid(row=4, column=0)
        self.kar_orani_entry = ttk.Entry(self.root)
        self.kar_orani_entry.grid(row=4, column=1)
        self.kar_orani_entry.insert(0, "0.01")

        # Hesapla butonu
        self.hesapla_button = ttk.Button(self.root, text="Hesapla", command=self.hesapla)
        self.hesapla_button.grid(row=5, columnspan=2)

        # Grafik alanı
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=6, columnspan=2)

    def hesapla(self):
        alis_maliyeti = float(self.alis_maliyeti_entry.get())
        kargo_ucreti = float(self.kargo_ucreti_entry.get())
        komisyon_orani = float(self.komisyon_orani_entry.get())
        kdv_orani = float(self.kdv_orani_entry.get())
        kar_orani = float(self.kar_orani_entry.get())

        toplam_maliyet = alis_maliyeti + kargo_ucreti
        kar = toplam_maliyet * kar_orani
        komisyon_dahil_fiyat = (toplam_maliyet + kar) / (1 - komisyon_orani)
        kdv_dahil_fiyat = komisyon_dahil_fiyat * (1 + kdv_orani)
        komisyon = komisyon_dahil_fiyat * komisyon_orani
        kdv = komisyon_dahil_fiyat * kdv_orani

        maliyetler = [alis_maliyeti, kargo_ucreti, komisyon, kar, kdv]
        kategoriler = ['Alış Maliyeti', 'Kargo', 'Komisyon', 'Kar', 'KDV']
        colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700']

        self.ax.clear()
        self.ax.pie(maliyetler, labels=kategoriler, autopct='%1.1f%%', colors=colors, startangle=90)
        self.ax.axis('equal')
        self.ax.set_title(f'{alis_maliyeti} TL Maliyetli Ürün İçin Maliyet Dağılımı\nSatış Fiyatı: {kdv_dahil_fiyat:.2f} TL')
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = MaliyetHesaplayiciApp(root)
    root.mainloop()
