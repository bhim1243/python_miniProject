import PyPDF2

def unlock_pdf(input_path, output_path, password):
    with open(input_path, 'rb') as input_file:
        pdf_reader = PyPDF2.PdfReader(input_file)
        if pdf_reader.isEncrypted:
            pdf_reader.decrypt(password)
            pdf_writer = PyPDF2.PdfWriter()

            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.getPage(page_num))

            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)
            print("PDF unlocked successfully!")
        else:
            print("PDF is not password protected.")

# Define the input PDF file path
input_pdf = "H:/college note/first sem/to/binary-system.pdf"
output_pdf = "unlocked.pdf"
password = "your_password"  # Replace 'your_password' with the actual password

unlock_pdf(input_pdf, output_pdf, password)
