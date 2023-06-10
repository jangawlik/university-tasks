import tkinter as tk
from tkinter import *
from tkinter import ttk
import requests

# Przelicznik walut
class Przelicz():
    def __init__(self, url):
            self.data = requests.get(url).json() 
            self.currencies = self.data['rates']

    def convert(self, waluty_1, waluty_2, ilosc): 
        if waluty_1 != 'USD':
            ilosc = ilosc / self.currencies[waluty_1] 
        # limitowanie precyzji do 4 cyfr
        ilosc = round(ilosc * self.currencies[waluty_2], 4) 
        return ilosc

class Grafika(tk.Tk):
    def __init__(self, przelicznik):
        tk.Tk.__init__(self)
        self.przelicznik_walut = przelicznik
        self.geometry("500x300")
        self.configure(bg="#d3aee7")

        # Opis
        self.tytuł = Label(self, text = 'Przelicznik walut',  fg = 'red', relief = tk.RAISED, justify = tk.CENTER,  borderwidth = 3)
        self.tytuł.config(font = ('Manrope',20,'bold'))
        self.data = Label(self, text = f"1 PLN = {self.przelicznik_walut.convert('PLN','USD',1)} USD \n Data : {self.przelicznik_walut.data['date']}", relief = tk.GROOVE, borderwidth = 2)
        self.tytuł.place(x = 140, y = 5)
        self.data.place(x = 195, y= 50)

        # Okno do wpisywania kwoty
        self.kwota = Entry(self, bd = 3, relief = tk.RIDGE, width = 22, justify = tk.CENTER, validate='key')
        self.przewalutowana_kwota = Label(self, text = '', fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 19, borderwidth = 3)

        # Lista rozwijająca się
        self.lista_walut_1 = StringVar(self)
        self.lista_walut_1.set("PLN")  
        self.lista_walut_2 = StringVar(self)
        self.lista_walut_2.set("USD")

        font = ("Manrope", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.waluty_1_lista_rozwijana = ttk.Combobox(self, textvariable=self.lista_walut_1, values=list(self.przelicznik_walut.currencies.keys()), font = font, state = 'readonly', width = 13, justify = tk.CENTER)
        self.waluty_2_lista_rozwijana = ttk.Combobox(self, textvariable=self.lista_walut_2, values=list(self.przelicznik_walut.currencies.keys()), font = font, state = 'readonly', width = 13, justify = tk.CENTER)

        # placing
        self.waluty_1_lista_rozwijana.place(x = 30, y= 120)
        self.kwota.place(x = 30, y = 150)
        self.waluty_2_lista_rozwijana.place(x = 340, y= 120)
        self.przewalutowana_kwota.place(x = 340, y = 150)
        
        # Przycisk do przeliczenia
        self.button = Button(self, text = "Przelicz", fg = "black", command = self.perform) 
        self.button.config(font=font)
        self.button.place(x = 215, y = 135)

    def perform(self):
        ilosc = float(self.kwota.get())
        z_waluta = self.lista_walut_1.get()
        do_waluta = self.lista_walut_2.get()
        przeliczona_kwota = self.przelicznik_walut.convert(z_waluta,do_waluta,ilosc)
        przeliczona_kwota = round(przeliczona_kwota, 2)
        self.przewalutowana_kwota.config(text = str(przeliczona_kwota))
    

if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    przelicznik = Przelicz(url)
    Grafika(przelicznik)
    mainloop()

    