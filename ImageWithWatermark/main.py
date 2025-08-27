import tkinter as tk
from tkinter import filedialog
#filedialog module provides classes and factory functions for creating file/directory selection windows
from PIL import Image, ImageDraw, ImageFont

#The Python Imaging Library adds image processing capabilities to your Python interpreter.
#The Image module provides a class with the same name which is used to represent a PIL image.
#The module also provides a number of factory functions, including functions to load images from files,
#and to create new images.
#The ImageDraw module provides simple 2D graphics for Image objects. You can use this module to create new images,
# annotate or retouch existing images, and to generate graphics on the fly for web use.
#The ImageFont module defines a class with the same name. Instances of this class store bitmap fonts,
# and are used with the PIL.ImageDraw.ImageDraw.text() method.


def upload_image():
    file_path = filedialog.askopenfilename()
    #create an Open dialog and return the selected filename(s) that correspond to existing file(s).
    if file_path:
        add_watermark(file_path)

def add_watermark(image_path):
    image = Image.open(image_path).convert("RGBA")
    watermark_text = "www.yourwebsite.com"

    # Create watermark layer
    watermark = Image.new("RGBA", image.size)
    draw = ImageDraw.Draw(watermark)
    # ImageDraw.Draw(watermark) - Creates an object that can be used to draw in the given image.

    font = ImageFont.truetype("arial.ttf", 36)  # You can change font and size
    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = (image.size[0] - text_width - 10, image.size[1] - text_height - 10)

    draw.text(position, watermark_text, font=font, fill=(255, 255, 255, 128))  # Semi-transparent white

    combined = Image.alpha_composite(image, watermark)
    #Alpha composite im2 over im1.

    combined = combined.convert("RGB")  # Remove alpha for saving as JPEG

    save_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    if save_path:
        combined.save(save_path)
        print("Watermarked image saved!")

# GUI setup
root = tk.Tk()
root.title("Auto Watermark App")

upload_btn = tk.Button(root, text="Upload Image", command=upload_image)
upload_btn.pack(pady=20)

root.mainloop()
