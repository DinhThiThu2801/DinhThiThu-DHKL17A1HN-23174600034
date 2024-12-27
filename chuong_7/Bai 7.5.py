import tkinter as tk
from PIL import Image, ImageTk
window = tk.Tk()

window.title("Chương trình xem ảnh")

image = Image.open("oto.png")
new_size = (400, 400)
image = image.resize(new_size, Image.ANTIALIAS)
oto.imshow("image", image)

img = ImageTk.PhotoImage(image)

label = tk.Label(window, image=img)

label.image = img

label.pack()
window.mainloop()