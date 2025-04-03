from tkinter import *
window = Tk()
window.title( 'AddressApp' )
window.resizable(0,0)
Label(text="Введите номер станции назначения:").grid(row=0, column=0, sticky=N+W,
                                                     pady=10, padx=10)
Scrollbar(window).grid(row=0, column=2, sticky=N+S+E+W)
station_numb = Entry(width = 3)
Listbox(window, width = 50).grid(row=0, column=1)
station_list = Listbox(window, width = 50)
station_list.grid(row=0, column=2, columnspan = 5,
                  padx=10)
#Размещаем в ячейке (1,0) метку с текстом

station_numb = Entry(width = 3)
station_numb.grid(row=1, column=1, sticky=W,
                  pady=10, padx=10)
station_numb = Entry(width = 5)

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



window.mainloop()