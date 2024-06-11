import cv2


def person_detection_opencv(video_path):
    # Initialize the HOG descriptor/person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to grayscale for HOG detector
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect people in the frame
        boxes, weights = hog.detectMultiScale(gray, winStride=(8, 8))

        # Draw bounding boxes for detected people
        for (x, y, w, h) in boxes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the frame
        cv2.imshow("Person Detection", frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close windows
    cap.release()
    cv2.destroyAllWindows()


# Path to the video file (update this path as per your setup)
video_path = "I:/video/tour video/video_20220404_231144.mp4"

# Run the person detection function
person_detection_opencv(video_path)
