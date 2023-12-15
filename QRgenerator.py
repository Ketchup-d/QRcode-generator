from qrcode import QRCode
import tkinter as tk
from tkinter import font
from tkinter import messagebox
import os

if __name__ == "__main__":
    print(">> welcome to QRcode generator v1.1, developed by: Artin (Ketchup d) <<")

path = "Qrcode"
isExist = os.path.exists(path)
if not isExist:
    os.makedirs(path)


def ofl(a=1):
    os.startfile("Qrcode")


def show_msg():
    msg = tk.Label(frame_message, text="Please enter a text/URL first",
                   font=font_xsmall, bg="#1A1A1A", fg="#C0C0C0")
    msg.pack(pady=28)
    window.after(3000, msg.destroy)
    msg = False


def show_msgbox():
    messagebox.showinfo(
        "Done", "QRcode has been saved as an image in the 'Qrcode' folder in the application directory.")


def qrcode():
    global msg

    if msg != 0:
        msg.destroy()
        msg = 0

    data = entry.get()
    if len(data) > 0:
        qr = QRCode(version=1, box_size=10, border=3)
        qr.add_data(data)
        img = qr.make_image(fill_color="black", back_color="white")
        if len(entryname.get()) >= 1:
            img.save(f"Qrcode\\{entryname.get()}.png")
        else:
            img.save("Qrcode\\qrcode.png")
        show_msgbox()
    else:
        show_msg()


msg = False

window = tk.Tk()
window.title("QRcode generator")
window.geometry("510x470")
window.config(bg="#1A1A1A")
window.resizable(False, False)

labelcopyright = tk.Label(text="© 2023 - QRgenerator",
                          bg="#1A1A1A", fg="#949494").pack(side="bottom")

photo = tk.PhotoImage(
    file="models\\qrcodeicon.png")
window.iconphoto(False, photo)

menubar = tk.Menu(window, background="black", fg="white")

file = tk.Menu(menubar, tearoff=False)

file.add_command(label="Open files locations",
                 command=ofl, accelerator="Ctrl+F")
file.add_command(label="Close", command=window.quit, accelerator="Alt+F4")

menubar.add_cascade(label="File", menu=file)

frame_url = tk.Frame(window, bg="#1A1A1A")
frame_url.pack(pady=40)

frame_name = tk.Frame(window, bg="#1A1A1A")
frame_name.pack()

frame_button = tk.Label(window, bg="#1A1A1A")
frame_button.pack(pady=30)

frame_message = tk.Label(window, bg="#1A1A1A")
frame_message.pack(side="bottom")

font_medium = font.Font(size=14)
font_small = font.Font(size=12)
font_xsmall = font.Font(size=10)

label = tk.Label(frame_url, text="Enter the text/URL you want to get as an QRcode:",
                 font=font_medium, bg="#1A1A1A", fg="white")
label.pack()

entry = tk.Entry(frame_url, width=45, font=font_small,
                 bg="#212121", fg="white")
entry.pack(pady=15)

labelname = tk.Label(frame_name, text="Save as (file name):",
                     font=font_medium, bg="#1A1A1A", fg="white")
labelname.pack()
label_optinal = tk.Label(frame_name, bg="#1A1A1A",
                         fg="#f0f0f0", text="(Optional)", font=font_xsmall)
label_optinal.pack()

entryname = tk.Entry(frame_name, width=25, font=font_small,
                     bg="#212121", fg="white")
entryname.pack(pady=15)

button = tk.Button(frame_button, text="Done", command=qrcode,
                   font=font_small, bg="#1A1A1A", fg="white", width=10, height=1)
button.pack()

window.config(menu=menubar)

window.bind_all("<Control-f>", ofl)

if __name__ == "__main__":
    window.mainloop()
