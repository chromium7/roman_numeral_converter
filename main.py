from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Roman Numerals")
root.geometry("380x200")
root.iconbitmap("spartan.ico")

#number to roman function
def number_roman(n):
    num_to_rom = {
    0: "",
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"}
    num_to_num = {
    2: [1,1],
    3: [1,1,1],
    4: [1,5],
    6: [5,1],
    7: [5,1,1],
    8: [5,1,1,1],
    9: [1,10]}
    zeros = len(str(n))-1
    str_num = [int(x) for x in str(n)]
    int_num = []
    for x in str_num:
        if x in num_to_num:
            x = num_to_num.get(x)
            y = [int(str(a) + "0"*zeros) for a in x]
            for b in y:
                int_num.append(b)
            zeros -= 1
        else:
            int_num.append(int(str(x) + "0"*zeros))
            zeros -= 1
    res = ""
    for num in int_num:
        res += num_to_rom.get(num)
    return res

#roman to number function
def roman_number(s):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            int_val += rom_val[s[i]]
    return int_val

#generate function
def generate():
    x = input_entry.get()
    if var1.get() == 1:
        if not x.isdigit():
            messagebox.showinfo("Invalid Input", "Input must be an integer")
        if int(x) <1 or int(x)>3999:
            messagebox.showinfo("Invalid Input", "Input must be between 0 and 4000")
        else:
            result = number_roman(x)
            result_label.config(text= result, font="Helvetica 18")
    if var1.get() ==2:
        try:
            result = roman_number(x.upper())
            result_label.config(text = result, font="Helvetica 18")
        except:
            messagebox.showinfo("Invalid Input", "Input must be roman number")

title = Label(root, text="Roman Number Converter", fg="Navy", font="Helvetica 24")
title.grid(row=0, column=0)

var1 = IntVar()
var1.set(1)
option1 = Radiobutton(root, text="From Number to Roman", variable = var1, value=1)
option2 = Radiobutton(root, text="From Roman to Number", variable = var1, value=2)

option1.grid(row=1,column=0, stick= W)
option2.grid(row=2, column=0, stick=W)

input_label = Label(root, text="Input number:")
input_label.grid(row=3, column=0)

input_entry = Entry(root, width=50, borderwidth=5)
input_entry.grid(row=4)

generate_btn = Button(root, text="Convert!", command = generate)
generate_btn.grid(row=5)

result_label = Label(root)
result_label.grid(row=6)

root.mainloop()

