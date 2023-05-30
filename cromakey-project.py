import cv2
import numpy as np

def apply_chroma_key(frame, background, color_patch, tolerance, smoothing, color_projection):
    background_resized = cv2.resize(background, (frame.shape[1], frame.shape[0]))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    green_range = np.array([color_patch - tolerance, 100, 100], np.uint8), np.array([color_patch + tolerance, 255, 255], np.uint8)
    mask = cv2.inRange(hsv, green_range[0], green_range[1])
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((smoothing, smoothing), np.uint8))

    foreground = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(mask))
    background_masked = cv2.bitwise_and(background_resized, background_resized, mask=mask)
    result = cv2.add(foreground, background_masked)
    if color_projection:
        result = cv2.addWeighted(frame, 0.3, result, 0.7, 0)

    return result

def on_trackbar(val):
    pass

if __name__ == '__main__':
    input_video = 'greenscreen-asteroid.mp4'
    background_image = 'space.jpg'
    cap = cv2.VideoCapture(input_video)
    background = cv2.imread(background_image)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = 'asteroid_space.mp4'

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    cv2.namedWindow('Chroma Key')
    cv2.createTrackbar('Color Patch', 'Chroma Key', 60, 180, on_trackbar)
    cv2.createTrackbar('Tolerance', 'Chroma Key', 30, 180, on_trackbar)
    cv2.createTrackbar('Smoothing', 'Chroma Key', 5, 50, on_trackbar)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        color_patch = cv2.getTrackbarPos('Color Patch', 'Chroma Key')
        tolerance = cv2.getTrackbarPos('Tolerance', 'Chroma Key')
        smoothing = cv2.getTrackbarPos('Smoothing', 'Chroma Key')

        result = apply_chroma_key(frame, background, color_patch, tolerance, smoothing, False)

        cv2.imshow('Chroma Key', result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        out.write(result)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

#%%

#%%
