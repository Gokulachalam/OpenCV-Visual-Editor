import cv2
import numpy as np

# Load image from path
def load_image(img_path):
    return cv2.imread(img_path)

# Save image to path
def save_image(img, output_path):
    cv2.imwrite(output_path, img)

# Remove background using color thresholding
def remove_background(img):
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the range of colors to be considered as the background
    lower_bound = np.array([0, 0, 100])
    upper_bound = np.array([179, 100, 255])

    # Create a mask for the background
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask for the background with holes filled
    mask_inv = np.zeros_like(mask)
    cv2.drawContours(mask_inv, contours, -1, (255), thickness=cv2.FILLED)

    # Apply the mask to the image
    removed_img = cv2.bitwise_and(img, img, mask=mask_inv)

    return removed_img

# Remove specified objects based on contour area
def remove_objects(img, min_object_area=1000):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold the image to create a binary mask
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # Find contours in the binary mask
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask for the specified objects
    mask = np.ones_like(img) * 255
    for contour in contours:
        if cv2.contourArea(contour) > min_object_area:
            cv2.drawContours(mask, [contour], -1, (0, 0, 0), thickness=cv2.FILLED)

    # Invert the mask to keep the specified objects
    mask_inv = cv2.bitwise_not(mask)

    # Apply the mask to the image
    removed_img = cv2.bitwise_and(img, mask_inv)

    return removed_img

# Placeholder: Clarity enhancement
def enhance_clarity(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)

    # Resize laplacian to match the size of the original image
    laplacian = cv2.resize(laplacian, (img.shape[1], img.shape[0]))

    enhanced_img = cv2.convertScaleAbs(laplacian)
    enhanced_img = cv2.addWeighted(img, 1.5, enhanced_img, -0.5, 0)
    return enhanced_img

# Placeholder: Color enhancement
def enhance_color(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv[:, :, 1] = hsv[:, :, 1] * 1.5
    enhanced_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return enhanced_img

# Convert the image to black and white
def convert_to_black_and_white(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert Colors
def invert_colors(img):
    inverted_img = cv2.bitwise_not(img)
    return inverted_img

# Oil Painting Effect
def oil_painting_effect(img, size=7, intensity=10):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median blur to the grayscale image
    gray_blurred = cv2.medianBlur(gray, size)

    # Create a 3-channel image for the result
    result = cv2.cvtColor(gray_blurred, cv2.COLOR_GRAY2BGR)

    # Apply bilateral filter to the result
    result = cv2.bilateralFilter(result, 9, 75, 75)

    # Create a mask for edges
    edges = cv2.Canny(gray, 30, 150)

    # Convert the edges mask to BGR
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Combine the result with edges mask using bitwise_and
    oil_painting = cv2.bitwise_and(result, edges)

    return oil_painting


# Blur Background
def blur_background(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale image
    blurred_gray = cv2.GaussianBlur(gray, (15, 15), 0)

    # Create a mask for the background
    _, thresh = cv2.threshold(blurred_gray, 200, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(thresh)

    # Apply the mask to the image
    blurred_background = cv2.bitwise_and(img, img, mask=mask_inv)

    return blurred_background

# Main image processing function
def process_image(img_path, output_path, operation):
    # Load the original image
    image = load_image(img_path)

    # Apply the chosen operation
    if operation == "bg_removal":
        image = remove_background(image)
    elif operation == "clarity_enhancement":
        image = enhance_clarity(image)
    elif operation == "color_enhancement":
        image = enhance_color(image)
    elif operation == "object_removal":
        image = remove_objects(image)
    elif operation == "black_and_white":
        image = convert_to_black_and_white(image)
    elif operation == "invert_colors":
        image = invert_colors(image)
    elif operation == "oil_painting_effect":
        image = oil_painting_effect(image)
    elif operation == "blur_background":
        image = blur_background(image)
    else:
        print("Invalid operation selected.")

    # Save the final result
    save_image(image, output_path)

# Example usage
input_image_path = "/home/gokul/Documents/myproject/image_pro/girl.jpg"
output_image_path = "/home/gokul/Documents/myproject/image_pro/output.jpg"

# Prompt the user for the desired operation
selected_operation = input("Choose an operation (bg_removal, clarity_enhancement, color_enhancement, object_removal, black_and_white, invert_colors, oil_painting_effect, blur_background): ")

# Process the image based on the chosen operation
process_image(input_image_path, output_image_path, selected_operation)
