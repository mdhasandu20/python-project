from tkinter import *
from PIL import ImageTk, Image
import os

def rotate_image():
    global counter
    img_label.config(image=img_arr[counter % len(img_arr)])
    counter = counter + 1

counter = 1
root = Tk()
root.title('Walpaper Viewer')
root.geometry('250x400')
root.configure(background='black')



files = os.listdir('wallpapers')

img_arr = []
for file in files:
    img = Image.open(os.path.join('wallpapers', file))
    resize_img = img.resize((200,300))
    img_arr.append(ImageTk.PhotoImage(resize_img))

img_label = Label(root, image=img_arr[0])
img_label.pack(pady=(15,10))


next_btn = Button(root, text='Next', bg='white', fg='black', width=28, height=2, command=rotate_image)
next_btn.pack()


root.mainloop()