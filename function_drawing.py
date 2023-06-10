from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import re


def rysuj():
    okno = Tk()
    okno.configure(background='pink')
    okno.geometry("1400x800")

    font = tkFont.Font(family='Arial Hebrew', size=16)

    Label(okno, text="Wzory funkcji (należy oddzielić je używając ' ; '):", bg='pink', font=font).place(x=20, y=22)
    wzory_tekst = StringVar(okno, value='(1/4)*cos(x); e^x; -x')
    wzory = Entry(okno, textvariable=wzory_tekst, font=font, width=35)
    wzory.place(x=20, y=50)

    def wyczysc():
        wzory.delete(0, END)

    def klikniecie(sign):
        wzory.insert(tk.INSERT, str(sign))

    Button(okno, text="Wyczyść", command=wyczysc, font=font, bg="indian red").place(x=475, y=40)
    
    Button(okno, text="+", command=lambda: klikniecie('+'), height=4,width=8).place(x=20, y=100)
    Button(okno, text='-', command=lambda: klikniecie('-'), height=4,width=8).place(x=90, y=100)
    Button(okno, text='*', command=lambda: klikniecie('*'), height=4, width=8).place(x=160, y=100)
    Button(okno, text='/', command=lambda: klikniecie('/'), height=4, width=8).place(x=230, y=100)
    Button(okno, text='(', command=lambda: klikniecie('('), height=4, width=8).place(x=300, y=100)
    Button(okno, text=')', command=lambda: klikniecie(')'), height=4, width=8).place(x=370, y=100)
    Button(okno, text='^', command=lambda: klikniecie('^'), height=4, width=8).place(x=440, y=100)
    Button(okno, text='abs', command=lambda: klikniecie('abs'), height=4, width=8).place(x=20, y=175)
    Button(okno, text='sqrt', command=lambda: klikniecie('sqrt'), height=4, width=8).place(x=90, y=175)
    Button(okno, text='π', command=lambda: klikniecie('π'), height=4, width=8).place(x=160, y=175)
    Button(okno, text='e', command=lambda: klikniecie('e'), height=4, width=8).place(x=230, y=175)
    Button(okno, text='x', command=lambda: klikniecie('x'), height=4, width=8).place(x=300, y=175)
    Button(okno, text='ln', command=lambda: klikniecie('ln'), height=4, width=8).place(x=370, y=175)  
    Button(okno, text='log10', command=lambda: klikniecie('log10'), height=4, width=8).place(x=440, y=175)  
    Button(okno, text='sin', command=lambda: klikniecie('sin'), height=4, width=8).place(x=20, y=250)
    Button(okno, text='cos', command=lambda: klikniecie('cos'), height=4, width=8).place(x=90, y=250)
    Button(okno, text='tan', command=lambda: klikniecie('tan'), height=4, width=8).place(x=160, y=250)
    Button(okno, text='cot', command=lambda: klikniecie('cot'), height=4, width=8).place(x=230, y=250)
    Button(okno, text='arcsin', command=lambda: klikniecie('arcsin'), height=4, width=8).place(x=300, y=250)
    Button(okno, text='arccos', command=lambda: klikniecie('arccos'), height=4, width=8).place(x=370, y=250)
    Button(okno, text='arctan', command=lambda: klikniecie('arctan'), height=4, width=8).place(x=440, y=250)

    Label(okno, text="Tytuł Wykresu:", bg='pink', font=font).place(x=100,y=350)
    tytul_tekst = StringVar(okno, value="Wykres Prezentacyjny")
    tytul = Entry(okno, textvariable=tytul_tekst, font=font)
    tytul.place(x=100,y=380)

    Label(okno, text="Tytuł osi OX:", bg='pink', font=font).place(x=100,y=430)
    xt = StringVar(okno, value='Tytuł_OX')
    x_tytul = Entry(okno, textvariable=xt, font=font)
    x_tytul.place(x=100,y=460)

    Label(okno, text="Tytuł osi OY:", bg='pink', font=font).place(x=100,y=510)
    yt = StringVar(okno, value='Tytuł_OY')
    y_tytul = Entry(okno, textvariable=yt, font=font)
    y_tytul.place(x=100,y=540)

    Label(okno, text="Zakres osi OX:", bg='pink', font=font).place(x=100,y=590)
    Label(okno, text="Od:", bg='pink', font=font).place(x=60,y=620)
    Label(okno, text="Do:", bg='pink', font=font).place(x=200,y=620)
    xr = StringVar(okno, value='-20')
    x_zakres = Entry(okno, textvariable=xr, font=font, width=8)
    x_zakres.place(x=100, y=620)
    xr_2 = StringVar(okno, value='20')
    x_zakres_2 = Entry(okno, textvariable=xr_2, font=font, width=8)
    x_zakres_2.place(x=240, y=620)

    Label(okno, text="Zakres osi OY:", bg='pink', font=font).place(x=100,y=670)
    Label(okno, text="Od:", bg='pink', font=font).place(x=60,y=700)
    Label(okno, text="Do:", bg='pink', font=font).place(x=200,y=700)
    yr = StringVar(okno, value='-10')
    y_zakres = Entry(okno, textvariable=yr, font=font, width=8)
    y_zakres.place(x=100, y=700)
    yr_2 = StringVar(okno, value='10')
    y_zakres_2 = Entry(okno, textvariable=yr_2, font=font, width=8)
    y_zakres_2.place(x=240, y=700)

    legenda = IntVar(value=True)

    def check_if_okay():
        try:
            float(x_zakres.get())
            float(x_zakres_2.get())
            float(y_zakres.get())
            float(y_zakres.get())
            return True
        except:
            return False

    def wykres():
        if len(wzory.get()) == 0 or len(x_zakres.get()) == 0 or len(y_zakres.get()) == 0:
            messagebox.showinfo("Error", "Podaj zakres osi OX i OY")
        elif ',' in wzory.get():
            messagebox.showinfo("Error", "Zamiast przecinka użyj średnika")
        elif check_if_okay() == False:
            messagebox.showinfo("Error", "Błedny zakres osi OX lub OY")
        else:
            try:
                x = np.linspace(eval(x_zakres.get()), eval(x_zakres_2.get()))
                fig = Figure(figsize=(8, 8))
                ax = fig.add_subplot(1, 1, 1)
                ax.grid()
                ax.set_ylabel(y_tytul.get())
                ax.set_xlabel(x_tytul.get())
                ax.set_title(tytul.get())
                ax.set_ylim([eval(y_zakres.get()), eval(y_zakres_2.get())])
                for i in wzory.get().split(';'):
                    y = i
                    y = y.replace('^', '**')
                    y = re.sub(r'\bsin\b', "np.sin", y)
                    y = re.sub(r'\bcos\b', "np.cos", y)
                    y = re.sub(r'\btan\b', "np.tan",y)
                    y = re.sub(r'\bcot\b', "1/np.tan", y)
                    y = re.sub(r'\bln\b', "np.log", y)
                    y = re.sub(r'\be\b', "np.e", y)
                    y = re.sub(r'\bsqrt\b', "np.sqrt", y)
                    y = re.sub(r'\bπ\b', "np.pi", y)
                    y = re.sub(r'\blog10\b', "np.log10", y)
                    y = re.sub(r"\barcsin\b", "np.arcsin", y)
                    y = re.sub(r"\barccos\b", "np.arccos", y)
                    y = re.sub(r'\barctan\b', "np.arctan", y)
                    y = re.sub(r'\babs\b', "np.absolute", y)
                    ax.plot(x, eval(y), label=str(i))
                    canvas = FigureCanvasTkAgg(fig, okno)
                    canvas.draw()
                canvas.get_tk_widget().place(x=600, y=0)
                if legenda.get() == True:
                    ax.legend()
                else:
                    pass
            except:
                messagebox.showinfo("Error", "Błedny wzór")

    Checkbutton(okno, text="Legenda", variable=legenda, onvalue=1, offvalue=0, command=wykres(), bg='pink', font=font).place(x=420, y=450)

    draw_button = Button(okno, text="RYSUJ", command=lambda: wykres(), font=font, bg="lightblue")
    draw_button.place(x=430,y=400)
    exit_button = Button(okno, text="Wyjście", command=quit, fg='pink', bg='black')
    exit_button.place(x=0, y=775)
    okno.mainloop()


if __name__ == '__main__':
    rysuj()

