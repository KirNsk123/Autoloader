import os
from tkinter import *
from tkinter import font
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import showerror
import sqlite3

elem_db = sqlite3.connect('elems.db')
elem_cur = elem_db.cursor()

scrt_db = sqlite3.connect('scrts.db')
scrt_cur = scrt_db.cursor()

try:
    elem_cur.execute("""CREATE TABLE elems
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        path TEXT
                        )
                    """)
    scrt_cur.execute("""CREATE TABLE scrt1
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            elem1 TEXT,
                            elem2 TEXT,
                            elem3 TEXT,
                            elem4 TEXT,
                            elem5 TEXT,
                            elem6 TEXT,
                            elem7 TEXT,
                            elem8 TEXT,
                            elem9 TEXT,
                            elem10 TEXT
                            )
                        """)
    scrt_cur.execute("""CREATE TABLE scrt2
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            elem1 TEXT,
                            elem2 TEXT,
                            elem3 TEXT,
                            elem4 TEXT,
                            elem5 TEXT,
                            elem6 TEXT,
                            elem7 TEXT,
                            elem8 TEXT,
                            elem9 TEXT,
                            elem10 TEXT
                            )
                        """)
    scrt_cur.execute("""CREATE TABLE scrt3
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            elem1 TEXT,
                            elem2 TEXT,
                            elem3 TEXT,
                            elem4 TEXT,
                            elem5 TEXT,
                            elem6 TEXT,
                            elem7 TEXT,
                            elem8 TEXT,
                            elem9 TEXT,
                            elem10 TEXT
                            )
                        """)
    scrt_cur.execute("""CREATE TABLE scrt4
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            elem1 TEXT,
                            elem2 TEXT,
                            elem3 TEXT,
                            elem4 TEXT,
                            elem5 TEXT,
                            elem6 TEXT,
                            elem7 TEXT,
                            elem8 TEXT,
                            elem9 TEXT,
                            elem10 TEXT
                            )
                        """)
    scrt_cur.execute("""CREATE TABLE scrt5
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            elem1 TEXT,
                            elem2 TEXT,
                            elem3 TEXT,
                            elem4 TEXT,
                            elem5 TEXT,
                            elem6 TEXT,
                            elem7 TEXT,
                            elem8 TEXT,
                            elem9 TEXT,
                            elem10 TEXT
                            )
                        """)
except sqlite3.OperationalError:
    pass
else:
    pass

elem_name_list = []
elem_list = []
path_list = []
scr_list = []
other_list = []
elem_ind = 0
scrt_ind = 1


class Element:
    def __init__(self, path, state="new"):
        global path_list
        self.path = path
        path_list.insert(0, self.path)
        pth_list = str(path).split(sep="/")
        self.name = pth_list[len(pth_list) - 1]
        del1_menu.add_command(label=self.name, command=self.delete)
        elem_name_list.insert(0, self.name)
        elem_list.insert(0, self)
        self.state = state

    def delete(self):
        global elem_ind
        del1_menu.delete(self.name)
        elem_name_list.remove(self.name)
        elem_list.remove(self)
        elem_cur.execute("DELETE FROM elems WHERE path=?", (self.path,))
        elem_db.commit()
        elem_ind -= 1
        try:
            elem_name_list[0]
        except IndexError:
            edit_menu.entryconfig(1, state=DISABLED)
            for i in scr_list:
                i.ch_elem_1.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_2.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_3.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_4.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_5.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_6.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_7.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_8.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_9.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_10.configure(values=elem_name_list, state=DISABLED)
        else:
            edit_menu.entryconfig(1, state=NORMAL)
            for i in scr_list:
                i.ch_elem_1.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_2.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_3.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_4.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_5.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_6.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_7.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_8.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_9.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_10.configure(values=elem_name_list, state=NORMAL)


class Script:
    def __init__(self, name="", state="closed", ch1="", ch2="", ch3="",
                 ch4="", ch5="", ch6="", ch7="", ch8="", ch9="", ch10=""):
        self.name = name
        self.index = scrt_ind
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
        self.save_elems_but = ttk.Button(master=self.frame_elem, text="Сохранить", command=self.save_elems)
        del2_menu.add_command(label=self.name, command=self.delete)
        scr_list.append(self)
        other_list.append(self)
        self.state = state

        self.ch1 = ch1
        self.ch2 = ch2
        self.ch3 = ch3
        self.ch4 = ch4
        self.ch5 = ch5
        self.ch6 = ch6
        self.ch7 = ch7
        self.ch8 = ch8
        self.ch9 = ch9
        self.ch10 = ch10

        self.ch_elem_1 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_name_list, state=DISABLED)
        self.ch_elem_1.pack(anchor=NW, pady=3)
        self.ch_elem_2 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_name_list, state=DISABLED)
        self.ch_elem_2.pack(anchor=NW, pady=3)
        self.ch_elem_3 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_name_list, state=DISABLED)
        self.ch_elem_3.pack(anchor=NW, pady=3)
        self.ch_elem_4 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_name_list, state=DISABLED)
        self.ch_elem_4.pack(anchor=NW, pady=3)
        self.ch_elem_5 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_name_list, state=DISABLED)
        self.ch_elem_5.pack(anchor=NW, pady=3)
        self.ch_elem_6 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_name_list, state=DISABLED)
        self.ch_elem_6.place(x=170, y=3)
        self.ch_elem_7 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_name_list, state=DISABLED)
        self.ch_elem_7.place(x=170, y=30)
        self.ch_elem_8 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_name_list, state=DISABLED)
        self.ch_elem_8.place(x=170, y=57)
        self.ch_elem_9 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_name_list, state=DISABLED)
        self.ch_elem_9.place(x=170, y=84)
        self.ch_elem_10 = ttk.Combobox(master=self.frame_elem, width=18, values=elem_name_list, state=DISABLED)
        self.ch_elem_10.place(x=170, y=111)

        self.save_elems_but.pack()

        self.close()

        try:
            elem_name_list[0]
        except IndexError:
            edit_menu.entryconfig(1, state=DISABLED)
            for i in scr_list:
                i.ch_elem_1.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_2.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_3.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_4.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_5.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_6.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_7.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_8.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_9.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_10.configure(values=elem_name_list, state=DISABLED)
        else:
            edit_menu.entryconfig(1, state=NORMAL)
            for i in scr_list:
                i.ch_elem_1.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_2.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_3.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_4.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_5.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_6.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_7.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_8.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_9.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_10.configure(values=elem_name_list, state=NORMAL)

    def delete(self):
        global scrt_ind
        del2_menu.delete(self.name)
        scr_list.remove(self)
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
            scr_list.append(self)
            self.save_name_but.configure(state=DISABLED)
        else:
            del2_menu.add_command(label=self.name, command=self.delete)
            scr_list.append(self)
            self.save_name_but.configure(state=DISABLED)
        scrt_cur.execute(f"INSERT INTO scrts (name) VALUES (?)", (self.name,))
        scrt_db.commit()

    def close(self):
        self.frame_elem.pack_forget()
        self.close_but.pack_forget()
        self.show_but.pack(anchor=NW)
        self.state = "closed"
        scrt_cur.execute("SELECT * FROM scrts")

    def show(self):
        # scr_list.remove(self)
        # for i in scr_list:
        #     if i.state == "opened":
        #         i.close()
        self.close_but.pack(anchor=NW)
        self.frame_elem.pack(anchor=NW, fill=X, padx=1, pady=1)
        self.show_but.pack_forget()

    def start(self):
        self.ch1 = self.ch_elem_1.get()
        self.ch2 = self.ch_elem_2.get()
        self.ch3 = self.ch_elem_3.get()
        self.ch4 = self.ch_elem_4.get()
        self.ch5 = self.ch_elem_5.get()
        self.ch6 = self.ch_elem_6.get()
        self.ch7 = self.ch_elem_7.get()
        self.ch8 = self.ch_elem_8.get()
        self.ch9 = self.ch_elem_9.get()
        self.ch10 = self.ch_elem_10.get()
        if self.ch1 == "":
            pass
        else:
            os.startfile(path_list[elem_name_list.index(self.ch1)])
        if self.ch2 == "":
            pass
        else:
            os.startfile(path_list[elem_name_list.index(self.ch2)])
        if self.ch3 == "":
            pass
        else:
            os.startfile(path_list[elem_name_list.index(self.ch3)])
        if self.ch4 == "":
            pass
        else:
            os.startfile(path_list[elem_name_list.index(self.ch4)])
        if self.ch5 == "":
            pass
        else:
            os.startfile(path_list[elem_name_list.index(self.ch5)])
        if self.ch6 == "":
            pass
        else:
            os.startfile(path_list[elem_name_list.index(self.ch6)])
        if self.ch7 == "":
            pass
        else:
            os.startfile(path_list[elem_name_list.index(self.ch7)])
        if self.ch8 == "":
            pass
        else:
            os.startfile(path_list[elem_name_list.index(self.ch8)])
        if self.ch9 == "":
            pass
        else:
            os.startfile(path_list[elem_name_list.index(self.ch9)])
        if self.ch10 == "":
            pass
        else:
            os.startfile(path_list[elem_name_list.index(self.ch10)])

    def save_elems(self):
        try:
            pass
        except ValueError:
            showerror(message="Невозможно сохранить: Не выбраны элементы!")
        self.ch1 = self.ch_elem_1.get()
        self.ch2 = self.ch_elem_2.get()
        self.ch3 = self.ch_elem_3.get()
        self.ch4 = self.ch_elem_4.get()
        self.ch5 = self.ch_elem_5.get()
        self.ch6 = self.ch_elem_6.get()
        self.ch7 = self.ch_elem_7.get()
        self.ch8 = self.ch_elem_8.get()
        self.ch9 = self.ch_elem_9.get()
        self.ch10 = self.ch_elem_10.get()
        if self.ch1 == "":
            pass
        else:
            scrt_cur.execute("UPDATE scrts SET elem1 =? WHERE name=?", (path_list[elem_name_list.index(self.ch1)],
                                                                        self.name))
        if self.ch2 == "":
            pass
        else:
            scrt_cur.execute("UPDATE scrts SET elem1 =? WHERE name=?", (path_list[elem_name_list.index(self.ch2)],
                                                                        self.name))
        if self.ch3 == "":
            pass
        else:
            scrt_cur.execute("UPDATE scrts SET elem1 =? WHERE name=?", (path_list[elem_name_list.index(self.ch3)],
                                                                        self.name))
        if self.ch4 == "":
            pass
        else:
            scrt_cur.execute("UPDATE scrts SET elem1 =? WHERE name=?", (path_list[elem_name_list.index(self.ch4)],
                                                                        self.name))
        if self.ch5 == "":
            pass
        else:
            scrt_cur.execute("UPDATE scrts SET elem1 =? WHERE name=?", (path_list[elem_name_list.index(self.ch5)],
                                                                        self.name))
        if self.ch6 == "":
            pass
        else:
            scrt_cur.execute("UPDATE scrts SET elem1 =? WHERE name=?", (path_list[elem_name_list.index(self.ch6)],
                                                                        self.name))
        if self.ch7 == "":
            pass
        else:
            scrt_cur.execute("UPDATE scrts SET elem1 =? WHERE name=?", (path_list[elem_name_list.index(self.ch7)],
                                                                        self.name))
        if self.ch8 == "":
            pass
        else:
            scrt_cur.execute("UPDATE scrts SET elem1 =? WHERE name=?", (path_list[elem_name_list.index(self.ch8)],
                                                                        self.name))
        if self.ch9 == "":
            pass
        else:
            scrt_cur.execute("UPDATE scrts SET elem1 =? WHERE name=?", (path_list[elem_name_list.index(self.ch9)],
                                                                        self.name))
        if self.ch10 == "":
            pass
        else:
            scrt_cur.execute("UPDATE scrts SET elem1 =? WHERE name=?", (path_list[elem_name_list.index(self.ch10)],
                                                                        self.name))
        scrt_db.commit()


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
            elem_name_list[0]
        except IndexError:
            edit_menu.entryconfig(1, state=DISABLED)
            for i in scr_list:
                i.ch_elem_1.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_2.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_3.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_4.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_5.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_6.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_7.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_8.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_9.configure(values=elem_name_list, state=DISABLED)
                i.ch_elem_10.configure(values=elem_name_list, state=DISABLED)
        else:
            edit_menu.entryconfig(1, state=NORMAL)
            for i in scr_list:
                i.ch_elem_1.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_2.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_3.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_4.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_5.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_6.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_7.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_8.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_9.configure(values=elem_name_list, state=NORMAL)
                i.ch_elem_10.configure(values=elem_name_list, state=NORMAL)


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


def load_elems_to_db():
    for i in elem_list:
        if i.state == "old":
            pass
        elif i.state == "new":
            elem_cur.execute("INSERT INTO elems (path) VALUES (?)", (i.path,))
            elem_db.commit()


def start_app():
    try:
        elem_name_list[0]
    except IndexError:
        edit_menu.entryconfig(1, state=DISABLED)
        for i in scr_list:
            i.ch_elem_1.configure(values=elem_name_list, state=DISABLED)
            i.ch_elem_2.configure(values=elem_name_list, state=DISABLED)
            i.ch_elem_3.configure(values=elem_name_list, state=DISABLED)
            i.ch_elem_4.configure(values=elem_name_list, state=DISABLED)
            i.ch_elem_5.configure(values=elem_name_list, state=DISABLED)
            i.ch_elem_6.configure(values=elem_name_list, state=DISABLED)
            i.ch_elem_7.configure(values=elem_name_list, state=DISABLED)
            i.ch_elem_8.configure(values=elem_name_list, state=DISABLED)
            i.ch_elem_9.configure(values=elem_name_list, state=DISABLED)
            i.ch_elem_10.configure(values=elem_name_list, state=DISABLED)
    else:
        edit_menu.entryconfig(1, state=NORMAL)
        for i in scr_list:
            i.ch_elem_1.configure(values=elem_name_list, state=NORMAL)
            i.ch_elem_2.configure(values=elem_name_list, state=NORMAL)
            i.ch_elem_3.configure(values=elem_name_list, state=NORMAL)
            i.ch_elem_4.configure(values=elem_name_list, state=NORMAL)
            i.ch_elem_5.configure(values=elem_name_list, state=NORMAL)
            i.ch_elem_6.configure(values=elem_name_list, state=NORMAL)
            i.ch_elem_7.configure(values=elem_name_list, state=NORMAL)
            i.ch_elem_8.configure(values=elem_name_list, state=NORMAL)
            i.ch_elem_9.configure(values=elem_name_list, state=NORMAL)
            i.ch_elem_10.configure(values=elem_name_list, state=NORMAL)


root = Tk()  # Создаем окно
root.title("Автозапускатель")
root.geometry("350x690")
root.resizable(False, False)

font1 = font.Font(family="Arial", size=11, weight="normal", slant="roman")

font2 = font.Font(family="Arial", size=11, weight="normal", slant="roman")  # Лейбл создателя
creatorLabel = ttk.Label(text="Author: KirNsk", font=font2, foreground="grey50")
creatorLabel.place(x=125, y=670)

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
edit_menu.add_command(label="Сохранить пути", command=load_elems_to_db)

no_scrt_yet_lab = ttk.Label(text="Ещё нет созданных сценариев!", font=font1, foreground="grey50")
no_scrt_yet_lab.place(anchor=N, x=175, y=10)

try:
    elem_name_list[0]
except IndexError:
    edit_menu.entryconfig(1, state=DISABLED)
    for i in scr_list:
        i.ch_elem_1.configure(values=elem_name_list, state=DISABLED)
        i.ch_elem_2.configure(values=elem_name_list, state=DISABLED)
        i.ch_elem_3.configure(values=elem_name_list, state=DISABLED)
        i.ch_elem_4.configure(values=elem_name_list, state=DISABLED)
        i.ch_elem_5.configure(values=elem_name_list, state=DISABLED)
        i.ch_elem_6.configure(values=elem_name_list, state=DISABLED)
        i.ch_elem_7.configure(values=elem_name_list, state=DISABLED)
        i.ch_elem_8.configure(values=elem_name_list, state=DISABLED)
        i.ch_elem_9.configure(values=elem_name_list, state=DISABLED)
        i.ch_elem_10.configure(values=elem_name_list, state=DISABLED)
else:
    edit_menu.entryconfig(1, state=NORMAL)
    for i in scr_list:
        i.ch_elem_1.configure(values=elem_name_list, state=NORMAL)
        i.ch_elem_2.configure(values=elem_name_list, state=NORMAL)
        i.ch_elem_3.configure(values=elem_name_list, state=NORMAL)
        i.ch_elem_4.configure(values=elem_name_list, state=NORMAL)
        i.ch_elem_5.configure(values=elem_name_list, state=NORMAL)
        i.ch_elem_6.configure(values=elem_name_list, state=NORMAL)
        i.ch_elem_7.configure(values=elem_name_list, state=NORMAL)
        i.ch_elem_8.configure(values=elem_name_list, state=NORMAL)
        i.ch_elem_9.configure(values=elem_name_list, state=NORMAL)
        i.ch_elem_10.configure(values=elem_name_list, state=NORMAL)

elem_cur.execute("SELECT * FROM elems")

for i in range(50):
    obj = elem_cur.fetchone()
    if obj is None:
        break
    else:
        Element(obj[1], state="old")

try:
    scr_list[0]
except IndexError:
    file_menu.entryconfig(2, state=DISABLED)
else:
    file_menu.entryconfig(1, state=NORMAL)

start_app()

root.config(menu=main_menu)
mainloop()
