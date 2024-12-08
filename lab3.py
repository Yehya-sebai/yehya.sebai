import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

def shift_characters(block, shift):
    shifted_block = ""
    for char in block:
        if char.isalpha():
            shifted_block += chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
    return shifted_block

def generate_key():
    input_block = entry.get()
    
    if len(input_block) != 5 or not input_block.isalpha():
        messagebox.showerror("Error", "Введите блок из 5 букв.")
        return
    
    input_block = input_block.upper()
    
    block2 = shift_characters(input_block, 3)
    block3 = shift_characters(input_block, -5)
    
    generated_key = f"{input_block}-{block2}-{block3}"
    
    result_label.config(text=f"Сгенерированный ключ: {generated_key}")

root = tk.Tk()
root.title("Keygen - Variant 5")
root.geometry("400x300")

try:
    background_image = Image.open("./bg.jpg")
    background_image = background_image.resize((400, 300), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print(f"Background image not loaded: {e}")

instruction_label = tk.Label(root, text="Введите блок из 5 букв:", bg="white", font=("Arial", 12))
instruction_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), width=10)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Генерировать ключ", command=generate_key, font=("Arial", 12), bg="blue", fg="white")
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", bg="white", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
