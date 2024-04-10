import cv2
import dlib
import openpyxl

# Initialize face detector and facial landmarks predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # Download this file from dlib's website

def mark_attendance(known_image_path, output_excel):
    # Load the known image and encoding
    known_image = cv2.imread(known_image_path)

    # Initialize video capture
    video_capture = cv2.VideoCapture(0)

    # Create or load Excel workbook and worksheet
    try:
        workbook = openpyxl.load_workbook(output_excel)
    except FileNotFoundError:
        workbook = openpyxl.Workbook()
    worksheet = workbook.active
    if not worksheet['A1'].value:
        worksheet['A1'] = 'Name'
        worksheet['B1'] = 'Attendance'

    try:
        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()
            if not ret:
                print("Error: Failed to capture frame")
                break

            # Convert frame to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the frame
            faces = detector(gray)

            # Draw rectangles around the faces and mark attendance
            for face in faces:
                # Get facial landmarks
                landmarks = predictor(gray, face)
                # Recognize face (you can add your own recognition logic here)
                recognized_name = "Unknown"
                # Extract coordinates of the face rectangle
                (x, y, w, h) = (face.left(), face.top(), face.width(), face.height())
                # Draw rectangle around the face
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                # Write recognized name on the frame
                cv2.putText(frame, recognized_name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                # Write to Excel
                worksheet.append([recognized_name, "Present"])
                workbook.save(output_excel)

            # Display the resulting frame
            cv2.imshow('Video', frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # Release the video capture object and close all windows
        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    known_image_path = "known_person.jpg"
    output_excel = "attendance.xlsx"
    mark_attendance(known_image_path, output_excel)
