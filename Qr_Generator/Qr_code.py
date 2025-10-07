import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import qrcode

class QRcodeApp:
    def __init__(self, root):
        self.file_path = None
        self.root = root

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)
        self.root.rowconfigure(4, weight=1)

        # URL Enter
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
        self.entry.insert(0, "https://")

        # Buttons
        self.add_photo = tk.Button(root, text="Orta Resim Ekle", command=self.addPhoto, font=("Arial", 12))
        self.add_photo.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.generate_btn = tk.Button(root, text="QR Oluştur", command=self.generate, font=("Arial", 12))
        self.generate_btn.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        # situation
        self.status = tk.Label(root, text="", font=("Arial", 12))
        self.status.grid(row=2, column=0, columnspan=2, pady=5)

        # QR Image 
        self.qr_label = tk.Label(root)
        self.qr_label.grid(row=3, column=0, columnspan=2, pady=10)

    def addPhoto(self):
        self.file_path = filedialog.askopenfilename(
            title="Bir resim seçin",
            filetypes=[("Resim Dosyaları", "*.jpg *.png *.jpeg *.bmp")]
        )
        if self.file_path:
            self.status.config(text="Image ✅")
        else:
            self.status.config(text="Image ❌")

    def generate(self):
        data = self.entry.get()

        if not data:
            self.status.config(text="URL enter ❌")
            return

        qr = qrcode.QRCode(version=1, box_size=10, border=2)
        qr.add_data(data)
        qr.make(fit=True)

        qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

        if self.file_path:
            try:
                center_img = Image.open(self.file_path).convert("RGBA")
                qr_width, qr_height = qr_img.size
                logo_size = qr_width // 4
                center_img = center_img.resize((logo_size, logo_size))
                pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
                qr_img.paste(center_img, pos, center_img)
            except Exception as e:
                self.status.config(text=f"Hata: {str(e)}")
                return

        self.qr_image_tk = ImageTk.PhotoImage(qr_img)
        self.qr_label.config(image=self.qr_image_tk)
        self.status.config(text="QR code is ready ✅")

# window starter
root = tk.Tk()
root.title("Qr generator")
root.geometry("600x600")  # starting size
root.minsize(400, 400)    # Min shape

QRcodeApp(root)
root.mainloop()
