import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox


root = tk.Tk()
root.title('ACEITAS?')
root.geometry('600x600')
root.configure(background='#ffc8dd')


def move_button_1(e):
        if abs(e.x - button_1.winfo.x()) < 50 and abs(e.y - button_1.winfo()) < 40:
            x = random.randit(0, root.winfo_width() - button_1.winfo_width())
            y = random.randit(0, root.winfo_height() - button_1.winfo_height())
            button_1.place(x=x, y=y)


def accepted():
        messagebox.showinfo(
            'MEU MACAQUINHO', 'EU TE AMO, PIZZA HOJE?')


def denied():
        button_1.destroy()


margin = Canvas(root, width=500, bg= '#ffc8dd', height=100,
                    bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = Label(root, bg='#ffc8dd', text= 'QUER NAMORAR COMIGO?',
                    fg='#590d22', font=(Monsterrat, 24, 'bold'))
text_id.pack()
button_1 = tk.Button(root, text= 'NÃO', bg='#ffb3c1', command=denied,
                        relief=RIDGE, bd=3, font=('Monsterrat', 8 'bold'))
button_1.pack()
root.bind('<Motion>', move_button1)
button_2 = tk.Button(root, text='SIM', bg='#ffb3c1', relief=RIDGE,
                        bd=3, command=accepted, font=('Monsterrat', 14, bold))
button_2.pack()
    
    
root.mainloop()