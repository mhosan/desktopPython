from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')

def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)

def add_item():
    if apellido.get() == '' or nombre.get() == '' or email.get() == '' or celular.get() == '':
        messagebox.showerror('Campos requeridos', 'Llenar todos los datos')
        return
    db.insert(apellido.get(), nombre.get(), email.get(), celular.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (apellido.get(), nombre.get(), email.get(), celular.get()))
    clear_text()
    populate_list()

def select_item(event):
    global selected_item
    index = parts_list.curselection()[0]
    selected_item = parts_list.get(index)
    
    apellido_entry.delete(0, END)
    apellido_entry.insert(END, selected_item[1])
    nombre_entry.delete(0, END)
    nombre_entry.insert(END, selected_item[2])
    email_entry.delete(0, END)
    email_entry.insert(END, selected_item[3])
    celular_entry.delete(0, END)
    celular_entry.insert(END, selected_item[4])


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_item():
    db.update(selected_item[0], apellido.get(), nombre.get(), email.get(), celular.get())
    populate_list()

def clear_text():
    apellido_entry.delete(0, END)
    nombre_entry.delete(0, END)
    email_entry.delete(0, END)
    celular_entry.delete(0, END)


app = Tk()

apellido = StringVar()
apellido_label = Label(app, text='Apellido', font=('bold',14), pady=20)
apellido_label.grid(row=0, column=0, sticky=W)
apellido_entry = Entry(app, textvariable=apellido)
apellido_entry.grid(row=0, column=1)

nombre = StringVar()
nombre_label = Label(app, text='Nombre', font=('bold',14))
nombre_label.grid(row=0, column=2, sticky=W)
nombre_entry = Entry(app, textvariable=nombre)
nombre_entry.grid(row=0, column=3)

email = StringVar()
email_label = Label(app, text='email', font=('bold',14))
email_label.grid(row=1, column=0, sticky=W)
email_entry = Entry(app, textvariable=email)
email_entry.grid(row=1, column=1)

celular = StringVar()
celular_label = Label(app, text='Celular', font=('bold',14))
celular_label.grid(row=1, column=2, sticky=W)
celular_entry = Entry(app, textvariable=celular)
celular_entry.grid(row=1, column=3)

parts_list = Listbox(app, height=8, width=50, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

scrollbar=Scrollbar(app)
scrollbar.grid(row=3, column=3)

parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)
parts_list.bind('<<ListboxSelect>>', select_item)

add_btn=Button(app, text='Agregar contacto', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn=Button(app, text='Borrar contacto', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn=Button(app, text='Actualizar contacto', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn=Button(app, text='Limpiar datos', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)


app.title('Esta es la aplicación principal')
app.geometry('700x350')

populate_list()

app.mainloop()