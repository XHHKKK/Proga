import os
from tkinter import *
from tkinter import messagebox

# Path to store names
DATA_FILE = "names.txt"

def load_names():
    # Load names from the file and insert them into the listboxes
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            for line in file:
                name, surname = line.strip().split(", ")
                full_name = f"{name} {surname}"
                station_list.insert(END, full_name)
                station_list1.insert(END, f"Имя: {name}, Фамилия: {surname}")


def save_names():
    # Save names to the file
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        for i in range(station_list.size()):
            full_name = station_list.get(i)
            file.write(full_name.replace(" ", ", ") + "\n")

def add_name():
    top = Toplevel(window)
    top.title("Добавить имя")

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
            station_list.insert(END, full_name)
            station_list1.insert(END, f"Имя: {name}, Фамилия: {surname}")
            save_names()  # Save names after adding
            top.destroy()
            update_additional_info()  # Обновляем дополнительную информацию после добавления
        else:
            messagebox.showwarning("Ошибка", "Пожалуйста, заполните все поля.")

    btn_submit = Button(top, text='Добавить', command=submit)
    btn_submit.pack()
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

    for index in selected_indices[::-1]:  # Убеждаемся, что удаляем с конца
        station_list.delete(index)
        station_list1.delete(index)
    save_names()  # Save names after deletion
    update_additional_info()  # Обновляем дополнительную информацию после удаления

def edit_func():
    selected_indices = station_list.curselection()
    if not selected_indices:
        messagebox.showwarning("Ошибка", "Пожалуйста, выберите имя для редактирования.")
        return

    index = selected_indices[0]
    full_name = station_list.get(index)
    name, surname = full_name.split()

    top = Toplevel(window)
    top.title("Редактировать имя")
    label_name = Label(top, text='Имя:')
    label_name.pack()
    entry_name = Entry(top)
    entry_name.insert(0, name)
    entry_name.pack()

    label_surname = Label(top, text='Фамилия:')
    label_surname.pack()
    entry_surname = Entry(top)
    entry_surname.insert(0, surname)
    entry_surname.pack()

    def submit():
        new_name = entry_name.get()
        new_surname = entry_surname.get()
        if new_name and new_surname:
            full_name = f"{new_name} {new_surname}"
            station_list.delete(index)  # Удаляем старую запись
            station_list.insert(index, full_name)  # Вставляем новую запись
            station_list1.delete(index)  # Удаляем старую запись в списке подробностей
            station_list1.insert(index, f"Имя: {new_name}, Фамилия: {new_surname}")  # Вставляем новую запись
            save_names()  # Save names after editing
            top.destroy()
            update_additional_info()  # Обновляем дополнительную информацию после редактирования
        else:
            messagebox.showwarning("Ошибка", "Пожалуйста, заполните все поля.")

    btn_submit = Button(top, text='Сохранить', command=submit)
    btn_submit.pack()
    button_top_level = Button(top, text='Закрыть', command=top.destroy)
    button_top_level.pack()
    top.transient(window)
    top.grab_set()
    top.focus_set()
    top.wait_window()

def update_additional_info(event=None):
    """Обновляем дополнительную информацию на основе выбранного имени."""
    station_list1.delete(0, END)  # Очищаем старые записи
    selected_indices = station_list.curselection()
    for index in selected_indices:
        full_name = station_list.get(index)
        name, surname = full_name.split()
        station_list1.insert(END, f"Имя: {name}, Фамилия: {surname}")

# Создание главного окна
window = Tk()
window.title('AddressApp')
window.resizable(0, 0)

station_list = Listbox(window, width=50)
station_list.grid(row=0, column=0, columnspan=1, padx=0)
station_list1 = Listbox(window, width=50)
station_list1.grid(row=0, column=2, columnspan=1, padx=0)



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

# Привязываем обновление дополнительной информации к событию выбора элемента
station_list.bind('<<ListboxSelect>>', update_additional_info)

load_names()

# Кнопки управления
btn_1 = Button(window, text="Delete", bg="black", width=20, fg="white", height=2, command=delete_func)
btn_1.grid(row=2, column=0, sticky=S, pady=30, padx=10)
btn_2 = Button(window, text="Edit...", bg="black", width=20, fg="white", height=2, command=edit_func)
btn_2.grid(row=2, column=1, sticky=S, pady=30, padx=10)
btn_3 = Button(window, text="New...", bg="black", width=20, fg="white", height=2, command=add_name)
btn_3.grid(row=2, column=2, sticky=S, pady=30, padx=10)

# Запуск основного цикла
window.mainloop()