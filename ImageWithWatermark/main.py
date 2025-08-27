import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        add_watermark(file_path)

def add_watermark(image_path):
    image = Image.open(image_path).convert("RGBA")
    watermark_text = "www.yourwebsite.com"

    # Create watermark layer
    watermark = Image.new("RGBA", image.size)
    draw = ImageDraw.Draw(watermark)

    font = ImageFont.truetype("arial.ttf", 36)  # You can change font and size
    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = (image.size[0] - text_width - 10, image.size[1] - text_height - 10)

    draw.text(position, watermark_text, font=font, fill=(255, 255, 255, 128))  # Semi-transparent white

    combined = Image.alpha_composite(image, watermark)
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
