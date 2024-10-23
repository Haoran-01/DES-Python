import os
import tkinter as tk
from tkinter import filedialog
from DES import *
from utils import *
from tkinter import *


# Main page GUI
def main():  # enter main
    def goto(win_num):
        # destroy main win
        root.destroy()
        if win_num == 1:
            one()  # enter win 1
        elif win_num == 2:
            two()  # enter win 2

    root = Tk()
    root.title('DES Algorithm')

    # Setting the window size
    window_width = 400
    window_height = 300

    # Get the width and length of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the x and y coordinates of the window to centre it.
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Setting the window size and position
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    label = tk.Label(root, text="DES algorithm", font=("Helvetica", 20), fg="blue")
    label.pack(pady=30, side='top')

    button1 = Button(root, text="Select file", command=lambda: goto(1), width=20, height=2)
    # enter win 1
    button1.pack(pady=40, side='bottom')

    button2 = Button(root, text="manual input", command=lambda: goto(2), width=20, height=2)
    # enter win 2
    button2.pack(pady=0, side='bottom')

    root.mainloop()


# Select the File Encryption page
def one():
    def gotomain():
        root1.destroy()  # close win 1
        main()  # enter main

    def open_key_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r", encoding='utf-8') as file:
                file_data = file.read()
                # Empty text box, Inserting file data into a text box
                text_key.delete("1.0", "end")
                text_key.insert("1.0", file_data)

    def open_text_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r", encoding='utf-8') as file:
                file_data = file.read()
                # Empty text box, Inserting file data into a text box
                text_plaintext.delete("1.0", "end")
                text_plaintext.insert("1.0", file_data)

    # Storing the ciphertext in a file
    def write_to_file(ciphertext, filename):
        subfolder_path = './text_file'

        # Full path to the created file
        file_path = os.path.join(subfolder_path, 'ciphertext.txt')

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(ciphertext)

    # Encryption Button Functions
    def encrypt_text():
        # Get the plaintext and the key
        text_data = text_plaintext.get("1.0", "end-1c")
        key_data = text_key.get("1.0", "end-1c")

        if len(text_data) == 0 or len(key_data) == 0:
            text_result.delete("1.0", "end")
            text_result.insert("1.0", "Please upload the ciphertext and key！")
        else:
            plaintexts = processing_string(text_data)
            ciphertexts = []
            for plaintext in plaintexts:
                # des encryption for each 64-bit segment
                ciphertext = encryption(plaintext, key_data)
                ciphertexts.append(ciphertext)

            ciphertext = string_transform("".join(ciphertexts))
            text_result.delete("1.0", "end")
            text_result.insert("1.0", ciphertext)
            write_to_file(ciphertext, "ciphertext.txt")

    # Decrypt Button Functions
    def decrypt_text():
        # Get the plaintext and the key
        text_data = text_plaintext.get("1.0", "end-1c")
        key_data = text_key.get("1.0", "end-1c")

        if len(text_data) == 0 or len(key_data) == 0:
            text_result.delete("1.0", "end")
            text_result.insert("1.0", "Please upload the ciphertext and key！")
        else:
            ciphertexts = processing_string(text_data)
            plaintexts = []
            for ciphertext in ciphertexts:
                # Decrypt each 64-bit fragment
                plaintext = decryption(ciphertext, key_data)
                plaintexts.append(plaintext)
            plaintexts = string_transform("".join(plaintexts))
            text_result.delete("1.0", "end")
            text_result.insert("1.0", plaintexts)

    root1 = Tk()

    # Setting the window size
    window_width = 500
    window_height = 650

    # Get the width and length of the screen
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()

    # Calculate the x and y coordinates of the window to centre it.
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Setting the window size and position
    root1.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # GUI design
    root1.title('encryption')
    Label(root1, text='Select plaintext and key file for encryption/decryption.', bg='lightgreen').pack(fill=X)

    buttwo1 = Button(root1, text="Back to main", command=gotomain)
    buttwo1.pack(pady=10, anchor='nw', padx=10)

    # Upload file options
    buttwo_upload_key = Button(root1, text="Selecting the key file", command=open_key_file)
    buttwo_upload_key.pack(pady=10, anchor='nw', padx=20)

    buttwo_upload_text = Button(root1, text="Selecting the text file", command=open_text_file)
    buttwo_upload_text.pack(pady=10, anchor='nw', padx=20)

    label1 = tk.Label(root1, text="Plain text", borderwidth=2, relief="solid")
    label1.pack(pady=10, anchor='nw', padx=20, side='top')

    # plaintext display box
    text_plaintext = tk.Text(root1, width=60, height=6)
    text_plaintext.pack()

    label2 = tk.Label(root1, text="Key", borderwidth=2, relief="solid")
    label2.pack(pady=10, anchor='nw', padx=20)

    # Key Display Box
    text_key = tk.Text(root1, width=60, height=6)
    text_key.pack()

    label3 = tk.Label(root1, text="Result", borderwidth=2, relief="solid")
    label3.pack(pady=10, anchor='nw', padx=20)

    # Results display box
    text_result = tk.Text(root1, width=60, height=6)
    text_result.pack()

    # encrypt & decrypt button
    buttwo_e = Button(root1, text="Encryption", command=encrypt_text)
    buttwo_e.pack(pady=20, anchor='sw', padx=20, side='left')

    buttwo_d = Button(root1, text="Decryption", command=decrypt_text)
    buttwo_d.pack(pady=20, anchor='se', padx=30, side='left')

    root1.mainloop()


# Manually enter the ciphertext and key page
def two():
    def gotomain():
        root2.destroy()  # close win 2
        main()  # enter main

    def encrypt_text():
        # Get the plaintext and the key
        text_data = text_plaintext.get("1.0", "end-1c")
        key_data = text_key.get("1.0", "end-1c")

        if len(text_data) == 0 or len(key_data) == 0:
            text_result.delete("1.0", "end")
            text_result.insert("1.0", "Please enter the ciphertext and key！")
        else:
            plaintexts = processing_string(text_data)
            ciphertexts = []
            for plaintext in plaintexts:
                ciphertext = encryption(plaintext, key_data)
                ciphertexts.append(ciphertext)

            ciphertext = string_transform("".join(ciphertexts))
            text_result.delete("1.0", "end")
            text_result.insert("1.0", ciphertext)

    def decrypt_text():
        # Get the plaintext and the key
        text_data = text_plaintext.get("1.0", "end-1c")
        key_data = text_key.get("1.0", "end-1c")

        if len(text_data) == 0 or len(key_data) == 0:
            text_result.delete("1.0", "end")
            text_result.insert("1.0", "Please enter the ciphertext and key！")
        else:
            ciphertexts = processing_string(text_data)
            plaintexts = []
            for ciphertext in ciphertexts:
                plaintext = decryption(ciphertext, key_data)
                plaintexts.append(plaintext)

            plaintext = string_transform("".join(plaintexts))
            text_result.delete("1.0", "end")
            text_result.insert("1.0", plaintext)

    root2 = Tk()

    # Window size and position settings
    window_width = 500
    window_height = 600

    screen_width = root2.winfo_screenwidth()
    screen_height = root2.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    root2.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Page GUI design
    root2.title('decryption')
    Label(root2, text='Input plaintext and key for encryption/decryption.', bg='lightblue').pack(fill=X)
    buttwo1 = Button(root2, text="Back to main", command=gotomain)
    buttwo1.pack(pady=10, anchor='nw', padx=10)

    label1 = tk.Label(root2, text="Plain text", borderwidth=2, relief="solid")
    label1.pack(pady=10, anchor='nw', padx=20)

    text_plaintext = tk.Text(root2, width=60, height=8)
    text_plaintext.pack()

    label2 = tk.Label(root2, text="Key", borderwidth=2, relief="solid")
    label2.pack(pady=10, anchor='nw', padx=20)

    text_key = tk.Text(root2, width=60, height=8)
    text_key.pack()

    label3 = tk.Label(root2, text="Result", borderwidth=2, relief="solid")
    label3.pack(pady=10, anchor='nw', padx=20)

    text_result = tk.Text(root2, width=60, height=8)
    text_result.pack()

    # 加密解密按钮
    buttwo_e = Button(root2, text="Encryption", command=encrypt_text)
    buttwo_e.pack(pady=20, anchor='sw', padx=20, side='left')

    buttwo_d = Button(root2, text="Decryption", command=decrypt_text)
    buttwo_d.pack(pady=20, anchor='se', padx=30, side='left')

    root2.mainloop()


if __name__ == '__main__':
    main()
