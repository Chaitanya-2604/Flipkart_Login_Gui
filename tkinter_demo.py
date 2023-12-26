# import tkinter with all pakages
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

#create function for checking user data
def handle_login():
    email=email_input.get()
    password=password_input.get()
    print(email,password)

    if email == 'chaitanya@gmail.com' and password == 'chaitanya123':
        messagebox.showinfo('yayy! ','Login Successful')
    else:
        messagebox.showinfo('Error ','Login Failed')


# create object of Tk class
root=Tk()

# Enter a Title of gui
root.title('Login Form')

# Replace the icon
try:
    image = Image.open("chaitanya_black_logo.png")
    icon = ImageTk.PhotoImage(image)
    root.iconphoto(True, icon)
except Exception as e:
    print("Error setting icon:", e)

# adjust the size of login window
root.geometry('350x500')
# change background colors
root.configure(background='#0096DC')

#open flipkart image using pillow pakage
img=Image.open('flipkart-logo-39904.png')
resized_img=img.resize((70,70))
img=ImageTk.PhotoImage(resized_img)
#we use label for print image on gui
img_label=Label(root,image=img)

#use geometry manager for adjust image on gui
img_label.pack(pady=((10,10)))  # pady for adjust image vertically

text_label=Label(root,text='Flipkart',fg='white',bg='#0096DC')  #add flipkart as name below logo
text_label.pack()
text_label.config(font=('verdana',24))

#email text bar
email_label=Label(root,text='Enter Email',fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

email_input=Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

#password text bar
password_label=Label(root,text='Enter password',fg='white',bg='#0096DC')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',12))

password_input=Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

#Add login button
login_btn=Button(root,text='Login Here',bg='white',fg='black',width=20,height=2,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',10))

# mainloop() method helps to bring gui on screen
root.mainloop()

