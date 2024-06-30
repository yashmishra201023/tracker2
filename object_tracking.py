import cv2
import os

# Path to the video file
video_path = "C:/Users/Harishchandra mishra/Downloads/C119-SA-main/C119-SA-main/bb3.mp4"

# Check if the file exists
if not os.path.isfile(video_path):
    print(f"Error: The file {video_path} does not exist.")
    exit()

video = cv2.VideoCapture(video_path)

# Check if the video capture object is initialized
if not video.isOpened():
    print("Error: Could not open video.")
    exit()

# Initialize the tracker
tracker = cv2.TrackerCSRT_create()

# Read the first frame of the video
returned, img = video.read()

if not returned:
    print("Error: Failed to read video.")
    exit()

# Select the bounding box
bbox = cv2.selectROI("Tracking", img, False)

# Initialize the tracker with the first frame and bounding box
tracker.init(img, bbox)

print(bbox)

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3, 1)
    cv2.putText(img, "Tracking", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

while True:
    check, img = video.read()   

    if not check:
        print("Error: Failed to capture image.")
        break
   
    success, bbox = tracker.update(img)

    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img, "Lost", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("result", img)
            
    key = cv2.waitKey(25)
    if key == 32:  # Spacebar key
        print("Stopped")
        break

video.release()
cv2.destroyAllWindows()
