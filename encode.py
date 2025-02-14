import cv2
import numpy as np

def hide_message(image_path, message, key, output_path="hidden_image.png"):
    
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load image. Check the file path.")
        return

    # Add key to the message to ensure authentication
    message = key + "::" + message + "<END>"  # "<END>" acts as a termination marker

    # Convert the message to binary
    binary_data = ''.join(format(ord(char), '08b') for char in message)

    # Flatten the image for faster processing
    flat_image = image.flatten()

    if len(binary_data) > len(flat_image):
        print("Error: The message is too long for the selected image.")
        return

    # Embed the message bits into the image's LSB
    for index, bit in enumerate(binary_data):
        flat_image[index] = (flat_image[index] & ~1) | int(bit)

    # Restore the modified pixel values into the image shape
    encoded_image = flat_image.reshape(image.shape)

    # Save the output image
    cv2.imwrite(output_path, encoded_image)
    print(f"✅ Message successfully embedded in {output_path}")

if __name__ == "__main__":
    # Get user input
    img_path = input("Enter the image file path: ")
    secret_text = input("Enter the message to hide: ")
    security_key = input("Enter a passcode for security: ")

    # Call the function to encode
    hide_message(img_path, secret_text, security_key)
