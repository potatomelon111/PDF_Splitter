import sys
import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_path):
    # Get the directory, file name, and base name of the input PDF.
    directory, filename = os.path.split(input_path)
    basename, ext = os.path.splitext(filename)
    
    # Create a new folder inside the original directory with the same base name.
    output_folder = os.path.join(directory, basename)
    os.makedirs(output_folder, exist_ok=True)
    
    # Define output file paths inside the new folder.
    odd_output_path = os.path.join(output_folder, f"{basename}_odd{ext}")
    even_output_path = os.path.join(output_folder, f"{basename}_even{ext}")
    
    try:
        # Open the PDF file.
        reader = PdfReader(input_path)
        odd_writer = PdfWriter()
        even_writer = PdfWriter()
        
        # Iterate over all pages (0-indexed).
        for i, page in enumerate(reader.pages):
            if (i + 1) % 2 == 1:
                odd_writer.add_page(page)
            else:
                even_writer.add_page(page)
        
        # Write the odd pages to the output PDF.
        with open(odd_output_path, 'wb') as odd_file:
            odd_writer.write(odd_file)
            
        # Write the even pages to the output PDF.
        with open(even_output_path, 'wb') as even_file:
            even_writer.write(even_file)
        
        print(f"✔️ Processed: {filename}")
        print(f"    ↳ Odd pages:  {odd_output_path}")
        print(f"    ↳ Even pages: {even_output_path}")
    
    except Exception as e:
        print(f"❌ Failed to process {filename}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_pdf.py file1.pdf file2.pdf ...")
        sys.exit(1)

    for input_path in sys.argv[1:]:
        split_pdf(input_path)
