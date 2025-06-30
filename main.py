from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from functions import import_image, images, add_watermark

window = Tk()
window.title("Watermarking App")
window.maxsize(width=750, height=500)
window.minsize(width=400, height=300)
window.config(padx=50, pady=30)

label = Label(text="Add a Watermark to an Image", font=("Times New Roman", 18))
label.config(pady=20)
label.grid(row=0, column=0, columnspan=2)

def import_start_img():
    global strl0
    import_image('start', 'Import a Starting Image',
                 row=1, destroy_button=start_img_button, next_button=water_m_button)
    strl0 = Label(text='Starting Image', font=('Times New Roman', 12))
    strl0.grid(row=1, column=0, columnspan=2)
    images['start_l'].grid(row=2, column=0, columnspan=2)


start_img_button = Button(text="Import a Starting Image", command=import_start_img)
start_img_button.grid(row=1, column=0, columnspan=2)

def import_water_m():
    import_image('watermark', 'Import a Watermark', next_button=combine,
                 row=2, destroy_button=water_m_button)
    strl0.grid(row=1, column=0, columnspan=1)
    images['start_l'].grid(row=2, column=0, columnspan=1)
    strl1 = Label(text='Watermark Image', font=('Times New Roman', 12))
    strl1.grid(row=1, column=1)
    images['watermark_l'].grid(row=2, column=1)

water_m_button = Button(text="Now Import a Watermark Image", command=import_water_m)

def add_waterm():
    add_watermark(images['start_pil'], images['watermark_pil'])

combine = Button(text='Add Watermark!', command=add_waterm)

window.mainloop()