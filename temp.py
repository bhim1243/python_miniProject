import os
import tempfile
from send2trash import send2trash


def move_temp_files_to_recycle_bin(directory):
    # List all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Check if the file is a temporary file
        if filename.startswith('tmp') or filename.endswith('.tmp'):
            try:
                # Move the temporary file to Recycle Bin
                send2trash(filepath)
                print(f"Moved temporary file to Recycle Bin: {filepath}")
            except Exception as e:
                print(f"Error moving file {filepath} to Recycle Bin: {e}")


if __name__ == "__main__":
    # Check if running as administrator
    import ctypes

    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Please run this script as an administrator.")
        exit()

    # Specify the directory to clean up
    directory_to_clean = tempfile.gettempdir()  # Gets the system's temporary directory

    # Move temporary files to Recycle Bin
    move_temp_files_to_recycle_bin(directory_to_clean)
