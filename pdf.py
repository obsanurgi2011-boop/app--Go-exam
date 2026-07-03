from reportlab.pdfgen import canvas
import os
import datetime


def generate_pdf(name, exam):
    folder = "certificates"
    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(
        folder,
        f"{name}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
    )

    c = canvas.Canvas(file_path)
    c.drawString(100, 750, "EXAM CERTIFICATE")
    c.drawString(100, 700, f"Name: {name}")
    c.drawString(100, 650, f"Exam: {exam}")
    c.save()

    return file_path
