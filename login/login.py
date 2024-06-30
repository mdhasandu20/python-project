from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()


    if email == 'mdhasan.join@gmail.com' and password == '1234':
        messagebox.showinfo('Yayyy', 'Login Successful')
    else:
        messagebox.showinfo('Error', 'Login Failed')


root = Tk()
root.title('Login Form')
root.iconbitmap('favicon.ico')

root.geometry('350x500')
root.configure(background='blue')

img = Image.open('flipkart-logo.png')
resize_img = img.resize((100,100))
img = ImageTk.PhotoImage(resize_img)

image_label = Label(root, image=img)
image_label.pack(pady=(10,10))

text_label = Label(root, text='Flipkart', fg='white',bg='blue')
text_label.pack()
text_label.config(font=('verdana', 24))


email_label = Label(root, text='Enter Email', fg='white', bg='blue')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana', 12))

email_input = Entry(root, width=50)
email_input.pack(ipady=6, pady=(1,15))

password_label = Label(root, text='Enter password', fg='white', bg='blue')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana', 12))

password_input = Entry(root, width=50)
password_input.pack(ipady=6, pady=(1,15))


login_btn = Button(root, text='Login Here', bg='white', fg='black', width=20, height=2, command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana', 10))


root.mainloop()