import tkinter as tk
from tkinter import ttk, filedialog
import subprocess
import threading
import os
import json

def download_audio():
    url = link_entry.get()
    output_path = output_path_var.get()
    command = [
        "yt-dlp",
        "-f", "bestaudio",  # Melhor qualidade de áudio disponível
        "-x",  # Extrair áudio
        "--audio-format", "mp3",
        "--ffmpeg-location", "/usr/bin/ffmpeg",  # Substitua pelo caminho correto do ffmpeg
        "--newline",  # Saída formatada para leitura
        "-o", os.path.join(output_path, "%(title)s.%(ext)s"),
        url
    ]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

    def update_progress():
        for line in process.stdout:
            if "ETA" in line:
                progress_str = line.split("ETA")[0].strip()
                progress_parts = progress_str.split("]")
                if len(progress_parts) > 1:
                    percentage_str = progress_parts[1].strip().split("%")[0]
                    try:
                        percentage = float(percentage_str)
                        progress_bar["value"] = percentage
                        stats_label.config(text=progress_str)
                        window.update_idletasks()
                    except ValueError:
                        pass

    progress_thread = threading.Thread(target=update_progress)
    progress_thread.start()

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        output_path_var.set(folder_selected)
        save_settings()

def load_settings():
    try:
        with open("settings.json", "r") as f:
            settings = json.load(f)
            output_path_var.set(settings.get("output_path", ""))
    except FileNotFoundError:
        pass

def save_settings():
    settings = {"output_path": output_path_var.get()}
    with open("settings.json", "w") as f:
        json.dump(settings, f)

# GUI
window = tk.Tk()
window.title("YouTube Audio Downloader")

link_label = ttk.Label(window, text="Link do Vídeo:")
link_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

link_entry = ttk.Entry(window, width=50)
link_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

output_path_var = tk.StringVar()
output_path_label = ttk.Label(window, text="Pasta de Destino:")
output_path_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

output_path_entry = ttk.Entry(window, textvariable=output_path_var, width=50)
output_path_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

browse_button = ttk.Button(window, text="Procurar", command=browse_folder)
browse_button.grid(row=1, column=2, padx=5, pady=5)

download_button = ttk.Button(window, text="Baixar", command=download_audio)
download_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

progress_bar = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate")
progress_bar.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

stats_label = ttk.Label(window, text="")
stats_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

load_settings()
window.mainloop()

