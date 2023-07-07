from io import BytesIO

import qrcode

from django.conf import settings
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from .models import Student


def generate_pdf(qr_code_titles, qr_codes_per_row=6, qr_code_width=70, qr_code_height=70, space=10):
    buffer = BytesIO()

    # Calculate the maximum number of QR codes per page based on qr_codes_per_row
    max_qr_codes_per_page = qr_codes_per_row * int(A4[1] // (qr_code_height + space))

    # Calculate the number of pages required
    total_pages = len(qr_code_titles) // max_qr_codes_per_page
    if len(qr_code_titles) % max_qr_codes_per_page != 0:
        total_pages += 1

    pdf = canvas.Canvas(buffer, pagesize=A4)
    # Iterate through the QR code titles
    for page in range(int(total_pages)):
        # Create a new PDF object for each page
        # Set the font and font size
        pdf.setFont("Helvetica", 5)

        # Set the initial position for drawing on the page
        x = 50
        y = A4[1] - 100

        # Calculate the starting and ending indices for the current page
        start_index = page * max_qr_codes_per_page
        end_index = start_index + max_qr_codes_per_page

        # Iterate through the QR code titles for the current page
        for i, (title, url) in enumerate(qr_code_titles[start_index: end_index]):
            # Calculate the position for drawing the QR codes and titles
            qr_code_x = x + (i % qr_codes_per_row) * (qr_code_width + space)
            qr_code_y = y - (i // qr_codes_per_row) * (qr_code_height + space)

            title_x = qr_code_x + qr_code_width/2
            title_y = qr_code_y + qr_code_height - space*7

            # Generate the QR code image
            qr = qrcode.make(url)

            # Draw the QR code on the PDF
            qr_image = qr.resize((qr_code_width, qr_code_height))
            pdf.drawInlineImage(qr_image, qr_code_x, qr_code_y)

            # Draw the title text below the QR code
            pdf.setFont("Helvetica", 10)
            pdf.drawCentredString(title_x, title_y, title)

        # Save the PDF content for the current page
        pdf.showPage()

    # Save the entire PDF
    pdf.save()

    # Return the PDF bytes
    return buffer.getvalue()


def generate_qr_code_titles(ids: list[int]):
    base_url = settings.BASE_URL + "/student/"
    qr_code_titles = []

    students = Student.objects.filter(id__in=ids).distinct()

    for student in students:
        qr_code_titles.append((student.document_number, base_url+str(student.id)))

    return qr_code_titles
