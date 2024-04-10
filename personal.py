import cv2
import mediapipe as mp

class PersonalTrainer:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()
        self.exercise_count = 0
        self.rep_count = 0

    def track_pushups(self, image):
        # Convert the image to RGB
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Make detections
        results = self.pose.process(rgb_image)

        # Check if push-up is detected
        if results.pose_landmarks:
            # Get landmarks
            landmarks = results.pose_landmarks.landmark

            # Calculate angle between shoulders, elbows, and hips
            left_shoulder = landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
            left_elbow = landmarks[self.mp_pose.PoseLandmark.LEFT_ELBOW.value].y
            left_hip = landmarks[self.mp_pose.PoseLandmark.LEFT_HIP.value].y
            right_shoulder = landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y
            right_elbow = landmarks[self.mp_pose.PoseLandmark.RIGHT_ELBOW.value].y
            right_hip = landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP.value].y

            # Check if arms are lower than shoulders and body is straight
            if left_shoulder < left_elbow and right_shoulder < right_elbow and \
                    left_hip < left_shoulder and right_hip < right_shoulder:
                # Increment rep count
                self.rep_count += 1
                print(f"Rep Count: {self.rep_count}")
                # Reset rep count after every 5 reps
                if self.rep_count % 5 == 0:
                    self.exercise_count += 1
                    print(f"Exercise Count: {self.exercise_count}")

        # Draw pose landmarks
        mp.solutions.drawing_utils.draw_landmarks(image, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

        return image


# Initialize personal trainer
trainer = PersonalTrainer()

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Track push-up exercise
    frame = trainer.track_pushups(frame)

    # Display frame
    cv2.imshow('Push-up Tracker', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy any OpenCV windows
cap.release()
cv2.destroyAllWindows()
