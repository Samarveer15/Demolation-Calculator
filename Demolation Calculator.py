from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Denomination Counter')
root.configure(bg = 'light blue')
root.geometry('650x400')

upload = Image.open("app_img.jpg")

upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg = 'light blue')
label.place(x=180, y=20)

label1 = Label(root,
               text="Hey User! Welcome to
Denomination Counter Application.",
                bg='Light blue')

lbel1.p,ace(relx=0.5, y-340, anchor=CENTER)
def msg():

    MsgBox = messagebox.showinfo(
        "Alert", "do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()

button1 = Button
