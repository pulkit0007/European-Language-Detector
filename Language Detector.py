from tkinter import *
import model


ld = Tk()
ld.title('Language Detector')

w = Label(ld, text="Language Detector", font=48, anchor='center')
w.grid(row=0, column=1)

w1 = Label(ld, text="", font=48)
w1.grid(row=1, column=0)


w3 = Label(ld, text="", font=48)
w3.grid(row=4, column=0)

w4 = Label(ld, text="", font=48)
w4.grid(row=6, column=0)

tex=""
en = Label(ld, text="Enter Text", width=40, padx =10, textvariable=tex)
tex = [tex]
en.grid(row=2, column=0)

def outLang():
    lang = model.predictor(tex)
    strout= lang.astype(str)
    OutputLabel = Label(ld, text= strout)
    OutputLabel.grid(row=2 ,column=2)

b = Button(ld, text='Detect Language', width=25, command=outLang)
b.grid(row=5, column=1)

e = Entry(ld , width=60)
e.grid(row=2, column=1)



ld.geometry('1280x480')
ld.resizable(True, True)

text = Text(ld, height=5, width=60)
text.insert(END,"Project By :- Pulkit Mehta \n \t      171B089")
text.grid(row=9, column=1)

ld.mainloop()
