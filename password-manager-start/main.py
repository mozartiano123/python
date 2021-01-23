from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import choice, randint
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_list = [letters,numbers,symbols]
mail_list = ["@gmail.com","@msn.com","@br.ibm.com","@yandex.com"]

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    if len(password_ent.get()) > 0:
        password_ent.delete(0,END)
    gen_password = choice(letters)
    for i in range(0,14):
        j = randint(0,2)
        gen_password += (choice(password_list[j]))
    password_ent.insert(0,gen_password)
    pyperclip.copy(gen_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_to_file(a_json_dict):
    with open("data.json", "w") as data_file:
        json.dump(a_json_dict, data_file, indent=4)

def read_file():
    with open("data.json", "r") as data_file:
        return json.load(data_file)

def save_password():
    website = website_ent.get().upper()
    username = username_ent.get() + mail_combo.get()
    password = password_ent.get()
    new_data = {
        website:{
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(username_ent.get()) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please don't leave any field unfilled.")
    else:
        # if messagebox.askokcancel(title="Confirmation", message="Do you want to go on with the following"
        #                                                      " information ?\n"
        #                                                      f"website:  {website}\n"
        #                                                      f"username: {username}\n"
        #                                                      f"password: {password}"):
        #Try to open an existing file to read the json.
        #File may not exist already.
        try:
            data = read_file()
        except FileNotFoundError:
            #if file does not exist, then create it and write new_data(dict) to the file
            write_to_file(new_data)
        else:
            #If file exists and was open and read on the try block, without error.
            #Update the data(dictionary) with the new info and save it to json file.
            data.update(new_data)
            write_to_file(data)
        finally:
            #clean screen up.
            website_ent.delete(0,END)
            password_ent.delete(0,END)
            generate_password()

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    try:
        data = read_file()
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        to_search = website_ent.get().upper()
        if to_search in data:
            # # search_dict = {key:val for (key,val) in data.items() if key == to_search}
            # username = search_dict[to_search]["username"]
            # password = search_dict[to_search]["password"]
            username = data[to_search]["username"]
            password = data[to_search]["password"]
            username_ent.delete(0,END)
            password_ent.delete(0,END)
            username_ent.insert(0,username)
            password_ent.insert(0,password)
            pyperclip.copy(password)
            messagebox.showinfo(title=to_search, message="Password retrieved successfully.\n\n"
                                                         f"username: {username}\n"
                                                         f"password: {password}")
        else:
            messagebox.showinfo(title="Search Results", message="Record not found.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pass Manager")
window.config(padx=25,pady=25)
window.focus()

#Canvas
canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

#Labels
website_lbl = Label(text="Website:", fg="Black", font=("Arial",10))
website_lbl.grid(column=0,row=1)

username_lbl = Label(text="Email/Username:", fg="Black", font=("Arial",10))
username_lbl.grid(column=0,row=2)

password_lbl = Label(text="Password:", fg="Black", font=("Arial",10))
password_lbl.grid(column=0,row=3)

#Entries
website_ent = Entry(width=35)
website_ent.grid(column=1,row=1)
website_ent.focus()

username_ent = Entry(width=35)
username_ent.grid(column=1,row=2)
# username_ent.grid(column=1,row=2, columnspan=2)
username_ent.insert(0,"mozartiano123")

password_ent = Entry(width=35)
password_ent.grid(column=1,row=3)

#Combobox
mail_combo = ttk.Combobox(values=mail_list)
mail_combo.current(0)
mail_combo.grid(column=2,row=2, padx=10)

#Buttons
search_bt = Button(text="Search", width=15, command=search_password)
search_bt.grid(column=2,row=1, pady=5)

gen_pass_bt = Button(text="Generate Password", command=generate_password)
gen_pass_bt.grid(column=2,row=3, pady=5)

add_pass_bt = Button(text="Add", width=36, command=save_password)
add_pass_bt.grid(column=1,row=4, columnspan=2, pady=5)

generate_password()

window.mainloop()