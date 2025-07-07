import tkinter as tk
from tkinter import messagebox, scrolledtext
import random
import string

def generate_codes():
    prefix = entry_prefix.get()
    try:
        noc = int(entry_noc.get())
        code_len = int(entry_len.get())
    except ValueError:
        messagebox.showerror("Lỗi", "Số lượng code và độ dài phải là số nguyên!")
        return

    if code_len < len(prefix):
        messagebox.showerror("Lỗi", "Độ dài code phải lớn hơn hoặc bằng độ dài tiền tố.")
        return

    chars = string.ascii_uppercase + string.digits
    codes = []

    for _ in range(noc):
        code = prefix
        for _ in range(code_len - len(prefix)):
            c = random.choice(chars)
            c = c.replace("0", "X").replace("O", "X")
            code += c
        codes.append(code)

    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, "\n".join(codes))

def copy_all():
    all_text = result_box.get("1.0", tk.END).strip()  # Loại bỏ dòng trống cuối
    window.clipboard_clear()
    window.clipboard_append(all_text)
    messagebox.showinfo("Đã sao chép", "Toàn bộ mã đã được sao chép vào clipboard!")

# --- Giao diện chính ---
window = tk.Tk()
window.title("Trình sinh mã code")
window.geometry("400x430")

# Nhãn và ô nhập
tk.Label(window, text="Tiền tố (prefix):").pack()
entry_prefix = tk.Entry(window)
entry_prefix.pack()

tk.Label(window, text="Số lượng code cần sinh:").pack()
entry_noc = tk.Entry(window)
entry_noc.pack()

tk.Label(window, text="Tổng độ dài của code:").pack()
entry_len = tk.Entry(window)
entry_len.pack()

tk.Button(window, text="Sinh mã", command=generate_codes).pack(pady=10)

# Kết quả hiển thị
result_box = scrolledtext.ScrolledText(window, width=40, height=10)
result_box.pack(padx=10, pady=5)

# Nút Copy All
tk.Button(window, text="Copy All", command=copy_all).pack(pady=5)

# Chạy chương trình
window.mainloop()
