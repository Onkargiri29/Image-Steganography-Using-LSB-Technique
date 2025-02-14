import cv2
import numpy as np

def reveal_message(image_path, key):
    """Extracts a hidden message from an image by reading the LSB of pixels."""

    # Load the encoded image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load image. Check the file path.")
        return

    # Flatten image for efficient processing
    flat_image = image.flatten()

    # Extract the LSBs to retrieve the hidden binary message
    binary_message = ''.join(str(flat_image[i] & 1) for i in range(len(flat_image)))

    # Convert binary data into text
    characters = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    hidden_text = ''.join(chr(int(char, 2)) for char in characters)

    # Check for the termination marker "<END>"
    if "<END>" in hidden_text:
        extracted_key, secret_content = hidden_text.split("::", 1)
        secret_content = secret_content.split("<END>")[0]  # Remove termination marker

        if extracted_key == key:
            print("🔓 Successfully retrieved message:", secret_content)
        else:
            print("❌ Incorrect passcode! Access denied.")
    else:
        print("❌ No hidden message detected in the image.")

if __name__ == "__main__":
    # Get user input
    img_path = input("Enter the image file path: ")
    security_key = input("Enter the passcode to decrypt: ")

    # Call the function to decode
    reveal_message(img_path, security_key)
