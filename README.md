# YouTube Audio Downloader
### Author: Felipe Pinto

This Python script provides a simple graphical interface for downloading audio from YouTube videos using the `yt-dlp` command-line tool. It allows you to select a download folder, monitor progress, and saves your preferences.

## Requirements

- **Python:** The script is written in Python and requires the `tkinter`, `subprocess`, `threading`, `os`, and `json` modules.
- **yt-dlp:**  You need to have the `yt-dlp` command-line downloader installed. You can download it from the official repository or install it using your package manager.
- **FFmpeg:** The script uses FFmpeg to convert audio to MP3 format. Ensure it's installed and that the `--ffmpeg-location` in the code points to its correct path. 

## Usage

1. **Run the script:** Execute the Python file. A window titled "YouTube Audio Downloader" will appear.
2. **Enter Video Link:** Paste the YouTube video URL into the provided field.
3. **Choose Output Folder:** 
    - Click the "Procurar" (Browse) button to select the directory where the downloaded audio will be saved.
    - The script remembers your last selected folder.
4. **Click "Baixar" (Download):** The download process will start.
5. **Monitor Progress:** A progress bar and text updates will show you the download status.

## Features

- **Best Audio Quality:**  The script automatically selects the best available audio quality.
- **MP3 Format:** The downloaded audio is converted to MP3 format for wider compatibility.
- **Progress Tracking:** A visual progress bar and detailed text output keep you informed.
- **Settings Persistence:** Your last used output folder is saved for convenience.

## Code Explanation

### Functions

- `download_audio()`:
    - Gets the video URL and output path.
    - Constructs the `yt-dlp` command with options:
        - `-f bestaudio`: Chooses the best audio quality.
        - `-x`: Extracts audio only.
        - `--audio-format mp3`: Converts to MP3 format.
        - `--ffmpeg-location`: Specifies the path to FFmpeg.
    - Starts the `yt-dlp` process.
    - Creates a thread to monitor and update progress.

- `update_progress()`:
    - Reads the output of the `yt-dlp` process.
    - Extracts progress information from lines containing "ETA."
    - Updates the progress bar and text label.

- `browse_folder()`:
    - Opens a dialog to select the output folder.
    - Updates the entry field and saves the setting.

- `load_settings()`:
    - Loads saved settings from `settings.json` (output folder).

- `save_settings()`:
    - Saves the current output folder to `settings.json`.

### GUI

- The main window uses `tkinter` to create the interface elements:
    - Labels and entry fields for the video link and output path.
    - Buttons to browse for a folder and start the download.
    - A progress bar to visualize download status.
    - A label to display detailed progress information.

## Important Note

Make sure to replace `/usr/bin/ffmpeg` with the correct path to FFmpeg on your system.

Let me know if you would like me to elaborate further on any aspect of the code or its usage!
