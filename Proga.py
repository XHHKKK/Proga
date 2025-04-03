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

window.mainloop()