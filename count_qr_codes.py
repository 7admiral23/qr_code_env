import cv2
from pyzbar import pyzbar


def count_qr_codes_in_video(video_path):
    # Initialize the video capture object
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    frame_count = 0
    unique_qr_codes = set()

    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        if not ret:
            break  # End of video

        frame_count += 1

        # Detect QR codes in the frame
        qr_codes = pyzbar.decode(frame)

        # Add QR code data to the set of unique QR codes
        for qr in qr_codes:
            qr_data = qr.data.decode('utf-8')
            unique_qr_codes.add(qr_data)

        # Print the count of QR codes in the current frame
        print(f"Frame {frame_count}: {len(qr_codes)} QR code(s) detected.")

        # Draw bounding boxes around the detected QR codes
        for qr in qr_codes:
            (x, y, w, h) = qr.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the frame with the QR code detections
        cv2.imshow("Frame", frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object
    cap.release()
    cv2.destroyAllWindows()

    # Print the total number of unique QR codes detected
    print(f"Total distinct QR codes detected in the video: {len(unique_qr_codes)}")
    print("Unique QR codes:", unique_qr_codes)


# Provide the path to your MOV video file
video_path = r'C:\Users\ULUGBEK\Desktop\IMG_0058.MOV'
count_qr_codes_in_video(video_path)
