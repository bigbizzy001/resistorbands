from tkinter import *
from  tkinter import messagebox
import tkinter.ttk as k
import tkinter.font as f
import ResistorCalculate as r

#color band indicators and multipliers
multiplier3ColorBand = ['Select Color', 'gold', 'silver', ]
colors = ['Select Color', 'black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'gray', 'white']
tolerance = ['Select Color', 'silver', 'gold', 'brown', 'red', 'green', 'blue', 'violet', 'no color band']




root = Tk()
root.geometry('700x300')
root.iconbitmap('marcus.ico')
root.title('RESISTOR BAND CALCULATIONS')

var = IntVar()
#method control for the radiobutton selected
def selections():
    if var.get() == 1:
        color1['value'] = tuple(colors)
        color1.current(0)

        color2['value'] = tuple(colors)
        color2.current(0)

        color3['value'] = tuple(multiplier3ColorBand)
        color3.current(0)

        color1.configure(state='readonly')
        color2.configure(state=NORMAL)
        color3.configure(state=NORMAL)
        color4.configure(state=DISABLED)
        color5.configure(state=DISABLED)
        chipTextBox.configure(state=DISABLED)
    elif var.get() == 2:
        color1['value'] = tuple(colors)
        color1.current(0)

        color2['value'] = tuple(colors)
        color2.current(0)

        color3['value'] = tuple(colors)
        color3.current(0)

        color4['value'] = tuple(tolerance)
        color4.current(0)

        color1.configure(state=NORMAL)
        color2.configure(state=NORMAL)
        color3.configure(state=NORMAL)
        color4.configure(state=NORMAL)
        color5.configure(state=DISABLED)

        chipTextBox.configure(state=DISABLED)

    elif var.get() == 3:
        color1['value'] = tuple(colors)
        color1.current(0)

        color2['value'] = tuple(colors)
        color2.current(0)

        color3['value'] = tuple(colors)
        color3.current(0)

        color4['value'] = tuple(colors)
        color4.current(0)
        color5['value'] = tuple(tolerance)
        color5.current(0)

        color1.configure(state=NORMAL)
        color2.configure(state=NORMAL)
        color3.configure(state=NORMAL)
        color4.configure(state=NORMAL)
        color5.configure(state=NORMAL)
        chipTextBox.configure(state=DISABLED)
    elif var.get() == 4:
        chipTextBox.configure(state=NORMAL)
        color1.configure(state=DISABLED)
        color2.configure(state=DISABLED)
        color3.configure(state=DISABLED)
        color4.configure(state=DISABLED)
        color5.configure(state=DISABLED)



def calculations():
    calc = r.Worker()
    try:
        if (color1.get() != colors[0] or color2.get() != colors[0] or color3.get() != colors[0] or color4.get() != colors[0]):
            if var.get() == 1:
                value = calc.three_color_band(str(color1.get()), str(color2.get()), str(color3.get()))
                answer.configure(text=value)
            elif var.get() == 2:
                value = calc.four_color_band(str(color1.get()), str(color2.get()), str(color3.get()), str(color4.get()))
                answer.configure(text=value)
            elif var.get() == 3:
                value = calc.five_color_band(str(color1.get()), str(color2.get()), str(color3.get()), str(color4.get()), str(color5.get()))
                answer.configure(text=value)
            elif var.get() == 4:
                value = calc.chip_resistors(chipTextBox.get())
                answer.configure(text=value)
    except Exception as e:
        messagebox.showinfo('IMPORTANT MESSAGE', 'Please select a color')



titleFrame = Frame(root)
font = f.Font(family='Helvetica', size=30, weight='bold')
title = Label(titleFrame, text='RESISTOR BAND CALCULATOR', font=font)
title.grid(row=0, column=0)

#radiobuttons to indicate the color bands
colorbandFrame = Frame(root)
rb3 = Radiobutton(colorbandFrame, text='3 Band',  value=1, variable=var, command=selections)
rb3.grid(row=0, column=0, padx=10, pady=10)
rb4 = Radiobutton(colorbandFrame, text='4 Band', value=2, variable=var, command=selections)
rb4.grid(row=0, column=1, padx=10, pady=10)
rb5 = Radiobutton(colorbandFrame, text='5 Band',value=3,  variable=var, command=selections)
rb5.grid(row=0, column=2, padx=10, pady=10)
rbChip = Radiobutton(colorbandFrame, text='Chip Resistors',value=4, variable=var, command=selections)
rbChip.grid(row=0, column=3, padx=10, pady=10)

#combobox to contain the colors
colorsFrame = Frame(root)
color1 = k.Combobox(colorsFrame, state='readonly', width=15, textvariable='first_color')
color1.grid(row=0, column=0, padx=10, pady=10)
color2 = k.Combobox(colorsFrame, state='readonly', width=15, textvariable='second_color')
color2.grid(row=0, column=1, padx=10, pady=10)
color3 = k.Combobox(colorsFrame, state='readonly', width=15, textvariable='third_color')
color3.grid(row=0, column=2, padx=10, pady=10)
color4 = k.Combobox(colorsFrame, state='readonly', width=15, textvariable='fourth_color')
color4.grid(row=0, column=3, padx=10, pady=10)
color5 = k.Combobox(colorsFrame, state='readonly', width=15, textvariable='fifth_color')
color5.grid(row=0, column=4, padx=10, pady=10)

#for the chip resistors
chipFrame = Frame(root)
indicator = Label(chipFrame, text='Chip selected?', underline=0)
indicator.grid(row=0, column=0, padx=5, pady=10)
chipTextBox = Entry(chipFrame)
chipTextBox.grid(row=0, column=1, pady=10)

buttonFrame = Frame(root)
calculate = Button(buttonFrame, text='Calculate', width=15, command=calculations)
calculate.grid(row=0, column=0, pady=10)

answerFrame = Frame(root)
font = f.Font(family='Helvetica', size=18, weight='bold')
answer = Label(answerFrame, font=font)
answer.grid(row=0, column=0, pady=10)

# answerLabel = Label(answerFrame)
# answerLabel.grid(row=0, column=0)

#the frame positionings
titleFrame.pack()
colorbandFrame.pack()
colorsFrame.pack()
chipFrame.pack()
buttonFrame.pack()
answerFrame.pack()

root.mainloop()
