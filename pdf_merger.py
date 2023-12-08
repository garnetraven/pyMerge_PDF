import PyPDF2
import os

def merge_pdfs(output_path, pdf_files):
    """
    Merge multiple PDF files into a single PDF document.

    Parameters:
        Output_path: The path of the output PDF file.
        pdf_files: The list of paths to the PDF files to merge.

    Returns: 
        None

    """

    pdf_merger = PyPDF2.PdfMerger()

    # Append each PDF to the end of the previous one
    for pdf_file in pdf_files:
        pdf_merger.append(pdf_file)

    # Write to an output PDF document
    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)

if __name__ == '__main__':
    # Specify PDF files to merge
    pdf_files_to_merge = ['file1.pdf', 'file2.pdf', 'file3.pdf']

    # Specific output file path
    output_pdf_path = 'merged_ouput.pdf'

    # Check if output file already exists and ask for confirmation to overwrite
    if os.path.exists(output_pdf_path):
        user_input = input(f"The file '{output_pdf_path}' already exists. Do you want to overwrite it? (y/n): ")
        if user_input.lower() != 'y':
            print('Operation canceled. No changes made.')
            exit()

    # Merge the PDFs
    merge_pdfs(output_pdf_path, pdf_files_to_merge)

    print(f"PDF files merfed successfully. Output saved to: '{output_pdf_path}'")