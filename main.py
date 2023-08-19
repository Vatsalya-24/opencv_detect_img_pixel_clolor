import cv2
import numpy as np

last_cursor_position = (-1, -1)  # Initialize to an invalid position
input_color = None  # Initialize the selected input color as None
clicked = False  # Variable to track if a pixel has been clicked

def on_mouse(event, x, y, flags, param):
    global last_cursor_position, input_color, clicked
    if event == cv2.EVENT_MOUSEMOVE:
        last_cursor_position = (x, y)
    elif event == cv2.EVENT_LBUTTONDOWN:
        last_cursor_position = (x, y)
        input_color = tuple(map(int, image[y, x]))
        clicked = True

# Load an image
image_path = 'Input.jpg'
image = cv2.imread(image_path)

# Create a window to display the image
cv2.namedWindow('Image')

# Set the mouse callback function
cv2.setMouseCallback('Image', on_mouse)

while not clicked:
    image_copy = image.copy()
    if last_cursor_position != (-1, -1):
        x, y = last_cursor_position
        pixel_color = image[y, x]
        pixel_color_text = f"B={pixel_color[0]}, G={pixel_color[1]}, R={pixel_color[2]}"
        cv2.putText(image_copy, pixel_color_text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    
    cv2.imshow('Image', image_copy)
    key = cv2.waitKey(1)
    if key == 27:  # Press Esc to exit
        break

cv2.destroyAllWindows()

if input_color is not None:
    print("Selected Color:", input_color)
