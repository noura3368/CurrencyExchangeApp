from tkinter import *
from tkinter import ttk, StringVar, Tk
import requests



def getCurrency():
    link = 'https://api.currencyscoop.com/v1/latest?api_key=6aa4fc4694aa24c1464a2d425b13bb93'
    response = requests.get(link)
    currency = response.json()
    dic = currency["response"]["rates"]
    return dic
def widgets():
    def menubar(dictionary):
        countryList = []
        for i in dictionary:
            countryList.append(i)
        return countryList

    menu_List = OptionMenu(root, variable1, *menubar(getCurrency()))
    menu_List.place(rely= .33, relx = .85, anchor=CENTER)

    menu_List2 = OptionMenu(root, variable2, *menubar(getCurrency()))
    menu_List2.place(rely= .65, relx = .85, anchor=CENTER)

    highFrame = Frame(root, bg="#ab549e", )
    highFrame.place(relx=.5, rely=.28, anchor='n', relwidth=.4, relheight=.1)
    global entry
    entry = Entry(highFrame, bg="#9f51ae", font="calibri 20 bold", fg='white', textvariable=amount)
    entry.place(rely=.5, relx=.5, anchor=CENTER, relwidth=.9, relheight=.9)

    lowFrame = Frame(root, bg="#ab549e", )
    lowFrame.place(relx=.5, rely=.6, relwidth=.4, relheight=.1, anchor='n')
    global entrysecond
    entrysecond = Entry(lowFrame, bg="#9f51ae", font="calibri 20 bold", fg='white')
    entrysecond.place(rely=.5, relx=.5, anchor=CENTER, relwidth=.9, relheight=.9)

    Titleframe = Frame(root, bg="#22addd")
    Titleframe.place(relx=.5, rely=.1, anchor='n', relwidth=.4, relheight=.1)
    label = Label(Titleframe, text= "Currency Converter App", font="courier 10", bg="#00c8ff")
    label.place(relx=.5, rely=.23, anchor='n')

    amountLabel = Label(frame, text="Converted Amount")
    amountLabel.place(rely= .65, relx= .15, anchor=CENTER)

    amountLabel2 = Label(frame, text="Enter Amount")
    amountLabel2.place(rely=.33, relx=.15, anchor=CENTER)

root = Tk()
canvas = Canvas(root, height=400, width=500)
canvas.pack()
frame = Frame(root)
frame.place( relwidth=1, relheight=1)

backgroundImage = PhotoImage(file="IMG_0990.png")
backgroundLabel = Label(frame, image=backgroundImage)
backgroundLabel.place(relwidth=1, relheight=1)



amount = StringVar()
variable1 = StringVar()
variable1.set("From Country:")
variable2 = StringVar()
variable2.set("To Country:")
widgets()



def Converter(value):
    clear()
    try:
        var1 = variable1.get()
        var2 = variable2.get()
        money = float(value)
        if money < 1:
            entrysecond.insert(0, "Invalid Input")
        elif var1 != "USD" and var2 != "USD":
            exchange = (getCurrency()["USD"] / getCurrency()[var1]) * getCurrency()[var2]
            number = round(exchange * money, 2)
            entrysecond.insert(0, str(number))
        elif var1 == "USD" and var2 != "USD":
            exchange = (getCurrency()["USD"] * getCurrency()[var2])
            number = round(exchange * money, 2)
            entrysecond.insert(0, str(number))
        else:
            exchange = getCurrency()["USD"] /getCurrency()[var1]
            number = round(exchange * money, 2)
            entrysecond.insert(0, str(number))
    except(KeyError):
        entrysecond.insert(0, "Pick Currency")
    except(ValueError):
        entrysecond.insert(0, "Invalid Input")
def clear():
    entrysecond.delete(0, END)

def clear2():
    entry.delete(0, END)
    entrysecond.delete(0, END)
button = Button(root, text="Go!", command=lambda : Converter(entry.get()))
button.place(rely=.8, relx=.5, relwidth=.2, anchor=CENTER)

button1 = Button(root, text="Clear All", command=clear2)
button1.place(rely=.9, relx=.5, relwidth=.2, anchor=CENTER)




root.mainloop()
