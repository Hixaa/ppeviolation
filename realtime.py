import cv2
from ultralytics.yolo.engine.model import YOLO

# Load the YOLOv8 model
model = YOLO(r"last.pt")

# Specify the class IDs based on model.names = {0: 'helmet', 1: 'mask', 2: 'jacket', 3: 'shoe', 4: 'harness', 5: 'no_helmet', 6: 'no_mask', 7: 'no_jacket', 8: 'no_shoe', 9: 'no_harness'}
# class_ids = [0]

import os

# class_ids = [0, 5]
class_ids = list(map(int, os.environ["CLASS_IDS"].split(",")))

# Open the camera
cap = cv2.VideoCapture(0)

# Loop through the camera frames
while True:
    # Read a frame from the camera
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame for the specified classes
        results = model.predict(source=frame, classes=class_ids)

        # Process the results for the specified classes
        for i, result in enumerate(results):
            # Get the annotated frame with the specified classes
            annotated_frame = result.plot()

            # Display the annotated frame
            cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Check for keyboard events
        key = cv2.waitKey(1) & 0xFF

        # Exit the loop if the 'q' key is pressed or the exit button in annotated_frame is pressed
        if key == ord('q') or cv2.getWindowProperty("YOLOv8 Inference", cv2.WND_PROP_VISIBLE) < 1:
            break

# Release the VideoCapture object
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
