import os
from tkinter import *
from tkinter import font
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import showerror

# elem_file = open('elems.txt', '+')

elem_list = []
path_list = []
scr_list = []
elem_ind = 0
scrt_ind = 1


class Element:
    def __init__(self, path):
        global path_list
        self.path = path
        path_list.insert(0, self.path)
        pth_list = str(path).split(sep="/")
        self.name = pth_list[len(pth_list) - 1]
        del1_menu.add_command(label=self.name, command=self.delete)
        elem_list.insert(0, self.name)

    def delete(self):
        global elem_ind
        del1_menu.delete(self.name)
        elem_list.remove(self.name)
        elem_ind -= 1
        try:
            elem_list[0]
        except IndexError:
            edit_menu.entryconfig(2, state=DISABLED)
            for i in scr_list:
                i.ch_elem_1.configure(values=elem_list, state=DISABLED)
                i.ch_elem_2.configure(values=elem_list, state=DISABLED)
                i.ch_elem_3.configure(values=elem_list, state=DISABLED)
                i.ch_elem_4.configure(values=elem_list, state=DISABLED)
                i.ch_elem_5.configure(values=elem_list, state=DISABLED)
                i.ch_elem_6.configure(values=elem_list, state=DISABLED)
                i.ch_elem_7.configure(values=elem_list, state=DISABLED)
                i.ch_elem_8.configure(values=elem_list, state=DISABLED)
                i.ch_elem_9.configure(values=elem_list, state=DISABLED)
                i.ch_elem_10.configure(values=elem_list, state=DISABLED)
        else:
            edit_menu.entryconfig(1, state=NORMAL)
            for i in scr_list:
                i.ch_elem_1.configure(values=elem_list, state=NORMAL)
                i.ch_elem_2.configure(values=elem_list, state=NORMAL)
                i.ch_elem_3.configure(values=elem_list, state=NORMAL)
                i.ch_elem_4.configure(values=elem_list, state=NORMAL)
                i.ch_elem_5.configure(values=elem_list, state=NORMAL)
                i.ch_elem_6.configure(values=elem_list, state=NORMAL)
                i.ch_elem_7.configure(values=elem_list, state=NORMAL)
                i.ch_elem_8.configure(values=elem_list, state=NORMAL)
                i.ch_elem_9.configure(values=elem_list, state=NORMAL)
                i.ch_elem_10.configure(values=elem_list, state=NORMAL)


class Script:
    def __init__(self, name=""):
        self.name = name
        self.frame_main = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 8])
        self.frame_main.pack(anchor=NW, fill=X, padx=5, pady=5)
        self.frame_name = ttk.Frame(master=self.frame_main, borderwidth=1, relief=SOLID, padding=[8, 8])
        self.frame_name.pack(anchor=NW, fill=X, padx=1, pady=1)
        self.close_but = ttk.Button(master=self.frame_main, text="▼", width=2, command=self.close)
        self.close_but.pack(anchor=NW)
        self.show_but = ttk.Button(master=self.frame_main, text="▲", width=2, command=self.show)
        self.start_but = ttk.Button(master=self.frame_main, text="Запустить", command=self.start)
        self.start_but.place(x=120, y=45)
        self.frame_elem = ttk.Frame(master=self.frame_main, borderwidth=1, relief=SOLID, padding=[8, 8])
        self.save_name_but = ttk.Button(master=self.frame_name, text="Сохранить", command=self.save)
        self.save_name_but.pack(anchor=NE)
        self.name_ent = ttk.Entry(master=self.frame_name)
        self.name_ent.place(x=0, y=3)
        self.name_ent.insert(0, f"Сценарий {scrt_ind}")
        self.name_ent.focus_set()
        self.name_ent.selection_range(0, END)
        del2_menu.add_command(label=self.name, command=self.delete)
        scr_list.append(self)

        self.ch_elem_1 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_list, state=DISABLED)
        self.ch_elem_1.pack(anchor=NW, pady=3)
        self.ch_elem_2 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_list, state=DISABLED)
        self.ch_elem_2.pack(anchor=NW, pady=3)
        self.ch_elem_3 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_list, state=DISABLED)
        self.ch_elem_3.pack(anchor=NW, pady=3)
        self.ch_elem_4 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_list, state=DISABLED)
        self.ch_elem_4.pack(anchor=NW, pady=3)
        self.ch_elem_5 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_list, state=DISABLED)
        self.ch_elem_5.pack(anchor=NW, pady=3)
        self.ch_elem_6 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_list, state=DISABLED)
        self.ch_elem_6.place(x=170, y=3)
        self.ch_elem_7 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_list, state=DISABLED)
        self.ch_elem_7.place(x=170, y=30)
        self.ch_elem_8 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_list, state=DISABLED)
        self.ch_elem_8.place(x=170, y=57)
        self.ch_elem_9 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_list, state=DISABLED)
        self.ch_elem_9.place(x=170, y=84)
        self.ch_elem_10 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_list, state=DISABLED)
        self.ch_elem_10.place(x=170, y=111)

        self.close()


    # def clear(self):
    #     self.ch_elem_1.set('')
    #     self.ch_elem_2.set('')
    #     self.ch_elem_3.set('')
    #     self.ch_elem_4.set('')
    #     self.ch_elem_5.set('')
    #     self.ch_elem_6.set('')
    #     self.ch_elem_7.set('')
    #     self.ch_elem_8.set('')
    #     self.ch_elem_9.set('')
    #     self.ch_elem_10.set('')
    def delete(self):
        global scrt_ind
        del2_menu.delete(self.name)
        scr_list.remove(self.name)
        self.frame_main.destroy()
        scrt_ind -= 1
        try:
            scr_list[0]
        except IndexError:
            file_menu.entryconfig(2, state=DISABLED)
        else:
            file_menu.entryconfig(1, state=NORMAL)

    def save(self):
        global scrt_ind
        del2_menu.delete(self.name)
        scr_list.remove(self)
        self.name = self.name_ent.get()
        if self.name == "Имя сценария":
            self.name = f"Сценарий {scrt_ind}"
            self.name_ent.delete(0, END)
            self.name_ent.insert(0, self.name)
            del2_menu.add_command(label=self.name, command=self.delete)
            scr_list.append(self.name)
            self.save_name_but.configure(state=DISABLED)
        else:
            del2_menu.add_command(label=self.name, command=self.delete)
            scr_list.append(self.name)
            self.save_name_but.configure(state=DISABLED)

    def close(self):
        self.frame_elem.pack_forget()
        self.close_but.pack_forget()
        self.show_but.pack(anchor=NW)

    def show(self):
        self.close_but.pack(anchor=NW)
        self.frame_elem.pack(anchor=NW, fill=X, padx=1, pady=1)
        self.show_but.pack_forget()

    def get_elems(self):
        self.ch1 = self.ch_elem_1.get()
        self.ch2 = self.ch_elem_1.get()
        self.ch3 = self.ch_elem_1.get()
        self.ch4 = self.ch_elem_1.get()
        self.ch5 = self.ch_elem_1.get()
        self.ch6 = self.ch_elem_1.get()
        self.ch7 = self.ch_elem_1.get()
        self.ch8 = self.ch_elem_1.get()
        self.ch9 = self.ch_elem_1.get()
        self.ch10 = self.ch_elem_1.get()

    def start(self):
        self.get_elems()
        if self.ch1 == "":
            pass
        else:
            os.startfile(path_list[elem_list.index(self.ch1)])
        if self.ch2 == "":
            pass
        else:
            os.startfile(path_list[elem_list.index(self.ch2)])
        if self.ch3 == "":
            pass
        else:
            os.startfile(path_list[elem_list.index(self.ch3)])
        if self.ch4 == "":
            pass
        else:
            os.startfile(path_list[elem_list.index(self.ch4)])
        if self.ch5 == "":
            pass
        else:
            os.startfile(path_list[elem_list.index(self.ch5)])
        if self.ch6 == "":
            pass
        else:
            os.startfile(path_list[elem_list.index(self.ch6)])
        if self.ch7 == "":
            pass
        else:
            os.startfile(path_list[elem_list.index(self.ch7)])
        if self.ch8 == "":
            pass
        else:
            os.startfile(path_list[elem_list.index(self.ch8)])
        if self.ch9 == "":
            pass
        else:
            os.startfile(path_list[elem_list.index(self.ch9)])
        if self.ch10 == "":
            pass
        else:
            os.startfile(path_list[elem_list.index(self.ch10)])

def ch_file():
    global elem_ind
    if elem_ind > 50:
        showerror(message="Количество одновременно загруженых файлов не может превышать 50!")
    else:
        file = filedialog.askopenfilename()
        if file == "":
            pass
        else:
            Element(file)
            elem_ind += 1
        try:
            elem_list[0]
        except IndexError:
            edit_menu.entryconfig(2, state=DISABLED)
            for i in scr_list:
                i.ch_elem_1.configure(values=elem_list, state=DISABLED)
                i.ch_elem_2.configure(values=elem_list, state=DISABLED)
                i.ch_elem_3.configure(values=elem_list, state=DISABLED)
                i.ch_elem_4.configure(values=elem_list, state=DISABLED)
                i.ch_elem_5.configure(values=elem_list, state=DISABLED)
                i.ch_elem_6.configure(values=elem_list, state=DISABLED)
                i.ch_elem_7.configure(values=elem_list, state=DISABLED)
                i.ch_elem_8.configure(values=elem_list, state=DISABLED)
                i.ch_elem_9.configure(values=elem_list, state=DISABLED)
                i.ch_elem_10.configure(values=elem_list, state=DISABLED)
        else:
            edit_menu.entryconfig(1, state=NORMAL)
            for i in scr_list:
                i.ch_elem_1.configure(values=elem_list, state=NORMAL)
                i.ch_elem_2.configure(values=elem_list, state=NORMAL)
                i.ch_elem_3.configure(values=elem_list, state=NORMAL)
                i.ch_elem_4.configure(values=elem_list, state=NORMAL)
                i.ch_elem_5.configure(values=elem_list, state=NORMAL)
                i.ch_elem_6.configure(values=elem_list, state=NORMAL)
                i.ch_elem_7.configure(values=elem_list, state=NORMAL)
                i.ch_elem_8.configure(values=elem_list, state=NORMAL)
                i.ch_elem_9.configure(values=elem_list, state=NORMAL)
                i.ch_elem_10.configure(values=elem_list, state=NORMAL)

def cr_scrt():
    global scrt_ind
    if scrt_ind == 6:
        showerror(message="Количество одновременно созданных сценариев не может превышать 5!")
    else:
        Script(name="")
        scrt_ind += 1
        try:
            scr_list[0]
        except IndexError:
            file_menu.entryconfig(2, state=DISABLED)
        else:
            file_menu.entryconfig(1, state=NORMAL)


root = Tk()  # Создаем окно
root.title("Автозапускатель")
root.geometry("350x670")
root.resizable(False, False)

font1 = font.Font(family="Arial", size=11, weight="normal", slant="roman")

main_menu = Menu()
file_menu = Menu(tearoff=0)
edit_menu = Menu(tearoff=0)
del1_menu = Menu(tearoff=0)
del2_menu = Menu(tearoff=0)

main_menu.add_cascade(label="Сценарии", menu=file_menu)
main_menu.add_cascade(label="Редактировать сценарии", menu=edit_menu)

file_menu.add_command(label="Создать", command=cr_scrt)
file_menu.add_cascade(label="Удалить", menu=del2_menu)

edit_menu.add_command(label="Добавить путь", command=ch_file)
edit_menu.add_cascade(label="Удалить путь", menu=del1_menu)

no_scrt_yet_lab = ttk.Label(text="Ещё нет созданных сценариев!", font=font1, foreground="grey50")
no_scrt_yet_lab.place(anchor=N, x=175, y=10)

try:
    elem_list[0]
except IndexError:
    edit_menu.entryconfig(2, state=DISABLED)
    for i in scr_list:
        i.ch_elem_1.configure(values=elem_list, state=DISABLED)
        i.ch_elem_2.configure(values=elem_list, state=DISABLED)
        i.ch_elem_3.configure(values=elem_list, state=DISABLED)
        i.ch_elem_4.configure(values=elem_list, state=DISABLED)
        i.ch_elem_5.configure(values=elem_list, state=DISABLED)
        i.ch_elem_6.configure(values=elem_list, state=DISABLED)
        i.ch_elem_7.configure(values=elem_list, state=DISABLED)
        i.ch_elem_8.configure(values=elem_list, state=DISABLED)
        i.ch_elem_9.configure(values=elem_list, state=DISABLED)
        i.ch_elem_10.configure(values=elem_list, state=DISABLED)
else:
    edit_menu.entryconfig(1, state=NORMAL)
    for i in scr_list:
        i.ch_elem_1.configure(values=elem_list, state=NORMAL)
        i.ch_elem_2.configure(values=elem_list, state=NORMAL)
        i.ch_elem_3.configure(values=elem_list, state=NORMAL)
        i.ch_elem_4.configure(values=elem_list, state=NORMAL)
        i.ch_elem_5.configure(values=elem_list, state=NORMAL)
        i.ch_elem_6.configure(values=elem_list, state=NORMAL)
        i.ch_elem_7.configure(values=elem_list, state=NORMAL)
        i.ch_elem_8.configure(values=elem_list, state=NORMAL)
        i.ch_elem_9.configure(values=elem_list, state=NORMAL)
        i.ch_elem_10.configure(values=elem_list, state=NORMAL)

try:
    scr_list[0]
except IndexError:
    file_menu.entryconfig(2, state=DISABLED)
else:
    file_menu.entryconfig(1, state=NORMAL)

root.config(menu=main_menu)
mainloop()
