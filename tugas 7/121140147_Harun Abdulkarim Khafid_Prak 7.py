import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

#fungsi untuk membuka file
def openfile():
    filepath = askopenfilename(filetype = [("Text Files", "*.txt"), ("All Files", "*.*")]) #type data file
    if filepath:
        #fungsi delete untuk menimpa text dengan text yang akan di buka
        txt_edit.delete(1.0, tk.END)
        
        with open(filepath, "r") as file:
            text = file.read()
            txt_edit.insert(tk.END, text)
        window.title(f"Text Editor - {filepath}")
#fungsi untuk menyimpan file
def savefile():
    filepath = asksaveasfilename( defaultextension="txt", filetype = [("Text Files", "*.txt"), ("All Files", "*.*")]) #type data file
    if filepath:
        with open(filepath, "w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
        window.title(f"Text Editor - {filepath}")
#inisiasi main window
window = tk.Tk()
#konfigurasi ukuran window
window.geometry("800x800")
window.title("Text editor")
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)


#widget-widget
txt_edit = tk.Text(window)
#grid_bar untuk pembatas antara open, save dengan textbox
grid_bar = tk.Frame(window, relief=tk.RAISED, bd=2)
button_open = tk.Button(grid_bar, text="Open",command = openfile)
button_save = tk.Button(grid_bar, text="Save As",command = savefile)
button_open.grid(column=0, row=0, sticky="ew", padx=5, pady=5)
button_save.grid(column=0, row=1, sticky="ew", padx=5)
grid_bar.grid(column=0, row=0, sticky="ns")
txt_edit.grid(column=1, row=0, sticky="nsew")

window.mainloop()
