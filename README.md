# Image Steganography Using LSB Technique

## 📌 Project Overview
Image steganography is a technique of hiding secret information within an image in such a way that it remains undetectable to human vision. This project implements **LSB (Least Significant Bit) steganography** to embed and extract hidden messages from images securely.

## 🔍 Problem Statement
With increasing concerns over cybersecurity and data privacy, there is a need for methods that **conceal sensitive information** without drawing attention. Traditional encryption makes data unreadable but also noticeable. **Steganography solves this by embedding messages within images, making them invisible to unauthorized users.**

## 🛠️ Technologies Used
- **Python** – For implementing the encoding and decoding algorithms.
- **OpenCV** – For image processing.
- **NumPy** – For efficient numerical and pixel data manipulation.
- **Least Significant Bit (LSB) Algorithm** – The technique used for embedding hidden messages.

## 🚀 Features
✅ **LSB-based Steganography** – Minimal image distortion while hiding messages.
✅ **Passcode Protection** – Ensures only authorized users can retrieve the hidden message.
✅ **Optimized Processing** – Fast and efficient encoding and decoding.
✅ **Minimal Image Alteration** – The changes are imperceptible to human eyes.
✅ **Secure Data Hiding** – Helps in covert communication and data security.

## 📥 Installation
To set up the project, follow these steps:

1. **Clone this repository**
   ```sh
   git clone https://github.com/Onkargiri29/Image-Steganography-Using-LSB-Technique.git
   cd Image-Steganography-Using-LSB-Technique
   ```
2. **Install Dependencies**
   ```sh
   pip install opencv-python numpy
   ```

## 📌 Usage
### **Encoding (Hiding a Message in an Image)**
```sh
python encode.py --image input.jpg --message "Your secret message" --output output.png --password yourpassword
```
- `--image` : Input image file.
- `--message` : Secret text message to hide.
- `--output` : Name of the output stego-image.
- `--password` : Passcode for encryption.

### **Decoding (Extracting the Hidden Message)**
```sh
python decode.py --image output.png --password yourpassword
```
- `--image` : The stego-image containing the hidden message.
- `--password` : Passcode for decryption.

## 📷 Results
This project will include **screenshots of the following**:
- **Original Image vs. Stego-Image** (visually identical)
- **Encoding Process** (Hiding text inside an image)
- **Decoding Process** (Extracting the hidden message)

## 🔮 Future Scope
🚀 **Support for More File Types** – Hide files like PDFs, text, and audio instead of just messages.  
🚀 **Encryption Before Embedding** – Adding an extra layer of security.  
🚀 **Graphical User Interface (GUI)** – To make it user-friendly.  
🚀 **Resistant to Image Compression** – Enhance robustness against noise and compression.  

## 📝 License
This project is open-source and available under the **MIT License**.

---
