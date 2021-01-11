# python module for one-timepad
import onetimepad

from tkinter import *

root = Tk()
root.title("CRYPTOGRAPHY")
root.geometry("800x600")


def encryptMessage():
    a = var.get()

    # inbuilt function to encrypt a message
    ct = onetimepad.encrypt(a, 'random')
    print("working",ct)
    e2.delete(0,END)
    e2.insert(END, ct)


def decryptMessage():
    a= var2.get()

    # inbuilt function to decrypt a message
    ct = onetimepad.decrypt(a, 'random')
    print("working",ct)
    e4.delete(0,END)
    e4.insert(0, ct)

label1 = Label(root, text='Plain text')
label1.grid(row=0, column=0)

label3 = Label(root, text='Encrypted text')
label3.grid(row=0, column=1)

var=StringVar()
e1 = Entry(root,textvariable=var)
e1.grid(row=0, column=1)

var2=StringVar()
e3 = Entry(root,textvariable=var2)
e3.grid(row=0, column=3)

label2 = label(root,text="Encypted Text")
label2.grid(row=0,column=1)

label4= label(root,text="Plain Text")
label4.grid(row=1,column=2)

e2 = Entry(root)
e2.grid(row=1, column=1)
e4 = Entry(root)
e4.grid(row=1, column=3)

# creating encryption button to produce the output
b1 = Button(root, text="encrypt", bg="red", fg="white", command=encryptMessage)
b1.grid(row=2, column=1)

# creating decryption button to produce the output
b2 = Button(root, text="decrypt", bg="green", fg="white", command=decryptMessage)
b2.grid(row=1, column=3)

root.mainloop()
