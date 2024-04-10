import cv2
import numpy as np

# Initialize canvas
canvas = np.ones((480, 640, 3), dtype=np.uint8) * 255  # White canvas
color = (0, 0, 0)  # Default color (BGR): Black
drawing = True  # Flag to toggle between drawing and erasing

# Create a window and set mouse callback function
cv2.namedWindow('Virtual Painter')
cv2.setMouseCallback('Virtual Painter', lambda event, x, y, flags, param: draw(event, x, y, flags, param))

# Function to draw on canvas
def draw(event, x, y, flags, param):
    global canvas, color, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        if drawing:
            cv2.circle(canvas, (x, y), 5, color, -1)  # Draw a circle on the canvas
        else:
            cv2.circle(canvas, (x, y), 5, (255, 255, 255), -1)  # Erase by drawing white circle

    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing:
            cv2.circle(canvas, (x, y), 5, color, -1)  # Draw a circle on the canvas
        else:
            cv2.circle(canvas, (x, y), 5, (255, 255, 255), -1)  # Erase by drawing white circle

# Main loop
while True:
    cv2.imshow('Virtual Painter', canvas)

    # Check for key events
    key = cv2.waitKey(1) & 0xFF

    # Clear canvas when 'c' is pressed
    if key == ord('c'):
        canvas = np.ones((480, 640, 3), dtype=np.uint8) * 255

    # Toggle between drawing and erasing when 'e' is pressed
    elif key == ord('e'):
        drawing = not drawing

    # Change color when 'r', 'g', 'b' is pressed
    elif key == ord('r'):
        color = (0, 0, 255)  # Red
    elif key == ord('g'):
        color = (0, 255, 0)  # Green
    elif key == ord('b'):
        color = (255, 0, 0)  # Blue

    # Quit when 'q' is pressed
    elif key == ord('q'):
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
