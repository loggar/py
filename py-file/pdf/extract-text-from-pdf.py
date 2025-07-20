import PyPDF2
import os


def extract_text_from_pdf(pdf_path, output_txt_path):
    """
    Extract text from a PDF file and save it to a text file.

    Args:
        pdf_path (str): Path to the input PDF file
        output_txt_path (str): Path to the output text file
    """
    try:
        # Open the PDF file in binary read mode
        with open(pdf_path, "rb") as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Get the number of pages
            num_pages = len(pdf_reader.pages)
            print(f"Processing {num_pages} pages...")

            # Extract text from all pages
            extracted_text = ""
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                extracted_text += f"\n--- Page {page_num + 1} ---\n"
                extracted_text += text

                # Print progress for large files
                if (page_num + 1) % 50 == 0:
                    print(f"Processed {page_num + 1} pages...")

            # Save extracted text to output file
            with open(output_txt_path, "w", encoding="utf-8") as txt_file:
                txt_file.write(extracted_text)

            print(f"Text extraction completed successfully!")
            print(f"Extracted text saved to: {output_txt_path}")
            print(f"Total pages processed: {num_pages}")

    except FileNotFoundError:
        print(f"Error: PDF file not found at {pdf_path}")
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Specify your PDF file path and output text file path
    pdf_file_path = "./_tmp/_in_pdf/input.pdf"  # Replace with your PDF file path
    output_file_path = "./_tmp/_out_txt/extracted_text.txt"  # Output text file

    # Check if PDF file exists
    if os.path.exists(pdf_file_path):
        extract_text_from_pdf(pdf_file_path, output_file_path)
    else:
        print(f"Please make sure the PDF file exists at: {pdf_file_path}")
