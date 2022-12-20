import tkinter as tk
from tkinter import ttk, END
from tkinter import messagebox
#from PIL import Image, ImageTk
import sqlite3

last_ID = 0
workers = {}

def check_if_item_exist(str,file):
    with open(f"{file}", 'r') as f:
        item = f.read()
        if str in item:
            return True
    return False

def change_bg_color_of_inventory(dict,items,file):
    with open(f'{file}', 'r') as f:
        item = f.read()
        for i in items:
            if i in item:
                dict[i] = "red"
    return dict

def change_availability(flag):
    workers[last_ID] =flag

def test_is_exist(str):
    db = open('DataBase.txt', 'r')
    for i in db:
        arr = i.split()
        if(i!='\n'):
            if (arr[1] == str):
                db.close()
                return True

    db.close()
    return False


class Loginpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#4f558f")

        Label = tk.Label(self, text="Login Page", font=("Arial Bold", 30), bg="#4f558f")
        Label.place(x=270, y=80)
        self.User_ID = tk.Entry(self, width=30)
        self.User_ID.place(x=350, y=200)
        self.Password = tk.Entry(self, width=30, show='*')
        self.Password.place(x=350, y=250)
        User_IDL = tk.Label(self, text="User ID", font=("Arial Bold", 12), bg="#4f558f", fg="white")
        User_IDL.place(x=260, y=200)
        PasswordL = tk.Label(self, text="Password", font=("Arial Bold", 12), bg="#4f558f", fg="white")
        PasswordL.place(x=260, y=250)
        button = tk.Button(self, text="login", font=("Arial", 15),
                           command=lambda: self.validation(controller))

        button.place(x=650, y=450)

    def validation(self, controller):
        username = self.User_ID.get()
        usercode = self.Password.get().upper()
        self.User_ID.delete(0, END)
        self.Password.delete(0, END)
        Exists = False
        db = open('DataBase.txt', 'r')
        # [0]-type [1]-ID [2]-password [3]-name [4]-lastname
        for i in db:

            arr = i.split()
            if(i!='\n'):
                typ = arr[0]
                ID = arr[1]
                code = arr[2]

                if (username == ID and usercode == code):
                    Exists = True

                    if (typ == 'secretary'):
                        controller.show_frame(SecretaryHomePage)
                    elif (typ == 'manager'):
                        controller.show_frame(ManagerHomePage)
                    elif (typ == 'worker'):
                        global last_ID
                        last_ID = ID
                        controller.show_frame(WorkerHomePage)
                    else:
                        messagebox.showerror(title="error", message="Unknown error")

                    break


        if (Exists == False):
            messagebox.showerror(title="error", message="Invalid login")
        db.close()


##-------------------------------------------------------------------------------------------------------------------------------

class SecretaryHomePage(tk.Frame):  # מזכירה רפואית
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#4f558f")
        Label = tk.Label(self, text="Secretary", font=("Arial Bold", 30), bg="#4f558f")
        Label.place(x=270, y=80)
        button = tk.Button(self, text="logout", font=("Arial", 15),
                           command=lambda: controller.show_frame(Loginpage))
        button.place(x=650, y=450)


# ---------------------------------------------------------------------------------------------------------------------------

class ManagerHomePage(tk.Frame):  # מנהל

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#4f558f")
        equipment = tk.Button(self, text="Viewing equipment orders", font=("Arial", 12), command=self.check_supp)
        equipment.place(x=300, y=400)
        Label = tk.Label(self, text="Manager", font=("Arial Bold", 30), bg="#4f558f")
        Label.place(x=270, y=80)
        log_out = tk.Button(self, text="logout", font=("Arial", 15),
                            command=lambda: controller.show_frame(Loginpage))

        log_out.place(x=650, y=450)
        self.edit = tk.Button(self, text="edit workers", bg="light blue", command=self.edit_workers, width=10)
        self.edit.place(x=100, y=300)
        self.edit_window_is_open = False

    def edit_workers(self):
        if (self.edit_window_is_open == False):
            self.edit_window_is_open = True
            newWindow = tk.Toplevel(self)
            newWindow.title("edit workers")
            newWindow.configure(bg="bisque")
            newWindow.geometry("400x320")
            newWindow.resizable(False, False)
            remove_window_is_open = False
            add_window_is_open = False

            def on_closing():
                self.edit_window_is_open = False
                newWindow.destroy()

            def remove_worker():
                nonlocal remove_window_is_open
                if (remove_window_is_open == False):
                    remove_window_is_open = True
                    removeWindow = tk.Toplevel(self)
                    removeWindow.title("remove workers")
                    removeWindow.configure(bg="bisque")
                    removeWindow.geometry("400x320")
                    removeWindow.resizable(False, False)

                    def on_close_remove():
                        nonlocal remove_window_is_open, removeWindow
                        remove_window_is_open = False
                        removeWindow.destroy()

                    removeWindow.protocol("WM_DELETE_WINDOW", on_close_remove)

            def add_worker():
                nonlocal add_window_is_open
                if (add_window_is_open == False):
                    add_window_is_open = True
                    addWindow = tk.Toplevel(self)
                    addWindow.title("add workers")
                    addWindow.configure(bg="bisque")
                    addWindow.geometry("400x390")
                    addWindow.resizable(False, False)

                    Lname = tk.Label(addWindow, text="name", bg="bisque")
                    Llastname = tk.Label(addWindow, text="last name", bg="bisque")
                    Lpassword = tk.Label(addWindow, text="password", bg="bisque")
                    LID = tk.Label(addWindow, text="ID", bg="bisque")

                    name = tk.Entry(addWindow, width=30)
                    lastname = tk.Entry(addWindow, width=30)
                    password = tk.Entry(addWindow, width=30)
                    ID = tk.Entry(addWindow, width=30)

                    Lname.place(x=20, y=80)
                    Llastname.place(x=20, y=140)
                    Lpassword.place(x=20, y=200)
                    LID.place(x=20, y=260)

                    name.place(x=120, y=80)
                    lastname.place(x=120, y=140)
                    password.place(x=120, y=200)
                    ID.place(x=120, y=260)

                    def writing_to_database():

                        find = test_is_exist(ID.get())

                        if find == True:
                            messagebox.showerror(title="error", message="this worker is already exist")

                        if find == False and tk.messagebox.askyesno("Question", "Add this employee?") == True:
                            string = "worker " + ID.get() + " " + password.get().upper() + " " + name.get() + " " + lastname.get() + "\n"
                            db = open('DataBase.txt', 'a')
                            db.write(string)
                            db.close()
                            new_worker = open(f'{ID.get()}.txt', 'w', encoding='utf-8')
                            new_worker.write(string)
                            new_worker.close()
                            workers[ID.get()] = False
                            self.edit_window_is_open = False
                            addWindow.destroy()
                            newWindow.destroy()

                    add = tk.Button(addWindow, text="add", bg="white", width=10, command=writing_to_database)
                    add.place(x=160, y=300)

                    def on_close_add():
                        nonlocal add_window_is_open, addWindow
                        add_window_is_open = False
                        addWindow.destroy()

                    addWindow.protocol("WM_DELETE_WINDOW", on_close_add)

            add_worker = tk.Button(newWindow, text="add worker", font=("Arial", 15), width=12, bg="green",
                                   command=add_worker)
            add_worker.place(x=40, y=150)
            remove_worker = tk.Button(newWindow, text="remove worker", font=("Arial", 15), width=12, bg="red",
                                      command=remove_worker)
            remove_worker.place(x=210, y=150)
            newWindow.protocol("WM_DELETE_WINDOW", on_closing)

    def check_supp(self):
        master = tk.Toplevel()

        master.configure(bg="light blue")
        master.grid_rowconfigure(0, minsize=450)
        master.grid_columnconfigure(0, minsize=400)

        master.resizable(False, False)
        items = ['soap', 'bleach', 'disinfectant', 'broom', 'mop', 'rags', 'tissue', 'masks', 'gloves']

        items_color = {'soap': "light green", 'bleach': "light green", 'disinfectant': "light green",
                       'broom': "light green", 'mop': "light green", 'rags': "light green", 'tissue': "light green",
                       'masks': "light green", 'gloves': "light green"}
        items_color=change_bg_color_of_inventory(items_color,items,"choices.txt")


        soap = tk.Label(master, text="soap", bg=items_color['soap'], font=("Arial", 15)).place(x=180, y=20)
        bleach = tk.Label(master, text='bleach',bg=items_color['bleach'], font=("Arial", 15)).place(x=180, y=60)
        disinfectant = tk.Label(master, text='disinfectant', bg=items_color['disinfectant'], font=("Arial", 15)).place(x=180, y=100)
        broom = tk.Label(master, text='broom', bg=items_color['broom'], font=("Arial", 15)).place(x=180, y=140)
        mop = tk.Label(master, text='mop', bg=items_color['mop'], font=("Arial", 15)).place(x=180, y=180)
        rags = tk.Label(master, text='rags', bg=items_color['rags'], font=("Arial", 15)).place(x=180, y=220)
        tissue = tk.Label(master, text='tissue', bg=items_color['tissue'], font=("Arial", 15)).place(x=180, y=260)
        masks = tk.Label(master, text='masks', bg=items_color['masks'], font=("Arial", 15)).place(x=180, y=300)
        gloves = tk.Label(master, text='gloves', bg=items_color['gloves'], font=("Arial", 15)).place(x=180, y=340)
        directive = tk.Label(master, text='red-need to order\ngreen-in stck', bg="light blue", font=("Arial", 8)).place(
            x=160, y=400)

        def confrim():
            if tk.messagebox.askyesno("Question", "With your approval, the requests will be deleted") == True:
                open('choices.txt', 'w').close()
                master.destroy()


        confrim = tk.Button(master, text="Confirmation", command=confrim).grid(row=9, rowspan=13)


# ---------------------------------------------------------------------------------------------------------------------------------------------

class WorkerHomePage(tk.Frame):  # עובד ניקיון
    def join_out_work(self):

        if (self.present['text'] == "enter work"):
            self.present.configure(bg="green", text="at work")
            self.label_name.configure(text=f"hello {last_ID}")
            change_availability(True)

        elif (self.present['text'] == "at work"):
            self.present.configure(bg="red", text="enter work")
            self.label_name.configure(text="hello")
            change_availability(False)

    def clean(self):
        self.label_name.configure(text="hello ")
        workers[last_ID] = False
        self.join_out_work()

    def order_supp(self):
        buttons = ['soap', 'bleach', 'disinfectant', 'broom', 'mop', 'rags', 'tissue ', 'masks', 'gloves']
        btnElements = []

        def handleBtnClick(btnText):
            btnElements[buttons.index(btnText)]["background"] = "green"
            exsist = check_if_item_exist(btnText,"choices.txt")


            if (exsist == False):
                with open("choices.txt", 'a+') as f:
                    f.write(btnText + "\r")

        master = tk.Toplevel(self)

        master.configure(bg="light blue")

        tk.Label(master, text="Mark if missing :", bg="light blue").grid(row=0)
        tk.Label(master, text="Mark if missing :", bg="light blue").grid(row=1)
        tk.Label(master, text="Mark if missing :", bg="light blue").grid(row=2)
        tk.Label(master, text="Mark if missing :", bg="light blue").grid(row=3)
        tk.Label(master, text="Mark if missing :", bg="light blue").grid(row=4)
        tk.Label(master, text="Mark if missing :", bg="light blue").grid(row=5)
        tk.Label(master, text="Mark if missing :", bg="light blue").grid(row=6)
        tk.Label(master, text="Mark if missing :", bg="light blue").grid(row=7)
        tk.Label(master, text="Mark if missing :", bg="light blue").grid(row=8)

        for i, z in enumerate(buttons):
            btnElements.append(tk.Button(master, text=z, width=12, command=lambda ztemp=z: handleBtnClick(ztemp)))
            btnElements[i].grid(
                row=i,
                column=2,
                sticky=tk.W)

        tk.Button(master, text='Order Confirmation', command=master.destroy).grid(row=10, column=1, sticky=tk.W)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lorder = tk.Button(self, text="order supplies", font=("Arial Bold", 20), bg="yellow", command=self.order_supp)
        lorder.place(x=200, y=280)
        self.label_name = tk.Label(self, text="hello ", font=("Arial Bold", 20), bg="#4f558f")
        self.label_name.place(x=80, y=200)
        self.configure(bg="#4f558f")
        Label = tk.Label(self, text="Worker", font=("Arial Bold", 30), bg="#4f558f")
        Label.place(x=270, y=80)
        button = tk.Button(self, text="logout", font=("Arial", 15),
                           command=lambda: [self.clean(), controller.show_frame(Loginpage)])
        button.place(x=650, y=450)
        self.present = tk.Button(self, text="enter work", bg="red", command=self.join_out_work, width=10)
        self.present.place(x=100, y=300)


# ---------------------------------------------------------------------------------------------------------------------------------------
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()
        self.title("team 10")
        self.resizable(False, False)

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=850)

        self.frames = {}
        for F in (Loginpage, SecretaryHomePage, ManagerHomePage, WorkerHomePage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Loginpage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


app = Application()
app.mainloop()
