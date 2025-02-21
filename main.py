import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

XEX_TOOL_PATH = "xextool.exe"
GAME_XEX = ""
XEXP_FILE = ""

def check_files():
    """Ensure necessary files exist before proceeding."""
    if not os.path.exists(XEX_TOOL_PATH):
        messagebox.showerror("Error", "xextool.exe not found!")
        return False
    if not GAME_XEX or not os.path.exists(GAME_XEX):
        messagebox.showerror("Error", "Game default.xex not selected or missing!")
        return False
    if not XEXP_FILE or not os.path.exists(XEXP_FILE):
        messagebox.showerror("Error", "XEXP file not selected or missing!")
        return False
    return True

def patch_xex():
    """Use xextool to apply TU patches to the XEX file."""
    if not check_files():
        return

    patched_xex = os.path.join(os.path.dirname(GAME_XEX), "default_patched.xex")
    cmd = f'"{XEX_TOOL_PATH}" -p "{XEXP_FILE}" "{GAME_XEX}"'

    try:
        # Run xextool to patch the XEX file
        subprocess.run(cmd, shell=True, check=True)
        messagebox.showinfo("Success", f"Patched XEX saved as {patched_xex}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to patch XEX:\n{e}")

def select_game_xex():
    """Select the game .xex file."""
    global GAME_XEX
    GAME_XEX = filedialog.askopenfilename(filetypes=[("Xbox Executable", "*.xex")])
    game_xex_label.config(text=os.path.basename(GAME_XEX) if GAME_XEX else "No file selected")

def select_xexp_file():
    """Select the .xexp patch file."""
    global XEXP_FILE
    XEXP_FILE = filedialog.askopenfilename(filetypes=[("XEX Patch", "*.xexp")])
    xexp_file_label.config(text=os.path.basename(XEXP_FILE) if XEXP_FILE else "No file selected")

root = tk.Tk()
root.title("Xbox 360 XEX Patcher")
root.geometry("400x250")

# Step 1: Select Game XEX
tk.Label(root, text="Select Game XEX:").pack(pady=(10, 0))
game_xex_label = tk.Label(root, text="No file selected", fg="gray")
game_xex_label.pack()
tk.Button(root, text="Browse", command=select_game_xex).pack(pady=5)

# Step 2: Select XEXP Patch File
tk.Label(root, text="Select XEXP File:").pack(pady=(10, 0))
xexp_file_label = tk.Label(root, text="No file selected", fg="gray")
xexp_file_label.pack()
tk.Button(root, text="Browse", command=select_xexp_file).pack(pady=5)

# Step 3: Patch XEX
tk.Button(root, text="Patch XEX", command=patch_xex).pack(pady=10)

root.mainloop()
