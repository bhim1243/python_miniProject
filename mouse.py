import cv2
import mediapipe as mp
import pyautogui

# Initialize hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Initialize screen dimensions
screen_width, screen_height = pyautogui.size()

# Function to map hand landmarks to screen coordinates
def map_coordinates(hand_landmarks):
    mapped_points = []
    for point in hand_landmarks.landmark:
        x = int(point.x * screen_width)
        y = int(point.y * screen_height)
        mapped_points.append((x, y))
    return mapped_points

# Function to perform mouse actions based on hand movement
def perform_mouse_actions(mapped_points):
    if len(mapped_points) == 0:
        return

    # Get hand landmarks
    index_finger = mapped_points[8]

    # Move mouse cursor
    pyautogui.moveTo(index_finger[0], index_finger[1])

    # Perform click action if thumb is raised
    if mapped_points[4][1] < mapped_points[3][1] < mapped_points[2][1] < mapped_points[1][1]:
        pyautogui.click()

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Use Mediapipe to detect hands
    results = hands.process(rgb_frame)

    # Draw hand landmarks on the frame
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Map hand landmarks to screen coordinates
            mapped_points = map_coordinates(hand_landmarks)

            # Perform mouse actions based on hand movement
            perform_mouse_actions(mapped_points)

    # Display the frame
    cv2.imshow('AI Virtual Mouse', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy any OpenCV windows
cap.release()
cv2.destroyAllWindows()
