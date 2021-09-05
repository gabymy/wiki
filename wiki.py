import tkinter
from tkinter import*
from wikipedia import*
import wikipedia as wk

window = Tk()
window.title('Respondo a todo')
window.config(bg='black')
f1_heading = Frame(window)
f2_frame = Frame(window)
f3_result = Frame(window)

Label(f1_heading, text='Respondo a todo', font=(
    'Times', 30, 'bold'), bg='Lightgreen').pack(side=TOP)

Label(f2_frame, text='Ingresa tu duda', font=(
    'Arial', 20, 'bold'), bg='yellow').pack(side=LEFT)

Label(f3_result, text='Espero que sea de ayuda ', font=(
    'Arial', 25, 'bold'), bg='Lightpink').pack(side=LEFT)


entry_box = Entry(f2_frame, width=40, font=('Arial', 20, 'bold'))
entry_box.pack(side=LEFT, fill=BOTH, expand=5)
entry_box.focus_set()


query = ''
text = Text(window, font=('Arial', 17, 'bold'),
            bg='Lightblue', padx='55', pady=10)


def text_Search():
    global query
    query = entry_box.get()
    try:
        txt_summary = wk.summary(query)
        text.insert('1.0', txt_summary)
    except:
        text.insert('1.0', 'lo sentimos no podemos encontrar respuesta')


button1 = Button(f2_frame, text='Click', command=text_Search, font=(
    'Arial', 15, 'bold'), bg='red', fg='white')
button1.pack(side=RIGHT)

f1_heading.pack()
f2_frame.pack(side=TOP)
f3_result.pack(side=TOP, pady=20, padx=50)
text.pack()


window.mainloop()
