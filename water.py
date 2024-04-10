import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def remove_watermark(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        messagebox.showerror("Error", "Failed to open input video.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    if not out.isOpened():
        messagebox.showerror("Error", "Failed to create output video.")
        return

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    while cap.isOpened():
        if not ret:
            break

        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 1000:  # Adjust the threshold based on the size of the watermark
                cv2.drawContours(frame1, [contour], -1, (0, 0, 0), -1)  # Fill the detected area with black

        out.write(frame1)

        frame1 = frame2
        ret, frame2 = cap.read()

    cap.release()
    out.release()
    messagebox.showinfo("Success", "Watermark removal completed successfully.")

def browse_input_file():
    input_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi")])
    if input_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, input_path)

def browse_output_file():
    output_path = filedialog.asksaveasfilename(defaultextension=".avi", filetypes=[("AVI files", "*.avi")], initialdir="/") # Change the initialdir to a different directory
    if output_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output_path)

def start_processing():
    input_path = input_entry.get()
    output_path = output_entry.get()
    if not input_path or not output_path:
        messagebox.showerror("Error", "Please select input and output files.")
        return
    remove_watermark(input_path, output_path)

# Create the main window
root = tk.Tk()
root.title("Video Watermark Removal")

# Create input file selection
input_label = tk.Label(root, text="Input Video:")
input_label.grid(row=0, column=0, padx=5, pady=5)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=5, pady=5)
input_button = tk.Button(root, text="Browse", command=browse_input_file)
input_button.grid(row=0, column=2, padx=5, pady=5)

# Create output file selection
output_label = tk.Label(root, text="Output Video:")
output_label.grid(row=1, column=0, padx=5, pady=5)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=5, pady=5)
output_button = tk.Button(root, text="Browse", command=browse_output_file)
output_button.grid(row=1, column=2, padx=5, pady=5)

# Create start button
start_button = tk.Button(root, text="Start Processing", command=start_processing)
start_button.grid(row=2, column=1, padx=5, pady=5)

# Start the main event loop
root.mainloop()
