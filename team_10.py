import tkinter as tk
from tkinter import ttk, END, simpledialog
from tkinter import messagebox
import os
#from PIL import Image, ImageTk
import sqlite3

last_ID = 0
workers = {}
beds = {}

def update_db_of_beds(dict):
    with open("beds.txt", "w") as file:
        for key, value in dict.items():
            file.write(f"{key} : {value}\n")
    file.close()


def update_bed_dict_by_DB(dict):
    with open("beds.txt", "r") as file:
        for line in file:
            items = line.split()
            key = int(items[0])
            value = ""
            for i in range(2, len(items)):
                value += items[i] + " "
            dict[key] = value
    file.close()
    return dict


def init_dict(dict):
    if os.path.exists("beds.txt"):
        update_bed_dict_by_DB(dict)
    else:
        dict = {i: "free and clean" for i in
                range(1, 100)}  # bed status's can be "free and clean", "cleaning needed", "occupied"
    return dict


beds = init_dict(beds)

def test_is_bed_in_dict(num):
    """Test if a bed is in a dict"""
    try:
        int(num)
    except:
        return False
    if num < 1 or num > 99:
        return False
    return True

def test_if_in_pattern(str):
    return test_if_in_clean_bed_pattern(str) or test_if_in_fill_pattern(str) or test_if_in_clean_pattern(str)


def test_if_in_fill_pattern(str):
    """test if a string is in a 'fill (supplies) in (place)' pattern"""
    list_of_str = str.split()
    if list_of_str[0] == "fill":
        return True
    return False


def test_if_in_clean_bed_pattern(str):
    """test if a string is in a 'clean bed (num of bed)' pattern"""
    list_of_str = str.split()
    if list_of_str[0] == "clean" and list_of_str[1] == "bed":
        return True
    return False


def test_if_in_clean_pattern(str):
    """test if a string is in a 'clean (somewhere)' pattern"""
    list_of_str = str.split()
    if list_of_str[0] == "clean":
        return True
    return False


def test_find_bed_by_serial_num(beds, num):
    """testing finding a bed in a dict"""
    curr_status = beds[num]
    return curr_status == beds[num]



def check_if_item_exist(str,file):
    '''Ordering equipment unit test W'''
    with open(f"{file}", 'r') as f:
        item = f.read()
        if str in item:
            return True
    return False

def change_bg_color_of_inventory(dict,items,file):
    '''Lack of equipment unit test M'''
    with open(f'{file}', 'r') as f:
        item = f.read()
        for i in items:
            if i in item:
                dict[i] = "red"
    return dict

def change_availability(flag):
    '''join\out work unite test w'''
    workers[last_ID] =flag

def test_is_exist(str):
    '''add worker unite test m'''
    db = open('DataBase.txt', 'r')
    for i in db:
        arr = i.split()
        if(i!='\n'):
            if (arr[1] == str):
                db.close()
                return True
    db.close()
    return False

def login_test(username,ID,usercode,code):
    """login unite test"""
    if username==ID and usercode==code:
        return True
    else: return False

def logout():
    global last_ID
    last_ID=0

def remove_worker_from_database(id,file):
    find=False
    with open(f"{file}", "r") as f:
        lines = f.readlines()
    with open(f"{file}", "w") as f:
        for line in lines:
            if line.strip("\n").split(" ")[0] == "worker":
                if line.strip("\n").split(" ")[1] == id:
                    find=True
                if line.strip("\n").split(" ")[1] != id:
                    f.write(line)
            else:
                f.write(line)
    return find


def watch_notifications(worker_id):
    filename = f"{worker_id}_Left_notifications.txt"
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        # Open the file and read the contents
        with open(filename, "r") as file:
            details = file.read()
            file.close()
            return details
    else:
        return False

def test_Delete_worker_report(worker_id):
    filename = f"{worker_id}_report.txt"
    if os.path.exists(filename):
        # Open the file and truncate it to zero length
        with open(filename, "w") as f:
            pass
            f.close()
        return f

def test_update_manager_file(Details_report):
    with open(f"test_report.txt", "w") as file:
        # Write the report to the file
        file.write(Details_report)
    return file

def test_update_work_path(worker_id, new_work_path):
    with open(f"{worker_id}.txt", "r+") as f:
        lines = f.readlines()
        # Update the second line with the new work path
        lines[1] = f"{new_work_path}\n"
        # Write the updated lines back to the file
        f.seek(0)
        f.writelines(lines)
def test_view_notifications_deficients():
    # read the notifications from the file
    with open("test_notifications.txt", 'r') as f:
        notifications = f.readlines()[4:]  # skip the first three lines

    fill_notifications = []
    # create a list to store the lines
    for notification in notifications:
        # check if the line contains the string "clean bed"
        if "fill" in notification:
            fill_notifications.append(notification)
    return fill_notifications

def test_view_notifications_clean_place():
    # read the notifications from the file
    with open("test_notifications.txt", 'r') as f:
        notifications = f.readlines()[4:]  # skip the first three lines

    # create a list to store the lines
    clean_places_notification_list = []
    # iterate over the lines
    for notification in notifications:
        # check if the line contains the string "clean bed"
        if "clean" in notification:
            if "clean bed" in notification:
                pass
            else:
                clean_places_notification_list.append(notification)
    return clean_places_notification_list


def test_view_notifications_clean_bed():
    # read the notifications from the file
    with open("test_notifications.txt", 'r') as f:
        notifications = f.readlines()[4:]  # skip the first three lines

    # create a list to store the lines
    clean_bed_list = []
    # iterate over the lines
    for notification in notifications:
        # check if the line contains the string "clean bed"
        if "clean bed" in notification:
            # add the line to the first index of the list
            clean_bed_list.append(notification)
    return clean_bed_list


def test_show_path():
    # make list of the path
    work_path = []
    # Read the first 3 lines of the file with the same name as the user's ID
    with open("test_notifications.txt", 'r') as f:
        # Split the contents of the file by line breaks
        work_path = f.read().split('\n')[1:4]
        list_path = []

        # Iterate through the elements in work_path
        for line in work_path:
            # Split the line into separate words
            words = line.split()
            # Add the words to the list_path list
            list_path.extend(words)
    return list_path

def if_availability():
    return workers[last_ID]


def available_workers_test(id):
    with open(f'{id}.txt','r') as f:
        line=f.readline()
        line=line.split()
        name=line[3]+" "+line[4]+" ID: "+str(id)
    f.close()
    return name

#------------------------------------------------------------------------------------------------------------------------


def create_worker_dic():
    db = open('DataBase.txt', 'r')
    # [0]-type [1]-ID [2]-password [3]-name [4]-lastname
    for i in db:

        arr = i.split()
        if (i != '\n'):
            typ = arr[0]
            ID = arr[1]
            if typ=="worker":
                workers[ID]=False

def on_closing():
    global last_ID
    last_ID = 0
    app.destroy()



#-----------------------------------------------------------------------------------------------------------------------
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

                #if (username == ID and usercode == code):
                 #   Exists = True
                Exists=login_test(username,ID,usercode,code)
                if Exists==True:

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
        call_cleaner_button = tk.Button(self, text="Call Cleaner", font=("Arial", 15),
                                        command=self.call_cleaner)
        call_cleaner_button.place(x=270, y=150)

        # create a button to request refills
        self.request_refill_button = tk.Button(self, text="Request Refill", font=("Arial", 15),
                                               command=self.request_refill)
        self.request_refill_button.place(x=270, y=350)

        # create a button to see beds
        self.view_all_beds = tk.Button(self, text="View All Beds", font=("Arial", 15),
                                       command=self.view_all_beds)
        self.view_all_beds.place(x=650, y=150)

        # create a button to see beds by status
        self.view_beds_by_status_button = tk.Button(self, text="View Beds By Status", font=("Arial", 15),
                                                    command=self.view_beds_by_status)
        self.view_beds_by_status_button.place(x=650, y=250)

        # create a button to see beds by serial number
        self.view_beds_status_by_key_button = tk.Button(self, text="View Beds By Key",
                                                        font=("Arial", 15), command=self.view_beds_status_by_key)
        self.view_beds_status_by_key_button.place(x=650, y=350)

        # create a button to change the bed's status by serial number
        self.change_bed_status_button = tk.Button(self, text="Change a bed's status by key", font=("Arial", 15),
                                                  command=self.change_bed_status)
        self.change_bed_status_button.place(x=270, y=250)

    def call_cleaner(self):
        # Open a new window for the report
        report_window = tk.Toplevel(self)
        report_window.title("Cleaner Report")

        # Add a text area for the report
        report_text = tk.Text(report_window)
        report_text.insert(tk.END, "clean ")
        report_text.pack()

        # Add a submit button
        submit_button = tk.Button(report_window, text="Submit", font=("Arial", 15),
                                  command=lambda: [self.submit_report(report_text.get("1.0", 'end-1c')),report_window.destroy()])
        submit_button.pack()

    def request_refill(self):
        """This func can only accept text such as 'fill (something to fill) in (place to fill)' pattern"""
        # the things to fill are: soap, bleach, disinfectant, broom, mop, rags, tissue, masks, gloves
        # Open a new window for the refill request
        refill_request_window = tk.Toplevel(self)
        refill_request_window.title("Refill Request")

        # Opens a text area for refill request
        refill_text = tk.Text(refill_request_window)
        refill_text.insert(tk.END, "fill ")
        refill_text.pack()

        # Add a submit button to send to a worker's db.
        submit_button = tk.Button(refill_request_window, text="Submit", font=("Arial", 15),
                                  command=lambda: [self.submit_report(refill_text.get("1.0", 'end-1c')),refill_request_window.destroy()])
        submit_button.pack()

    def submit_report(self, report):
        num_of_lines = 5
        # Save the report to a text file
        worker_at_work = None
        for ID in workers:
            if workers[ID]:
                worker_at_work = ID
                break
        if worker_at_work is None:
            messagebox.showerror("Error", "There is no worker at work to send the report to.")
            return
        if test_if_in_pattern(report):
            #open the file for reading
            with open(f"{worker_at_work}.txt", "r+") as file:
                for i in range(num_of_lines):
                    file.readline()
                while file.readline() != "":
                    file.readline()
                current_position = file.tell()
                file.seek(current_position)
                file.write(report + "\n")


    def view_all_beds(self):
        # Create a new window to display the beds status
        beds_status_window = tk.Toplevel(self)
        beds_status_window.minsize(300, 300)
        beds_status_window.title("Beds Status")

        # Create a scrollable listbox to display the beds status
        listbox = tk.Listbox(beds_status_window, width=30, height=10, font=("Arial", 15))
        listbox.pack(fill='both', expand=True)
        scrollbar = tk.Scrollbar(listbox)
        scrollbar.pack(side='right', fill='y')
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        for bed, status in beds.items():
            listbox.insert("end", f"{bed} : {status}")

    def view_beds_by_status(self):
        # Create a new window to display the beds status
        beds_status_window = tk.Toplevel(self)
        beds_status_window.title("Beds By Status")

        # create an entry for the status
        status_label = tk.Label(beds_status_window, text="Enter Status:", font=("Arial", 15))
        status_label.pack()
        status_entry = tk.Entry(beds_status_window, font=("Arial", 15))
        status_entry.pack()
        submit_button = tk.Button(beds_status_window, text="Submit", font=("Arial", 15),
                                  command=lambda: self.show_beds_by_status(status_entry.get(), beds_status_window))
        submit_button.pack()

    def show_beds_by_status(self, status, beds_status_window):
        bed_list = tk.Listbox(beds_status_window, width=30, height=10, font=("Arial", 15))
        bed_list.pack()
        for bed, stat in beds.items():  # can only accept 3 types of status
            if stat == status:
                bed_list.insert("end", bed)
        if not bed_list.get(0, "end"):
            bed_list.insert("end", "No beds with this status.")

    def view_beds_status_by_key(self):
        # Create a new window to display the bed status
        bed_status_window = tk.Toplevel(self)
        bed_status_window.title("Bed Status By Serial Number")

        # Create an entry for the serial number
        serial_number_label = tk.Label(bed_status_window, text="Enter Serial Number:", font=("Arial", 15))
        serial_number_label.pack()
        serial_number_entry = tk.Entry(bed_status_window, font=("Arial", 15))
        serial_number_entry.pack()
        submit_button = tk.Button(bed_status_window, text="Submit", font=("Arial", 15),
                                  command=lambda: self.show_bed_status_by_serial_number(serial_number_entry.get(),
                                                                                        bed_status_window))
        submit_button.pack()

    def show_bed_status_by_serial_number(self, serial_number, bed_status_window):
        bed_status = beds.get(int(serial_number))
        if bed_status is None:
            status_label = tk.Label(bed_status_window, text=f"Bed with serial number {serial_number} not found.",
                                    font=("Arial", 15))
        else:
            status_label = tk.Label(bed_status_window,
                                    text=f"Bed with serial number {serial_number} status is: {bed_status}.",
                                    font=("Arial", 15))
        status_label.pack()

    def change_bed_status(self):
        # Get the serial number of the bed
        serial_number = simpledialog.askstring("Change bed status", "Enter the serial number of the bed:", parent=self)
        if int(serial_number) in beds:
            # Get the new status for the bed
            new_status = simpledialog.askstring("Change bed status",
                                                "Enter the new status for the bed (\"cleaning needed\", \"occupied\"):",
                                                parent=self)
            if new_status in ['cleaning needed', 'occupied']:
                beds[int(serial_number)] = new_status
                update_db_of_beds(beds)
                messagebox.showinfo("Change bed status",
                                    f"Bed with serial number {serial_number}'s status has been updated to {new_status}.")
                if new_status == "cleaning needed":
                    for worker_id, worker in workers.items():
                        if worker:
                            report = f'clean bed {serial_number}'
                            with open(f"{worker_id}.txt", "a") as file:
                                file.write(report)
                            file.close()
                            break
            else:
                messagebox.showerror("Change bed status", "Invalid status, please enter one of the valid statuses")
        else:
            messagebox.showerror("Change bed status", f"Bed with serial number {serial_number} not found.")


# ---------------------------------------------------------------------------------------------------------------------------

class ManagerHomePage(tk.Frame):  # מנהל

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#4f558f")
        equipment = tk.Button(self, text="Viewing Equipment Orders", font=("Arial", 16), command=self.check_supp,bg="light blue")
        equipment.place(x=100, y=380)
        Label = tk.Label(self, text="Manager", font=("Arial Bold", 30), bg="#4f558f")
        Label.place(x=310, y=80)
        log_out = tk.Button(self, text="Logout", font=("Arial", 15),
                            command=lambda: controller.show_frame(Loginpage))

        log_out.place(x=650, y=450)
        self.edit = tk.Button(self, text="Edit Workers", bg="light blue", command=self.edit_workers, width=10,font=("Arial", 16))
        self.edit.place(x=100, y=240)
        self.edit_window_is_open = False



        # Add the "Edit specific worker work-path" button
        self.edit_work_path = tk.Button(self, text="Edit Specific Worker Work-Path", bg="light blue",
                                        command=self.edit_work_path, width=30,font=("Arial", 16))
        self.edit_work_path.place(x=100, y=310)
        self.edit_work_path_window_is_open = False

        self.button3 = tk.Button(self, text='Daily Reports', bg='light green', font=('Arial Bold', 15),
                                 command=self.view_daily_report)
        self.button3.place(x=590, y=250)

        self.show_all_workers=tk.Button(self,text="View Available Workers",bg="#119981", font=('Arial Bold', 15),command=self.view_all_workers)
        self.show_all_workers.place(x=580, y=350)


    def view_all_workers(self):
        # Create a new window to display the workers
        workers_window = tk.Toplevel(self)
        workers_window.minsize(300,300)
        workers_window.title("available workers")

        # Create a scrollable listbox to display the beds status
        listbox = tk.Listbox(workers_window, width=30, height=10, font=("Arial", 15))
        listbox.pack(fill='both', expand=True)
        scrollbar = tk.Scrollbar(listbox)
        scrollbar.pack(side='right', fill='y')
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        for ID in workers.keys():
            if workers[ID]:
                name=available_workers_test(ID)
                listbox.insert("end",f"{name}")

    def view_daily_report(self):
        newWindow = tk.Toplevel(self)
        newWindow.title("Daily report")
        newWindow.configure(bg="#002955")
        newWindow.geometry("400x400")
        newWindow.resizable(True, True)
        # ID Entry field
        id_label = tk.Label(newWindow, text="ID:", bg="bisque")
        id_entry = tk.Entry(newWindow)
        id_label.pack(side="left", padx=10, pady=10)
        id_entry.pack(side="left", padx=10, pady=10)

        # Create a frame to hold the buttons
        button_frame = tk.Frame(newWindow)
        button_frame.config(bg="#00294b")
        button_frame.pack(side="left", padx=10, pady=10)

        # Enter button
        enter_button = tk.Button(button_frame, text="Watch Report", command=lambda: self.display_report_window(id_entry.get()))
        enter_button.pack(side="top", padx=10, pady=10)

        # Delete report Button
        delete_button = tk.Button(button_frame, text="Delete report",
                                  command=lambda: self.Delete_worker_report(id_entry.get()))
        delete_button.pack(side="top", padx=10, pady=10)

        # View Open Calls Notifications
        notifications_button = tk.Button(button_frame, text="Watch Open Notifications",
                                         command=lambda: self.watch_notifications(id_entry.get()))
        notifications_button.pack(side="top", padx=10, pady=20)

        # Exit button
        exit_button = tk.Button(button_frame, text="Exit", command=newWindow.destroy)
        exit_button.pack(side="top", padx=10, pady=10)


    def watch_notifications(self,worker_id):
        filename = f"{worker_id}_Left_notifications.txt"
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            # Open the file and read the contents
            with open(filename, "r") as file:
                details = file.read()

            # Create the window and a scrollable frame
            window = tk.Toplevel(self)
            window.title(f"Open notifications for Worker ID: {worker_id}")
            frame = tk.Frame(window)
            frame.pack()

            # Add a scrollbar to the frame
            scrollbar = tk.Scrollbar(frame)
            scrollbar.pack(side="right", fill="y")

            # Add a Text widget to the frame and set it to display the report details
            text = tk.Text(frame, yscrollcommand=scrollbar.set)
            text.pack()
            text.insert("1.0", details)

            # Set the scrollbar to control the Text widget
            scrollbar.config(command=text.yview)
            file.close()
        else:
            messagebox.showerror(f"{worker_id} Error",
                                 f"{worker_id} didnt send daily report or your already deleted it.")

    def Delete_worker_report(self,worker_id):
        if messagebox.askyesno("Security question", "By clicking on the Delete button you accept to remove the details"):
            # Construct the filename for the worker's report
            filename = f"{worker_id}_report.txt"
            if os.path.exists(filename):
                # Open the file and truncate it to zero length
                with open(filename, "w") as f:
                    pass
                    f.close()
                messagebox.showinfo("Deleted",f"Deleted report for Worker ID: {worker_id}")


    def display_report_window(self, worker_id):
        filename = f"{worker_id}_report.txt"
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            # Open the file and read the contents
            with open(filename, "r") as file:
                details = file.read()

            # Create the window and a scrollable frame
            window = tk.Toplevel(self)
            window.title(f"Report for Worker ID: {worker_id}")
            frame = tk.Frame(window)
            frame.pack()


            # Add a scrollbar to the frame
            scrollbar = tk.Scrollbar(frame)
            scrollbar.pack(side="right", fill="y")

            # Add a Text widget to the frame and set it to display the report details
            text = tk.Text(frame, yscrollcommand=scrollbar.set)
            text.pack()
            text.insert("1.0", details)

            # Set the scrollbar to control the Text widget
            scrollbar.config(command=text.yview)

            # Close the window when the "x" button is clicked
            window.protocol("WM_DELETE_WINDOW", window.destroy)
            file.close()
        else:
            messagebox.showerror(f"{worker_id} Error",f"{worker_id} didnt send daily report or your already deleted it.")

    def edit_work_path(self):
        # Open a new window if it is not already open
        if (self.edit_work_path_window_is_open == False):

            def on_closing():
                self.edit_work_path_window_is_open = False
                newWindow.destroy()

            self.edit_work_path_window_is_open = True
            newWindow = tk.Toplevel(self)
            newWindow.title("Edit specific worker work-path")
            newWindow.configure(bg="bisque")
            newWindow.geometry("400x320")
            newWindow.resizable(False, False)

            # Add a label and entry for the worker's ID
            LID = tk.Label(newWindow, text="ID", bg="bisque")
            ID = tk.Entry(newWindow, width=30)
            LID.place(x=20, y=40)
            ID.place(x=120, y=40)

            # Add a label and entry for the new work path
            work_path = tk.Text(newWindow, width=60, height=6, font=("Arial Bold", 13))
            work_path.place(x=2, y=100)
            # Add a button to submit the new work path
            submit_button = tk.Button(newWindow, text="Send", bg="light blue", font=("Arial Bold", 20),
                                      command=lambda:[self.update_work_path(ID.get(), work_path.get("1.0", "end")), ID.delete(0,END),work_path.delete('1.0',END)])
            submit_button.pack(side="bottom", pady=45)
            submit_button.configure(height=1, width=15)

            # add an Exit button to close the window
            exit_button = tk.Button(newWindow, text="Exit", command=on_closing)

            # Get the width of the window and the required width of the Exit button
            window_width = newWindow.winfo_width()
            exit_button_width = exit_button.winfo_reqwidth()

            # Place the Exit button at the right edge of the window, with a small margin
            exit_button.place(x=350, y=280)

            # Close the window when the "x" button is clicked
            newWindow.protocol("WM_DELETE_WINDOW", on_closing)


    def update_work_path(self, worker_id, new_work_path):
        if tk.messagebox.askyesno("Question", f"By clicking yes the {worker_id} work path will change") == True:
            # Open the worker's id.txt file and update the first line with the new work path
            with open(f"{worker_id}.txt", "r+") as f:
                lines = f.readlines()
                if '\n' not in lines[0]:
                    lines[0] += '\n'
                while len(lines) < 4:
                    lines.append('\n')
                # Update the second line with the new work path
                lines[1] = str(new_work_path)
                # Write the updated lines back to the file
                f.seek(0)
                f.writelines(lines)
                f.close()




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
                    id=tk.Label(removeWindow,text="ID of the worker",bg="bisque")
                    id.place(x=60,y=80)
                    IDentry=tk.Entry(removeWindow)
                    IDentry.place(x=160,y=80,width=155)
                    def remove():
                        if tk.messagebox.askyesno("Question", "are you sure you want to remove this worker?") == True:
                            id_to_remove = IDentry.get()
                            IDentry.delete(0,END)
                            find_worker=remove_worker_from_database(id_to_remove,"DataBase.txt")
                            removeWindow.destroy()
                            self.edit_window_is_open = False
                            remove_window_is_open=False
                            newWindow.destroy()
                            if find_worker==True:
                                tk.messagebox.showinfo("worker removed","The employee has been removed!")
                                workers.pop(id_to_remove)
                                os.remove(f"{id_to_remove}.txt")
                                os.remove(f'{id_to_remove}_Left_notifications.txt')
                                os.remove(f'{id_to_remove}_report.txt')

                            else:
                                tk.messagebox.showerror("eroor","The employee does not exist!")

                    remove=tk.Button(removeWindow,text="remove",bg="#900001",command=remove)
                    remove.place(x=200,y=200)




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
                            new_worker = open(f'{ID.get()}.txt', 'w')
                            new_worker.write(string+"\n")
                            new_worker.close()
                            Left_notifications=open(f'{ID.get()}_Left_notifications.txt','w')
                            Left_notifications.close()
                            report=open(f'{ID.get()}_report.txt','w')
                            report.close()
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
        directive = tk.Label(master, text='red-need to order\ngreen-in stock', bg="light blue", font=("Arial", 8)).place(x=160, y=400)

        def confrim():
            if tk.messagebox.askyesno("Question", "With your approval, the requests will be deleted") == True:
                open('choices.txt', 'w').close()
                master.destroy()


        confrim = tk.Button(master, text="Confirmation", command=confrim).grid(row=9, rowspan=13)


# ---------------------------------------------------------------------------------------------------------------------------------------------

class WorkerHomePage(tk.Frame):  # עובד ניקיון



    def join_out_work(self):

        if (self.present['text'] == "Enter Work"):
            self.present.configure(bg="red", text="Leave a shift")
            f = open(f'{last_ID}.txt', 'r')
            line=f.readline()
            line=line.split()
            name=line[4]+" "+line[3]
            f.close()
            self.label_name.configure(text=f"Hello {name}",font=("Arial Bold", 25))
            change_availability(True)

        elif (self.present['text'] == "Leave a shift"):
            if self.daily_report == False:
                tk.messagebox.showinfo(title="report not enterd",message="Please fill your daily report before leaving")
            else:
                self.present.configure(bg="green", text="Enter Work")
                self.label_name.configure(text="Hello",font=("Arial Bold", 25))
                change_availability(False)


    def clean(self):
        self.present.configure(bg="green", text="Enter Work")
        self.label_name.configure(text="Hello",font=("Arial Bold", 25))

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
        self.lorder = tk.Button(self, text="Order Supplies", font=("Arial Bold", 15), bg="yellow",
                                command=self.order_supp)
        self.lorder.place(x=350, y=380)
        self.label_name = tk.Label(self, text="Hello ", font=("Arial Bold", 25), bg="#4f558f")
        self.label_name.place(x=80, y=150)
        self.configure(bg="#4f558f")
        Label = tk.Label(self, text="Worker Home Page", font=("Arial Bold", 30), bg="#4f558f")
        Label.place(x=270, y=80)
        self.daily_report = False

        button = tk.Button(self, text="Logout", font=("Arial", 15),
                           command=lambda: [self.clean(), logout(),controller.show_frame(Loginpage),self.daily_report_reset()])
        button.place(x=750, y=450)
        self.present = tk.Button(self, text="Enter Work", bg="green", command=self.join_out_work, width=10)
        self.present.place(x=80, y=200)
        self.button1 = tk.Button(self, text="Worker Work Path", font=("Arial", 15), command=self.show_path)
        self.button1.place(x=100, y=380)
        # create a button to view notifications
        self.button2 = tk.Button(self, text='Clean Beds Notifications', bg='#ff3333', font=('Arial Bold', 15),width=23,
                                 command=self.view_notifications_clean_bed)
        self.button2.place(x=300, y=210)
        self.button3 = tk.Button(self, text='Clean Places Notifications', bg='#905fa2', font=('Arial Bold', 15),width=23 ,
                                 command=self.view_notifications_clean_place)
        self.button3.place(x=300, y=250)
        self.button4 = tk.Button(self, text='Notifications of Deficiencies', bg='#d48f7c', font=('Arial Bold', 15),width=23,
                                 command=self.view_notifications_deficients)
        self.button4.place(x=300, y=290)
        self.daily_report_button = tk.Button(self, text='Send Daily Report', font=('Arial Bold', 15),
                                             command=self.send_daily_report)
        self.daily_report_button.place(x=550, y=380)

    def daily_report_reset(self):
        self.daily_report = False

        # display the option of the report

    def send_daily_report(self):
        if if_availability() == 0:
            # Show an error message
            messagebox.showerror("Error", "Please enter work first")
            return
        if (self.daily_report == False):
            newWindow = tk.Toplevel(self)
            newWindow.title(f"Daily report of {last_ID}")
            newWindow.configure(bg="bisque")
            newWindow.geometry("550x500")
            newWindow.resizable(False, False)

            # Add a label and entry for the worker's ID
            L_Enter = tk.Label(newWindow, text='Enter your report ' + str(last_ID) + ':', bg="bisque",
                               font=("Arial Bold", 20))
            L_Enter.place(x=120, y=0)
            Detials_report = tk.Text(newWindow, width=60, height=20, font=("Arial Bold", 13))
            Detials_report.place(x=2, y=40)
            # Add a button to submit the new work path
            submit_button = tk.Button(newWindow, text="Send", bg="light blue", font=("Arial Bold", 20),
                                      command=lambda: update_manager_file(Detials_report.get("1.0", "end")))
            submit_button.pack(side="bottom", pady=20)
            submit_button.configure(height=1, width=20)

        def update_manager_file(Details_report):
            if tk.messagebox.askyesno("Confirm", "By clicking on the send button you confirm to send the details"):
                self.daily_report = True
                # Open the file in write mode
                with open(f"{last_ID}_report.txt", "w") as file:
                    # Write the report to the file
                    file.write(str(Details_report))
                    file.close()
                with open(f"{last_ID}.txt", "r") as f:
                    lines = f.readlines()
                    f.close()

                with open(f"{last_ID}.txt", "w") as f:
                    f.writelines(lines[:4])
                    f.close()

                with open(f"{last_ID}_Left_notifications.txt", "w") as notFile:
                    notFile.writelines(lines[4:])
                    notFile.close()

                newWindow.destroy()

        # display the work path of the worker

        # display the work path of the worker
    def show_path(self):
        global last_ID
        if if_availability() == 0:
        # Show an error message
           messagebox.showerror("Enter Work Error", "Please enter work first")
           return

         # make list of the path
        work_path = []
            # Read the first 3 lines of the file with the same name as the user's ID
        with open(str(last_ID) + '.txt', 'r') as f:
            # Split the contents of the file by line breaks
            f.seek(2)

            work_path = []
            work_path.append(f.readline())
            work_path.append(f.readline())
            work_path.append(f.readline())
            work_path.append(f.readline())
            work_path.pop(0)
            list_path = []

                # Iterate through the elements in work_path
            for line in work_path:
                 # Split the line into separate words
                words = line.split()
                # Add the words to the list_path list
                list_path.extend(words)

            # Show the work path to the user
        addWindow = tk.Toplevel(self)
        addWindow.title("Work Path")
        addWindow.configure(bg="bisque")
        addWindow.geometry("400x390")
        addWindow.resizable(False, False)

        buttons = {}

        def mark_as_finished(word):
            buttons[word]['bg'] = 'lightgreen'
            buttons[word]['activebackground'] = 'lightgreen'
            buttons[word]['text'] = f"{word} (Done)"

            # Iterate through the elements in list_path
        i = 1
        for word in list_path:
            # Create a label with the text from list_path
            # create a button for each path and store a reference in the dictionary
            button = tk.Button(addWindow, text=f"{i}. {word}", command=lambda n=word: mark_as_finished(n))
            buttons[word] = button
            button.pack()
            i += 1
        f.close()
        # Create a button to return to the previous state
        back_button = tk.Button(addWindow, text="Back", font=("Helvetica", 20, "bold"), width=10,
                                command=addWindow.destroy)
        # Pack the button to display it on the very bottom and right side of the window
        back_button.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10)

    def confirm_request(self):
        # Ask the user to confirm the request
        result = messagebox.askyesno("Confirm Request", "Are you sure you want to confirm this request?")
        if result:
            # Close the notification window
            self.window.destroy()
            # Create a button on the home page to indicate that the bed is ready
            self.bed_ready_button = tk.Button(self, text="Click here when the bed is ready", bg="red",
                                              command=self.bed_ready)
            self.bed_ready_button.place(x=100, y=350)
            # Disable all other buttons on the home page
            self.lorder.config(state=tk.DISABLED)
            self.present.config(state=tk.DISABLED)
            self.button1.config(state=tk.DISABLED)
            self.button2.config(state=tk.DISABLED)
            self.button3.config(state=tk.DISABLED)
            self.button4.config(state=tk.DISABLED)
            self.daily_report_button.config(state=tk.DISABLED)
        return result

    def bed_ready(self, notification):
        # Ask the user to confirm the request
        result = messagebox.askyesno("Mark As Ready", "Are you sure you want to mark this bed as ready?")
        if result:
            # remove the notification from the file
            with open(f"{last_ID}.txt", 'r') as f:
                notifications = f.readlines()
                f.close()
            notifications = [n for n in notifications if n != notification]
            with open(f"{last_ID}.txt", 'w') as f:
                f.writelines(notifications)
            # Enable all buttons on the home page again
            self.lorder.config(state=tk.NORMAL)
            self.present.config(state=tk.NORMAL)
            self.button1.config(state=tk.NORMAL)
            self.button2.config(state=tk.NORMAL)
            self.button3.config(state=tk.NORMAL)
            self.button4.config(state=tk.NORMAL)
            self.daily_report_button.config(state=tk.NORMAL)
            # Remove the "bed ready" button
            self.bed_ready_button.destroy()
            f.close()
            notification=notification.split()
            for word in notification:
                try:
                    word = int(word)

                    with open("beds.txt", "r+") as beds_file:
                        beds_list = beds_file.readlines()
                        beds_list[word - 1] = str(word) + ' : free and clean\n'
                        beds_file.close()
                        with open("beds.txt", "w") as beds_file:
                            beds_file.writelines(beds_list)
                            beds_file.close()
                            beds[word]="free and clean"
                            break
                except: pass

    def view_notifications_clean_bed(self):
        if if_availability() == 0:
            # Show an error message
            messagebox.showerror("Error", "Please enter work first")
            return

        """Opens a new window with a list of all notifications in the file"""
        # create the new window
        self.window = tk.Toplevel(self)
        self.window.title("Clean Bed Notifications")
        self.window.geometry("350x350")  # set the window size to 350x350 pixels
        self.window.withdraw()  # hide the window
        self.window.deiconify()  # show the window again
        self.window.geometry("+700+100")  # open the window 700 pixels to
        # the right and 100 pixels down from the top-left corner of the screen

        # create a dictionary to store references to the buttons
        buttons = {}

        # create a function to mark a notification as verified
        def mark_as_verified(notification):
            # Disable all the buttons if the user click yes.
            result = messagebox.askyesno("Confirm Request", "Are you sure you want to confirm this request?")
            try:
                if result:
                    # Close the notification window
                    self.window.destroy()
                    # Create a button on the home page to indicate that the bed is ready
                    self.bed_ready_button = tk.Button(self, text="Click here when the bed is ready", bg="red",
                                                      command=lambda: self.bed_ready(notification))
                    self.bed_ready_button.place(x=100, y=350)
                    # Disable all other buttons on the home page
                    self.lorder.config(state=tk.DISABLED)
                    self.present.config(state=tk.DISABLED)
                    self.button1.config(state=tk.DISABLED)
                    self.button2.config(state=tk.DISABLED)
                    self.button3.config(state=tk.DISABLED)
                    self.button4.config(state=tk.DISABLED)
                    self.daily_report_button.config(state=tk.DISABLED)
                    # update the appearance of the button
                    buttons[notification]['bg'] = 'lightgreen'
                    buttons[notification]['activebackground'] = 'lightgreen'
                    buttons[notification]['text'] = f"{notification} (Accepted)"
            except:
                pass

        # read the notifications from the file
        with open(f"{last_ID}.txt", 'r') as f:
            notifications = f.readlines()[4:]  # skip the first three lines
            f.close()

        # create a list to store the lines
        clean_bed_list = []
        # iterate over the lines
        for notification in notifications:
            # check if the line contains the string "clean bed"
            if "clean bed" in notification:
                # add the line to the first index of the list
                clean_bed_list.append(notification)

        # display the notifications in the new window
        for notification in clean_bed_list:
            # create a button for each notification and store a reference in the dictionary
            button = tk.Button(self.window, text=notification, bg="red",
                               command=lambda n=notification: mark_as_verified(n))
            buttons[notification] = button
            button.pack()

        # add an Exit button to close the window
        tk.Button(self.window, text="Exit", command=self.window.destroy).pack()

    def view_notifications_clean_place(self):
        if if_availability() == 0:
            # Show an error message
            messagebox.showerror("Error", "Please enter work first")
            return

        """Opens a new window with a list of all notifications in the file"""
        # create the new window
        window = tk.Toplevel(self)
        window.title("Clean Place Notifications")
        window.geometry("350x350")  # set the window size to 800x500 pixels
        window.withdraw()  # hide the window
        window.deiconify()  # show the window again
        window.geometry("+700+100")  # open the window 700 pixels to
        # the right and 100 pixels down from the top-left corner of the screen

        # create a dictionary to store references to the buttons
        buttons = {}

        # create a function to mark a notification as verified
        def mark_as_verified(notification):
            # update the appearance of the button
            buttons[notification]['bg'] = 'lightgreen'
            buttons[notification]['activebackground'] = 'lightgreen'
            buttons[notification]['text'] = f"{notification} (Accepted)"
            # remove the notification from the file
            with open(f"{last_ID}.txt", 'r') as f:
                notifications = f.readlines()
                f.close()
            notifications = [n for n in notifications if n != notification]
            with open(f"{last_ID}.txt", 'w') as f:
                f.writelines(notifications)
                f.close()

        # read the notifications from the file
        with open(f"{last_ID}.txt", 'r') as f:
            notifications = f.readlines()[4:]  # skip the first three lines
            f.close()

        # create a list to store the lines
        clean_places_notification_list = []
        # iterate over the lines
        for notification in notifications:
            # check if the line contains the string "clean bed"
            if "clean" in notification:
                if "clean bed" in notification:
                    pass
                else:
                    clean_places_notification_list.append(notification)

        # display the notifications in the new window
        for notification in clean_places_notification_list:
            # create a button for each notification and store a reference in the dictionary
            button = tk.Button(window, text=notification, command=lambda n=notification: mark_as_verified(n))
            buttons[notification] = button
            button.pack()
        # add an Exit button to close the window
        tk.Button(window, text="Exit", command=window.destroy).pack()

    def view_notifications_deficients(self):
        if if_availability() == 0:
            # Show an error message
            messagebox.showerror("Error", "Please enter work first")
            return

        """Opens a new window with a list of all notifications in the file"""
        # create the new window
        window = tk.Toplevel(self)
        window.title("Notifications")
        window.geometry("350x350")  # set the window size to 800x500 pixels
        window.withdraw()  # hide the window
        window.deiconify()  # show the window again
        window.geometry("+700+100")  # open the window 700 pixels to
        # the right and 100 pixels down from the top-left corner of the screen

        # create a dictionary to store references to the buttons
        buttons = {}

        # create a function to mark a notification as verified
        def mark_as_verified(notification):
            # update the appearance of the button
            buttons[notification]['bg'] = 'lightgreen'
            buttons[notification]['activebackground'] = 'lightgreen'
            buttons[notification]['text'] = f"{notification} (Accepted)"
            # remove the notification from the file
            with open(f"{last_ID}.txt", 'r') as f:
                notifications = f.readlines()
                f.close()
            notifications = [n for n in notifications if n != notification]
            with open(f"{last_ID}.txt", 'w') as f:
                f.writelines(notifications)
                f.close()

        # read the notifications from the file
        with open(f"{last_ID}.txt", 'r') as f:
            notifications = f.readlines()[4:]  # skip the first three lines
            f.close()

        fill_notifications = []
        # create a list to store the lines
        for notification in notifications:
            # check if the line contains the string "clean bed"
            if "fill" in notification:
                fill_notifications.append(notification)

        # display the notifications in the new window
        for notification in fill_notifications:
            # create a button for each notification and store a reference in the dictionary
            button = tk.Button(window, text=notification, bg="light blue",command=lambda n=notification: mark_as_verified(n))
            buttons[notification] = button
            button.pack()
        # add an Exit button to close the window
        tk.Button(window, text="Exit", command=window.destroy).pack()




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

create_worker_dic()
app = Application()
app.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()

