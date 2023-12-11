# import cv2

# imgpath1 = 'image.jpeg'
# img1 = cv2.imread(imgpath1, 1)

# output = cv2.resize(img1, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)

# cv2.imshow('Output', output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2

imgpath1 = 'image.jpeg'
img1 = cv2.imread(imgpath1, 1)

scale_factor = 1.0  # Initial scale factor

while True:
    # Resize the image based on the updated scale factor
    output = cv2.resize(img1, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)

    cv2.imshow('Output', output)
    
    key = cv2.waitKey(0) & 0xFF
    
    # Zoom in
    if key == ord('i'):
        scale_factor *= 1.1
    # Zoom out
    elif key == ord('o'):
        scale_factor /= 1.1
    # Exit on 'ESC' key
    elif key == 27:
        break

cv2.destroyAllWindows()

