import sqlite3
import tkinter as tk
from  tkinter import messagebox

root = tk.Tk()
root.title("Kontakt")
root.geometry("350x300")
connection = sqlite3.connect('kontakti.db')
cursor = connection.cursor()#obavlja executeee
# autoincrement sluzi da se primarni kljuc sam dodaje( vjr jer ga ne ubacujemo)
cursor.execute('''CREATE TABLE IF NOT EXISTS kontakti(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ime TEXT,
                prezime TEXT,
                broj TEXT
) ''')

def dodaj_kontakt():
    connection = sqlite3.connect('kontakti.db')
    cursor = connection.cursor()
    ime = entryIme.get()
    prezime = entryPrezime.get()
    broj = entryBroj.get()
    if ime and prezime and broj:
        cursor.execute("INSERT INTO kontakti(ime, prezime,broj) VALUES (?,?,?)", (ime, prezime, broj))
        connection.commit()
        entryIme.delete(0, tk.END)
        entryPrezime.delete(0, tk.END)
        entryBroj.delete(0, tk.END)
        messagebox.showinfo("Uspjeh", "Dodali ste novi kontakt!")
    else:
        messagebox.showerror("Greška", "Unesite sve podatke.")
def pregledaj_kontakte():
    connection = sqlite3.connect('kontakti.db')
    cursor = connection.cursor()
    pregledProzor = tk.Toplevel(root)
    pregledProzor.title("Svi kontakti")

    listaKon = tk.Listbox(pregledProzor)
    listaKon.pack(padx=10, pady=10)
    cursor.execute("SELECT * FROM kontakti")
    kontakti = cursor.fetchall()
    for kontakt in kontakti:
        listaKon.insert(tk.END, f"{kontakt[1]} {kontakt[2]} --> {kontakt[3]}")#pretpostavljam kao kontakt[broj] predstavljaju redom ime prezime broj
    btnZatvoriPregled = tk.Button(pregledProzor, text="Zatvori", command=pregledProzor.destroy)# samo ga ovdje stvaramo, ne treba doli jer bi onda morali definirati novi prozor u koji ga treba spremiti
    btnZatvoriPregled.pack(padx=10, pady=10)# samo se stvara u ovoj funkciji u ovom prozoru
    def obrisi_kontakte():
        connection = sqlite3.connect('kontakti.db')
        cursor = connection.cursor()
        izabraniKontakt = listaKon.curselection()
        if izabraniKontakt:
            #indeks_izabranog = izabraniKontakt[0]#izabrani kontakt je oblika ntorke npr. (1,)
            kontakt_zaBrisanje = kontakti[izabraniKontakt[0]]
            cursor.execute("DELETE FROM kontakti WHERE ID=?", (kontakt_zaBrisanje[0],))
            listaKon.delete(izabraniKontakt)
            connection.commit()
            novikontakti = cursor.fetchall()
            return novikontakti
    btnBrisi = tk.Button(pregledProzor, text="Obrisi kontakt", command= obrisi_kontakte)
    btnBrisi.pack(padx=10,pady=10)

#GUI
lblIme = tk.Label(root, text="Ime")
lblIme.grid(row = 0, column=0, padx=10, pady=10)
entryIme = tk.Entry(root)
entryIme.grid(row=0,column=1, padx=10,pady=10)

lblPrezime = tk.Label(root, text="Prezime")
lblPrezime.grid(row = 1, column=0, padx=10, pady=10)
entryPrezime = tk.Entry(root)
entryPrezime.grid(row=1,column=1, padx=10,pady=10)

lblBroj = tk.Label(root, text="Broj telefona")
lblBroj.grid(row = 2, column=0, padx=10, pady=10)
entryBroj = tk.Entry(root)
entryBroj.grid(row=2,column=1, padx=10,pady=10)

btnDodaj = tk.Button(root, text="Dodaj kontakt", command=dodaj_kontakt)
btnDodaj.grid(row=3, column=0, padx=10, pady=10)

btnPregled = tk.Button(root, text="Pregledaj kontakte", command=pregledaj_kontakte)
btnPregled.grid(row=4, column=0, padx=10, pady=10)

connection.close()
root.mainloop()