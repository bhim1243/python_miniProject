import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, font
from tkinter import ttk
from PIL import Image, ImageTk
import io
import docx2pdf

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Edit")

        # Create a Text widget
        self.text = tk.Text(self.root, undo=True)
        self.text.pack(fill=tk.BOTH, expand=1)

        # Create a menu bar
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        # File menu
        file_menu = tk.Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="New Window", command=self.new_window)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_command(label="Save All", command=self.save_all)
        file_menu.add_command(label="Page Setup", command=self.page_setup)
        file_menu.add_command(label="Print", command=self.print_file)
        file_menu.add_command(label="Load Image", command=self.load_image)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = tk.Menu(self.menubar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)
        edit_menu.add_command(label="Delete", command=self.delete)
        edit_menu.add_command(label="Select All", command=self.select_all)
        edit_menu.add_command(label="Replace", command=self.replace_text)
        self.menubar.add_cascade(label="Edit", menu=edit_menu)

        # View menu
        view_menu = tk.Menu(self.menubar, tearoff=0)
        view_menu.add_command(label="Zoom In", command=self.zoom_in)
        view_menu.add_command(label="Edit Font", command=self.edit_font)
        self.menubar.add_cascade(label="View", menu=view_menu)

        # Tools menu
        tools_menu = tk.Menu(self.menubar, tearoff=0)
        tools_menu.add_command(label="Convert Word to PDF", command=self.word_to_pdf)
        tools_menu.add_command(label="Enhance Text in Image Online", command=self.enhance_text_in_image)
        self.menubar.add_cascade(label="Tools", menu=tools_menu)

    def new_window(self):
        new_root = tk.Tk()
        new_app = TextEditor(new_root)
        new_root.mainloop()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, content)
            self.root.title(f"Text Edit - {file_path}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                content = self.text.get(1.0, tk.END)
                file.write(content)
            self.root.title(f"Text Edit - {file_path}")

    def save_as(self):
        self.save_file()

    def save_all(self):
        self.save_file()

    def page_setup(self):
        messagebox.showinfo("Info", "Page Setup functionality is not implemented yet.")

    def print_file(self):
        messagebox.showinfo("Info", "Print functionality is not implemented yet.")

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("All files", "*.*")])
        if file_path:
            image = Image.open(file_path)
            image.thumbnail((400, 400))
            photo = ImageTk.PhotoImage(image)
            img_label = tk.Label(self.text, image=photo)
            img_label.image = photo
            self.text.window_create(tk.END, window=img_label)

    def cut(self):
        self.text.event_generate("<<Cut>>")

    def copy(self):
        self.text.event_generate("<<Copy>>")

    def paste(self):
        self.text.event_generate("<<Paste>>")

    def delete(self):
        self.text.delete("sel.first", "sel.last")

    def select_all(self):
        self.text.tag_add("sel", "1.0", "end")

    def replace_text(self):
        find_text = simpledialog.askstring("Find", "Enter the text to replace:")
        replace_text = simpledialog.askstring("Replace", "Enter the new text:")
        content = self.text.get(1.0, tk.END)
        new_content = content.replace(find_text, replace_text)
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, new_content)

    def zoom_in(self):
        current_font = font.nametofont(self.text.cget("font"))
        current_size = current_font.actual()["size"]
        new_size = current_size + 2
        current_font.configure(size=new_size)

    def edit_font(self):
        font_family = simpledialog.askstring("Font", "Enter font family (e.g., Arial):")
        font_size = simpledialog.askinteger("Font", "Enter font size (e.g., 12):")
        current_font = font.nametofont(self.text.cget("font"))
        current_font.configure(family=font_family, size=font_size)

    def word_to_pdf(self):
        word_file = filedialog.askopenfilename(filetypes=[("Word files", "*.docx"), ("All files", "*.*")])
        if word_file:
            pdf_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
            if pdf_file:
                docx2pdf.convert(word_file, pdf_file)
                messagebox.showinfo("Info", f"Successfully converted {word_file} to {pdf_file}")

    def enhance_text_in_image(self):
        messagebox.showinfo("Info", "Enhance text in image online functionality is not implemented yet.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
