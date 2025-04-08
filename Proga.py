from tkinter import messagebox
from tkinter import *
from tkinter import Tk, Toplevel, Button, Label, Entry, messagebox
import pickle
from tkinter.font import names


def add_name():
    top = Toplevel(window)
    top.title("Добавить новое имя и фамилию")
    label_name = Label(top, text='Имя:')
    label_name.pack()
    entry_name = Entry(top)
    entry_name.pack()

    label_surname = Label(top, text='Фамилия:')
    label_surname.pack()
    entry_surname = Entry(top)
    entry_surname.pack()

    def submit():
        name = entry_name.get()
        surname = entry_surname.get()
        if name and surname:
            full_name = f"{name} {surname}"
            station_list.insert(END, full_name)  # Добавляем в первый список
            station_list1.insert(END, f"Имя: {name}, Фамилия: {surname}")  # Добавляем в общий список
            top.destroy()
        else:
            messagebox.showwarning("Ошибка", "Пожалуйста, введите имя и фамилию.")

    btn_submit = Button(top, text='Добавить', command=submit)
    btn_submit.pack()
    button_top_level = Button(top, text='Закрыть', command=top.destroy)
    button_top_level.pack()

    top.transient(window)
    top.grab_set()
    top.focus_set()
    top.wait_window()

def func():
    top = Toplevel(window)
    top.title = ("Добавить новую строку")

    label = Label(top, text='Уверены, что хотите добавить новую строку?')
    label.pack()
    button_top_level = Button(top, text='Да', command=add_name)
    button_top_level.pack()
    top.transient(window)
    top.grab_set()
    top.focus_set()
    top.wait_window()


def edit_func():
    top = Toplevel(window)
    label = Label(top, text='Текст из модального окна Edit...')
    label.pack()
    button_top_level = Button(top, text='Закрыть', command=top.destroy)
    button_top_level.pack()
    top.transient(window)
    top.grab_set()
    top.focus_set()
    top.wait_window()

def delete_func():
    selected_indices = station_list.curselection()
    if not selected_indices:
        messagebox.showwarning("Ошибка", "Пожалуйста, выберите имя для удаления.")
    return

    for index in selected_indices[::-1]:
        station_list.delete(index)
    station_list1.delete(index)


window = Tk()
window.title( 'AddressApp' )
window.resizable(0,0)
station_list = Listbox(window, width = 50)
station_list.grid(row=0, column=0, columnspan = 1,
                  padx=0)
#Список доп инфы
station_list1 = Listbox(window, width = 50)
station_list1.grid(row=0, column=3, columnspan = 1,
                  padx=0)
entry = Entry(window, width=50, borderwidth=5)


#Создаем меню в главном окне
mainmenu = Menu(window)
window.config(menu=mainmenu)
#Создаем пункты подменю для пункта меню "Файл"
filemenu = Menu(mainmenu, tearoff=0) #Создаем еще один объект Menu
filemenu.add_command(label="Открыть...")
#Добавляем в него пункты меню
filemenu.add_separator()#Добавляем линиюразделитель
filemenu.add_command(label="Новый")
filemenu.add_separator()#Добавляем линиюразделитель
filemenu.add_command(label="Сохранить...")
filemenu.add_separator()#Добавляем линиюразделитель
filemenu.add_command(label="Выход")
#Создаем пункт подменю "Помощь" для пункта меню
"Справка"
helpmenu = Menu(mainmenu, tearoff=0) #Создаем еще один объект Menu
#Добавляем еще один уровень меню к пункту подменю
"Помощь"
helpmenu1 = Menu(helpmenu, tearoff=0)
helpmenu1.add_command(label="Локальная справка")
helpmenu1.add_separator()#Добавляем линию разделитель
helpmenu1.add_command(label="На сайте")
#Связываем два созданных пункта меню с пунктом подменю "Помощь"
helpmenu.add_cascade(label="Help",
                     menu=helpmenu1)
helpmenu.add_separator()#Добавляем линию разделитель
#Создаем пункт подменю "О программе" для пункта меню "Справка"
helpmenu.add_command(label="О программе")
#Связываем два созданных меню с главным меню

statmenu = Menu(mainmenu, tearoff=0) #Создаем еще один объект Menu
statmenu.add_command(label="Просмотреть справку")
#Добавляем в него пункты меню
statmenu.add_separator()#Добавляем линиюразделитель
statmenu.add_command(label="Отправить отзыв")
statmenu.add_separator()#Добавляем линиюразделитель
statmenu.add_command(label="О программе")

mainmenu.add_cascade(label="File", menu=filemenu)
mainmenu.add_cascade(label="Statistics",
                     menu=statmenu)
mainmenu.add_cascade(label="Help",
                     menu=helpmenu)


#Размещаем в ячейке (1,4) метку с текстом
btn_1 = Button(window, text = "Delete", bg = "black", width = 20, fg = "white", height=2, command=func)
btn_1.grid(row=2, column=0, sticky=S, pady=30,
           padx=10)
#Размещаем в ячейке (2,2) кнопку
btn_2 = Button(window, text = "Edit...", bg =
"black", width = 20, fg = "white", height=2, command=func)
btn_2.grid(row=2, column=2, sticky=S, pady=30,
           padx=10)
#Размещаем в ячейке (2,4) кнопку
btn_3 = Button(window, text = "New...", bg = "black",
               width = 20, fg = "white", height=2, command=func)
btn_3.grid(row=2, column=4, sticky=S, pady=30,
           padx=10)


window.mainloop()