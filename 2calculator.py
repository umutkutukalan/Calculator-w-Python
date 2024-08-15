import tkinter as tk
from simpleeval import SimpleEval

degerlendirici = SimpleEval()
hesaplama = ""

def hesaplamayaEkle(symbol):
    global hesaplama
    hesaplama += str(symbol)
    label_result.delete(1.0, 'end')
    label_result.insert(1.0, hesaplama)

def hesaplamayıDegerlendir():
    global hesaplama
    try:
        result = degerlendirici.eval(hesaplama)
        hesaplama = str(result)
        label_result.delete(1.0, 'end')
        label_result.insert(1.0, hesaplama)
    except:
        alanıTemizle()
        label_result.insert(1.0, "Error")
def alanıTemizle():
    global hesaplama
    hesaplama = ''
    label_result.delete(1.0, 'end')

def disableKey(event):          #klavye olaylarını engeller
    return 'break'

# Root ( Temel-kök)
root = tk.Tk()
root.geometry("235x300")
root.title("Hesap Makinesi")

label_result = tk.Text(root, height=2, width=15, font=("Ariel", 24), bg='white', fg='black')
label_result.grid(columnspan=5)

label_result.bind("<Key>", disableKey) # klavye girişini engeller

#Buttons Numbers
btn_1 = tk.Button(root, text='1', command=lambda: hesaplamayaEkle(1), height= 2, width=2, font=('Ariel', 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text='2', command=lambda: hesaplamayaEkle(2), height= 2, width=2, font=('Ariel', 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text='3', command= lambda: hesaplamayaEkle(3),height= 2, width=2, font=('Arial', 14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text='4', command= lambda: hesaplamayaEkle(4),height= 2, width=2, font=('Arial', 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text='5', command= lambda: hesaplamayaEkle(5),height= 2, width=2, font=('Arial', 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text='6', command= lambda: hesaplamayaEkle(6),height= 2, width=2, font=('Arial', 14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text='7', command= lambda: hesaplamayaEkle(7),height= 2, width=2, font=('Arial', 14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text='8', command= lambda: hesaplamayaEkle(8),height= 2, width=2, font=('Arial', 14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text='9', command= lambda: hesaplamayaEkle(9),height= 2, width=2, font=('Arial', 14))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text='0', command= lambda: hesaplamayaEkle(0),height= 2, width=2, font=('Arial', 14))
btn_0.grid(row=5, column=2)

#Buttons Operators
btn_topla = tk.Button(root, text='+', command= lambda: hesaplamayaEkle("+"), height=2, width=2, font=('Ariel', 14))
btn_topla.grid(row=2, column=4)
btn_cıkar = tk.Button(root, text='-', command= lambda: hesaplamayaEkle("-"), height=2, width=2, font=('Ariel', 14))
btn_cıkar.grid(row=3, column=4)
btn_carp = tk.Button(root, text='*', command= lambda: hesaplamayaEkle("*"), height=2, width=2, font=('Ariel', 14))
btn_carp.grid(row=4, column=4)
btn_bol = tk.Button(root, text='/', command= lambda: hesaplamayaEkle("/"), height=2, width=2, font=('Ariel', 14))
btn_bol.grid(row=5, column=4)
btn_acma = tk.Button(root, text='(', command= lambda: hesaplamayaEkle("("), height=2, width=2, font=('Ariel', 14))
btn_acma.grid(row=5, column=1)
btn_kapama = tk.Button(root, text=')', command= lambda: hesaplamayaEkle(")"), height=2, width=2, font=('Ariel', 14))
btn_kapama.grid(row=5, column=3)

# Esittir - Temizle
btn_esittir = tk.Button(root, text='=', command=hesaplamayıDegerlendir, height=2, width=15, font=('Ariel', 14))
btn_esittir.grid(row=6, column=2, columnspan=3)
btn_temizle = tk.Button(root, text='C', command=alanıTemizle, height=2, width=2, font=('Ariel', 14))
btn_temizle.grid(row=6, column=1)

root.mainloop()