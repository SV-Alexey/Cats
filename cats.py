from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO


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


def set_image():
    img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img

window = Tk()
window.title("Котики!")
window.geometry("600x520")

label = Label()
label.pack()

# updete_button = Button(text="Обновить", command=set_image)
# updete_button.pack()

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Обновить", command=set_image)

url = "http://cataas.com/cat"

set_image()

window.mainloop()
