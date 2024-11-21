from fpdf import FPDF

# Create a PDF instance
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add content to the PDF
pdf.set_font("Arial", style="B", size=16)
pdf.cell(200, 10, txt="Appointment Confirmation", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Astradental Services", ln=True, align="C")
pdf.cell(200, 10, txt="Westlands, Nairobi", ln=True, align="C")
pdf.cell(200, 10, txt="Phone: +254-700-123-456", ln=True, align="C")
pdf.cell(200, 10, txt="Email: info@astradental.co.ke", ln=True, align="C")
pdf.ln(20)

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Date: 20th November 2024", ln=True)
pdf.ln(10)
pdf.cell(200, 10, txt="To Whom It May Concern,", ln=True)
pdf.ln(10)

class PDFWithLogo(FPDF):
    def header(self):
        # Add logo
        self.image('/mnt/data/dental_logo.png', 10, 8, 33)  # Adjust as needed for logo file path and size
        self.set_font('Arial', 'B', 12)
        self.cell(80)  # Move to the right
        self.cell(30, 10, 'Astradental Services', 0, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(0, 10, 'Westlands, Nairobi | Phone: +254-700-123-456 | Email: info@astradental.co.ke', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        # Add a footer with page number
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')


# Create a PDF instance
pdf = PDFWithLogo()
pdf.add_page()

# Add content
pdf.set_fill_color(200, 220, 255)  # Light blue fill for sections
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Appointment Invoice", ln=True, align="C", fill=True)
pdf.ln(10)

pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "Appointment Details", ln=True, fill=True)
pdf.ln(5)
pdf.set_font("Arial", size=11)
pdf.cell(0, 10, "Patient Name: Victor Mandere Mose", ln=True)
pdf.cell(0, 10, "Appointment Date: Friday, 22nd November 2024", ln=True)
pdf.cell(0, 10, "Appointment Time: 7:00 PM", ln=True)
pdf.cell(0, 10, "Location: Astradental Services, Westlands, Nairobi", ln=True)
pdf.ln(10)

pdf.set_font("Arial", "B", size=12)
pdf.cell(0, 10, "Insurance Information", ln=True, fill=True)
pdf.ln(5)
pdf.set_font("Arial", size=11)
pdf.cell(0, 10, "Insurance Provider: Minet Kenya Insurance Brokers", ln=True)
pdf.cell(0, 10, "Member Number: MRMA-2416", ln=True)
pdf.ln(10)

pdf.set_font("Arial", "B", size=12)
pdf.cell(0, 10, "Contact Us", ln=True, fill=True)
pdf.ln(5)
pdf.set_font("Arial", size=11)
pdf.cell(0, 10, "Phone: +254-700-123-456", ln=True)
pdf.cell(0, 10, "Email: info@astradental.co.ke", ln=True)

# Save the PDF
file_path_invoice = r"C:\Users\Mosev\Desktop\Victor_Dental_Invoice.pdf"
pdf.output(file_path_invoice)

file_path_invoice


# Use the generated logo in the PDF design

logo_path = r"C:\Users\Mosev\Desktop\A_minimalist_and_modern_logo_design_for_a_dental_c.png"

# Create a PDF with the logo included
pdf = PDFWithLogo()
pdf.add_page()

# Adjust header to include the generated logo
class PDFWithGeneratedLogo(PDFWithLogo):
    def header(self):
        # Add generated logo
        self.image(logo_path, 10, 8, 33)  # Adjust as needed for logo file path and size
        self.set_font('Arial', 'B', 12)
        self.cell(80)  # Move to the right
        self.cell(30, 10, 'Astradental Services', 0, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(0, 10, 'Westlands, Nairobi | Phone: +254-700-123-456 | Email: info@astradental.co.ke', 0, 1, 'C')
        self.ln(10)

# Generate the invoice with the new header
pdf = PDFWithGeneratedLogo()
pdf.add_page()

# Add content
pdf.set_fill_color(200, 220, 255)  # Light blue fill for sections
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Appointment Invoice", ln=True, align="C", fill=True)
pdf.ln(10)

pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "Appointment Details", ln=True, fill=True)
pdf.ln(5)
pdf.set_font("Arial", size=11)
pdf.cell(0, 10, "Patient Name: Victor Mandere Mose", ln=True)
pdf.cell(0, 10, "Appointment Date: Friday, 22nd November 2024", ln=True)
pdf.cell(0, 10, "Appointment Time: 7:00 PM", ln=True)
pdf.cell(0, 10, "Location: Astradental Services, Westlands, Nairobi", ln=True)
pdf.ln(10)

pdf.set_font("Arial", "B", size=12)
pdf.cell(0, 10, "Insurance Information", ln=True, fill=True)
pdf.ln(5)
pdf.set_font("Arial", size=11)
pdf.cell(0, 10, "Insurance Provider: Minet Kenya Insurance Brokers", ln=True)
pdf.cell(0, 10, "Member Number: MRMA-2416", ln=True)
pdf.ln(10)

pdf.set_font("Arial", "B", size=12)
pdf.cell(0, 10, "Contact Us", ln=True, fill=True)
pdf.ln(5)
pdf.set_font("Arial", size=11)
pdf.cell(0, 10, "Phone: +254-700-123-456", ln=True)
pdf.cell(0, 10, "Email: info@astradental.co.ke", ln=True)

# Save the PDF
file_path_invoice_with_logo = r"C:\Users\Mosev\Desktop\Victor_Dental_Invoice_with_Logo.pdf"
pdf.output(file_path_invoice_with_logo)
