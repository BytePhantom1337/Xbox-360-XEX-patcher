import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

XEX_TOOL_PATH = "xextool.exe"

def get_xex_version(xex_path):
    """Get the version of the XEX file using xextool."""
    cmd = f'"{XEX_TOOL_PATH}" -l "{xex_path}"'
    process = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if process.returncode == 0:
        for line in process.stdout.splitlines():
            if "Version:" in line:
                version = line.split(":")[1].strip()
                return version
    else:
        messagebox.showerror("Error", f"Failed to get XEX version:\n{process.stderr}")
        return None

def compare_versions():
    """Compare the versions of two XEX files."""
    xex_file_1 = file_1_entry.get()
    xex_file_2 = file_2_entry.get()
    
    if not xex_file_1 or not os.path.exists(xex_file_1):
        messagebox.showerror("Error", "First XEX file not selected or doesn't exist!")
        return
    
    if not xex_file_2 or not os.path.exists(xex_file_2):
        messagebox.showerror("Error", "Second XEX file not selected or doesn't exist!")
        return
    
    version_1 = get_xex_version(xex_file_1)
    version_2 = get_xex_version(xex_file_2)
    
    if version_1 and version_2:
        result_text.config(state=tk.NORMAL)

        result_text.delete(1.0, tk.END)

        result_text.insert(tk.END, f"Version of File 1: {version_1}\n")
        result_text.insert(tk.END, f"Version of File 2: {version_2}\n")
        
        if version_1 == version_2:
            result_text.insert(tk.END, "The versions are the same.")
        else:
            result_text.insert(tk.END, f"The versions are different!\nFile 1: {version_1}\nFile 2: {version_2}")
        
        result_text.config(state=tk.DISABLED)

def select_file_1():
    """Select the first XEX file."""
    file_1 = filedialog.askopenfilename(filetypes=[("Xbox Executable", "*.xex")])
    file_1_entry.delete(0, tk.END)
    file_1_entry.insert(0, file_1)

def select_file_2():
    """Select the second XEX file."""
    file_2 = filedialog.askopenfilename(filetypes=[("Xbox Executable", "*.xex")])
    file_2_entry.delete(0, tk.END)
    file_2_entry.insert(0, file_2)

root = tk.Tk()
root.title("Compare XEX Versions")
root.geometry("500x350")

tk.Label(root, text="Select First XEX File:").pack(pady=5)
file_1_entry = tk.Entry(root, width=50)
file_1_entry.pack(pady=5)
tk.Button(root, text="Browse", command=select_file_1).pack(pady=5)

tk.Label(root, text="Select Second XEX File:").pack(pady=5)
file_2_entry = tk.Entry(root, width=50)
file_2_entry.pack(pady=5)
tk.Button(root, text="Browse", command=select_file_2).pack(pady=5)

tk.Button(root, text="Compare XEX Versions", command=compare_versions).pack(pady=10)

result_text = tk.Text(root, height=10, width=60)
result_text.pack(pady=10)

result_text.config(state=tk.DISABLED)

root.mainloop()
