from tkinter import *

def km_to_miles():
    km = float(km_input.get())
    miles = round(km/1.609)
    result_label.config(text=str(miles))

#Creating a new window and configurations
window = Tk()
window.title("KM to Miles Converter")
window.config(padx=20, pady=20)
window.minsize(width=200, height=100)

#Entries
km_input = Entry(width=7)
km_input.grid(column=1, row=0)

#Labels
km_label = Label(text="KM")
km_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles.")
miles_label.grid(column=2, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

#Buttons
calculate_bt = Button(text="OK", command=km_to_miles)
calculate_bt.grid(column=1, row=2)

# #Add some text to begin with
# km_input.insert(END, string="0")
# #Gets text in entry
# print(km_input.get())
# km_input.grid(row=1, column=2)


window.mainloop()