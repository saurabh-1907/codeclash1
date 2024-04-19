import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import requests
import io

class TkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x200")
        self.root.title("Brain Tumor Detection")

        self.file_path = tk.StringVar()
        self.result_var = tk.StringVar()

        label = tk.Label(root, text="Select an image:")
        label.pack()

        self.file_entry = tk.Entry(root, textvariable=self.file_path, state='disabled')
        self.file_entry.pack()

        browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        browse_button.pack()

        upload_button = tk.Button(root, text="Upload", command=self.upload_image)
        upload_button.pack()

        result_label = tk.Label(root, textvariable=self.result_var)
        result_label.pack()

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.file_path.set(file_path)

    def upload_image(self):
        file_path = self.file_path.get()
        if not file_path:
            messagebox.showerror("Error", "Please select an image.")
            return

        try:
            files = {'image': open(file_path, 'rb')}
            response = requests.post('http://127.0.0.1:5000/upload', files=files)
            result = response.json().get('result')
            self.result_var.set(f"Result: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterApp(root)
    root.mainloop()
