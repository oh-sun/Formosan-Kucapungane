from tkinter import Tk
from tkinter.filedialog import askopenfilename
import easyocr

Tk().withdraw()

image_path = askopenfilename(
    title="Select a screenshot or image",
    filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff")]
)

if image_path:

    print("Loading OCR model...")

    # English + Traditional Chinese
    reader = easyocr.Reader(['en','ch_tra'])

    print("\nReading text...\n")

    results = reader.readtext(image_path)

    print("Detected text:\n")

    for bbox, text, confidence in results:
        print(f"{text} (confidence: {confidence:.2f})")

else:
    print("No image selected.")
