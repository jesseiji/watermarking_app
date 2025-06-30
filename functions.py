from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance

image_types = (
    ("PNG files", "*.png"),
    ("GIF files", "*.gif"),
    ("PPM files", "*.ppm"),
    ("PGM files", "*.pgm"),
)

images = {
    'start_pil': None,
    'watermark_pil': None,
    'start_l': None,
    'watermark_l': None,
    'start_lpho': None,
    'watermark_lpho': None
}

def import_image(prefix, title, row, destroy_button=None, next_button=None):
    global images
    file_path = None
    while not file_path:
        file_path = filedialog.askopenfilename(
            initialdir="C:/Downloads",  # Set the initial directory
            title=title,  # Title of the dialog
            filetypes=image_types  # File types to filter
        )

        if file_path:
            pil_img = Image.open(file_path)
            pil_img.thumbnail((250, 250))

            photo = ImageTk.PhotoImage(pil_img)
            img_label = Label(image=photo)

            images[f'{prefix}_pil'] = pil_img
            images[f'{prefix}_l'] = img_label
            images[f'{prefix}_lpho'] = photo

            destroy_button.destroy()
            next_button.grid(row=row+3, column=0, pady=20, columnspan=2)

def add_watermark(img, waterm):
    if waterm.mode != 'RGBA':
        waterm = waterm.convert('RGBA')

    alpha = waterm.split()[3]  # get alpha channel
    alpha = ImageEnhance.Brightness(alpha).enhance(0.5)  # lower brightness = lower opacity
    waterm.putalpha(alpha)  # apply new alpha back

    waterm.thumbnail((50, 50))
    region = waterm
    img.paste(region, (0, 0), region)
    img.show()


