# PDF Image Extractor

A Python script to extract all images from a PDF file and save them as image files in the same directory as the PDF.

## Features
- Extracts all embedded images from a PDF file.
- Saves images in the same folder as the input PDF.
- Outputs images in `.png` format with filenames indicating the page and image numbers.

## Prerequisites
Ensure Python is installed on your system. The required Python libraries are listed in the `requirements.txt` file.

Install the dependencies using pip:
```bash
pip install -r requirements.txt
```

## Usage
1. Save the script as `extract_images.py`.
2. Run the script from the command line, providing the path to your PDF file as an argument:

   ```bash
   python extract_images.py /path/to/document.pdf
   ```

3. The script will save all extracted images in the same directory as the input PDF. Filenames will follow the format:
   ```
   document_page_<page_number>_img_<image_number>.png
   ```

### Example
If the input PDF is located at `/home/user/documents/sample.pdf`, run:
```bash
python extract_images.py /home/user/documents/sample.pdf
```

The extracted images will be saved in `/home/user/documents/` with filenames like:
```
sample_page_1_img_1.png
sample_page_2_img_1.png
```

## License
This script is provided under the MIT License. You are free to use, modify, and distribute it.

## Contributing
If you find any issues or want to suggest improvements, feel free to open an issue or submit a pull request.