import customtkinter as ctk
import DB as db
from tkinter import ttk
from datetime import datetime, timedelta
from PIL import Image

root = ctk.CTk()
root.geometry("800x600")

ctk.set_default_color_theme("green")  
root.configure(fg_color="green")
image = Image.open("C:\\Users\\yusuf\\Downloads\\kütüphane.jpg")

ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(800, 600))

bg_label = ctk.CTkLabel(root, image=ctk_image, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

def add_student():
    new_window = ctk.CTkToplevel(root)
    new_window.title("Add Student")
    new_window.geometry("600x400")

    new_window.configure(fg_color="white")
    entry1 = ctk.CTkEntry(new_window, placeholder_text="Name")
    entry1.place(x=10, y=10)
    entry2 = ctk.CTkEntry(new_window, placeholder_text="Book")
    entry2.place(x=10, y=50)
    entry4 = ctk.CTkEntry(new_window, placeholder_text="Delivery")
    entry4.place(x=10, y=130)
    
    def destroy1():
        today = datetime.now()
        future = today + timedelta(days=int(entry4.get()))

        db.cursor.execute("INSERT INTO users (name, book, date, delivery) VALUES (?, ?, ?, ?)",
                      (entry1.get(), entry2.get(), today.strftime("%Y-%m-%d") ,future.strftime("%Y-%m-%d")))

        db.connection.commit()
        new_window.destroy()

    Destroy = ctk.CTkButton(new_window, text="Tamamla",command=destroy1)
    Destroy.place(x=10, y=170)

def delete_student():
    selected = tree.selection()  # seçilen satırı al
    if selected:
        values = tree.item(selected[0], "values")  # seçilen satırın verileri
        student_id = values[0]  # id üzerinden silme yapacağız

        db.cursor.execute("DELETE FROM users WHERE id = ?", (student_id,))
        db.connection.commit()

        tree.delete(selected[0])  # GUI'den de sil

delete_button = ctk.CTkButton(root, text="Öğrenci Sil", command=delete_student)
delete_button.place(x=325, y=350)

add_button = ctk.CTkButton(root, text="Öğrenci Ekle",command=add_student)
add_button.place(x=325,y=300)

tree = ttk.Treeview(root, columns=("id","name","book","date","delivery"), show="headings") 
tree.heading("id", text="ID")
tree.heading("name", text="İsim")
tree.heading("book", text="Eser")
tree.heading("date", text="Alınma Tarihi")
tree.heading("delivery", text="Veriş Tarihi")
tree.place(x=10, y=50)

"""for i in db.datas:
    tree.insert("", "end", values=i)"""

tree.tag_configure("late", background="red")  # kırmızı arka planlı satırlar için

for i in db.datas:
    delivery_date = datetime.strptime(i[4], "%Y-%m-%d")  # i[4] teslim tarihi
    today = datetime.now()

    if delivery_date <= today:
        tree.insert("", "end", values=i, tags=("late",))  # geç kaldıysa kırmızı
    else:
        tree.insert("", "end", values=i)

root.mainloop()
