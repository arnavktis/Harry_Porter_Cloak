import cv2
import numpy as np

# Function for trackbar callback
def hello(x):
    pass

# Initialize the camera
cap = cv2.VideoCapture(0)
cv2.namedWindow("bars")

# Create trackbars for HSV range adjustments
# cv2.createTrackbar("upper_hue", "bars", 53, 180, hello)
# cv2.createTrackbar("upper_saturation", "bars", 20, 255, hello)
# cv2.createTrackbar("upper_value", "bars", 130, 255, hello)
# cv2.createTrackbar("lower_hue", "bars", 43, 180, hello)
# cv2.createTrackbar("lower_saturation", "bars", 0, 255, hello)
# cv2.createTrackbar("lower_value", "bars", 90, 255, hello)

cv2.createTrackbar("upper_hue", "bars", 180, 190, hello)  # Upper range for hue
cv2.createTrackbar("upper_saturation", "bars", 255, 255, hello)  # Upper range for saturation
cv2.createTrackbar("upper_value", "bars", 206, 255, hello)  # Upper range for value
cv2.createTrackbar("lower_hue", "bars", 165, 180, hello)  # Lower range for hue (example, adjust as needed)
cv2.createTrackbar("lower_saturation", "bars", 71, 255, hello)  # Lower range for saturation (example, adjust as needed)
cv2.createTrackbar("lower_value", "bars", 156, 255, hello)

# Capture the initial frame for background
while True:
    ret, init_frame = cap.read()
    if ret:
        break

# Start processing frames
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get HSV trackbar values
    upper_hue = cv2.getTrackbarPos("upper_hue", "bars")
    upper_saturation = cv2.getTrackbarPos("upper_saturation", "bars")
    upper_value = cv2.getTrackbarPos("upper_value", "bars")
    lower_hue = cv2.getTrackbarPos("lower_hue", "bars")
    lower_saturation = cv2.getTrackbarPos("lower_saturation", "bars")
    lower_value = cv2.getTrackbarPos("lower_value", "bars")

    # Define the HSV range for masking
    upper_hsv = np.array([upper_hue, upper_saturation, upper_value])
    lower_hsv = np.array([lower_hue, lower_saturation, lower_value])

    # Create the mask and its inverse
    mask = cv2.inRange(hsv_frame, lower_hsv, upper_hsv)
    mask = cv2.medianBlur(mask, 5)  # Increase blur to reduce noise
    mask_inv = 255 - mask
    mask = cv2.dilate(mask, np.ones((5, 5), np.uint8), iterations=3)  # Increased iterations

    # Process the current frame
    frame_inv = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Process the background frame
    blanket_area = cv2.bitwise_and(init_frame, init_frame, mask=mask)

    # Combine both frames
    final = cv2.add(frame_inv, blanket_area)

    cv2.imshow("Harry's Cloak", final)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()