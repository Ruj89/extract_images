import os
import sys
from PyPDF2 import PdfReader
from PIL import Image

def extract_images_from_pdf(pdf_path):
    # Check if the PDF file exists
    if not os.path.exists(pdf_path):
        print(f"Error: The file '{pdf_path}' does not exist.")
        return
    
    # Get the directory of the PDF file
    output_folder = os.path.dirname(pdf_path)
    
    # Read the PDF
    reader = PdfReader(pdf_path)
    image_count = 0
    
    # Iterate through the pages
    for page_number, page in enumerate(reader.pages, start=1):
        resources = page.get("/Resources", {})
        x_objects = resources.get("/XObject", {})
        
        if isinstance(x_objects, dict):  # Ensure we have a dictionary of XObjects
            x_objects = x_objects.get_object()  # Resolve indirect objects

            for obj_name, obj_ref in x_objects.items():
                obj = obj_ref.get_object()  # Dereference the object

                if obj.get("/Subtype") == "/Image":
                    # Extract image data
                    data = obj.get_data()
                    width = obj.get("/Width")
                    height = obj.get("/Height")
                    color_space = obj.get("/ColorSpace")
                    
                    # Save the image
                    mode = "RGB" if color_space == "/DeviceRGB" else "P"
                    img = Image.frombytes(mode, (width, height), data)
                    image_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(pdf_path))[0]}_page_{page_number}_img_{image_count + 1}.png")
                    img.save(image_path)
                    
                    image_count += 1
    
    print(f"Extraction completed: {image_count} images found and saved in '{output_folder}'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_images.py <pdf_path>")
    else:
        pdf_file = sys.argv[1]
        extract_images_from_pdf(pdf_file)
