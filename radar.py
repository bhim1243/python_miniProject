import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize data
labels = np.array(['A', 'B', 'C', 'D'])
stats = np.zeros(len(labels))  # Start with zeros

# Function to update data from camera feed
def update_data(frame):
    _, frame = cap.read()

    # Convert frame to grayscale and apply object detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Update stats based on detected objects
    stats.fill(0)  # Reset stats to zeros
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:  # Filter out small noise
            M = cv2.moments(cnt)
            cx = int(M['m10'] / (M['m00'] + 1e-5))  # x-coordinate of centroid
            cy = int(M['m01'] / (M['m00'] + 1e-5))  # y-coordinate of centroid
            # Assign values to corresponding labels based on centroid position
            if cy < frame.shape[0] // 2:
                stats[0] += 1
            elif cy >= frame.shape[0] // 2:
                stats[1] += 1
            if cx < frame.shape[1] // 2:
                stats[2] += 1
            elif cx >= frame.shape[1] // 2:
                stats[3] += 1

    # Update radar chart
    ax_radar.clear()
    ax_radar.fill(angles, stats, color='blue', alpha=0.25)
    ax_radar.plot(angles, stats, color='blue', linewidth=2)
    ax_radar.set_xticks(np.linspace(0, 2 * np.pi, len(labels), endpoint=False))
    ax_radar.set_xticklabels(labels)

    # Display the camera feed
    ax_camera.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

# Number of variables
num_vars = len(labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Set up camera
cap = cv2.VideoCapture(0)

# Create figure and axes for radar chart and camera feed
fig, (ax_radar, ax_camera) = plt.subplots(1, 2, figsize=(12, 6), subplot_kw=dict(polar=True))
ax_camera.axis('off')  # Turn off axis for camera feed

# Create animation
ani = FuncAnimation(fig, update_data, frames=range(200), interval=200)

plt.show()

# Release the camera
cap.release()
