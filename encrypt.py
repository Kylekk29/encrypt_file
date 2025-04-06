from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog
import os
from tkinter import messagebox
def load_file():
    global opened_file_path
    global opened_file_type
    opened_file_path = filedialog.askopenfilename(filetypes=[('All file','*.*')],title='load file')
    opened_file_info = os.path.splitext(os.path.basename(opened_file_path))
    opened_file_name = opened_file_info[0]
    opened_file_type = opened_file_info[1]
    opened_file_load_label = tk.Label(win, text=opened_file_name, bg="white", fg="black", font=("Arial", 16))
    opened_file_load_label.place(x=200, y=5, width=400, height=50)

def load_key():
    global opened_key_path
    global key
    opened_key_path = filedialog.askopenfilename(filetypes=[('Key file','*.key*')],title='load key')
    opened_key_show_info = os.path.splitext(os.path.basename(opened_key_path))[0]
    opened_key_load_label = tk.Label(win, text=opened_key_show_info, bg="white", fg="black", font=("Arial", 16))
    opened_key_load_label.place(x=200, y=60, width=400, height=50)    
    with open(opened_key_path,'rb') as loaded_key:
        key = loaded_key.read()

def generate_key():
    global key_path
    key_path = filedialog.asksaveasfilename(defaultextension=".key", filetypes=[("Key files", "*.key")],title='Generate_Key', initialfile='NewKey')
    if key_path:
        with open(key_path, "wb") as key_file:
            key = Fernet.generate_key()
            key_file.write(key)
        messagebox.showinfo("Key Path", f"Key file path: {key_path}", )

def encrypt_file():
    f=Fernet(key)
    with open(opened_file_path,'rb') as original_file:
        encrypted = f.encrypt(original_file.read())
    save_path = filedialog.asksaveasfilename(defaultextension=opened_file_type, filetypes=[("All files","*.*")]
                                             ,initialfile='encrypted_file',initialdir=opened_file_path)
    with open(save_path,'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt_file():
    f=Fernet(key)
    with open(opened_file_path,'rb') as original_file:
        decrypted = f.decrypt(original_file.read())
    try:
        save_path = filedialog.asksaveasfilename(defaultextension=opened_file_type, filetypes=[("All files","*.*")]
                                                 ,initialfile='decrypt_file',initialdir=opened_file_path)
        with open(save_path,'wb') as decrypted_file:
            decrypted_file.write(decrypted)
    except:
        print('error')

win = tk.Tk()
win.config(bg="white")
win.resizable(False, False)
win.title("Encryptor")
win.geometry("600x500")
load_file_load_button = tk.Button(win, text="Load File",command=load_file
                                    ,bg="#4CAF50", fg="black", font=("Arial", 16))
load_file_load_button.place(x=30, y=5, width=150, height=50)
load_key_button = tk.Button(win, text="Load Key",command=load_key
                                    ,bg="yellow", fg="black", font=("Arial", 16))
load_key_button.place(x=30, y=60, width=150, height=50)
generate_key_button = tk.Button(win, text="Generate Key",command=generate_key
                                    ,bg="yellow", fg="black", font=("Arial", 16))
generate_key_button.place(x=30, y=115, width=150, height=50)
encrypt_file_button = tk.Button(win, text="encrypt file",command=encrypt_file
                                    ,bg="yellow", fg="black", font=("Arial", 16))
encrypt_file_button.place(x=30, y=170, width=150, height=50)
decrypt_file_button = tk.Button(win,text="decrypt file",command=decrypt_file
                                    ,bg="yellow", fg="black", font=("Arial", 16))
decrypt_file_button.place(x=30,y=225,width=150,height=50)

win.mainloop()
