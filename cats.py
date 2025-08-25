from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO
from tkinter import Toplevel


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка {e}")
        return None


def open_new_window():
    tag = tag_entry.get()
    url_tag = f"http://cataas.com/cat/{tag}" if tag else "http://cataas.com/cat"
    img = load_image(url_tag)
    if img:
        new_window = Toplevel()
        new_window.title("Котик")
        new_window.geometry("600x480")
        label = Label(new_window, image = img)
        label.pack()
        label.image = img


window = Tk()
window.title("Котики!")
window.geometry("200x300")

tag_entry = Entry()
tag_entry.pack()

load_button = Button(text="Загрузить", command=open_new_window)
load_button.pack()



menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить картинку", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=window.destroy)

url = "http://cataas.com/cat"


window.mainloop()
