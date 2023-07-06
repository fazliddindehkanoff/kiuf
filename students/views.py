from io import BytesIO

import pandas as pd

from django.db import transaction
from django.http import FileResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Student
from .utils import generate_pdf, generate_qr_code_titles


@login_required(login_url="login")
def home_view(request):
    if request.method == "POST" and request.FILES:
        file = request.FILES['file']
        try:
            student_ids: list[int] = []
            sheets = pd.read_excel(file, sheet_name=None)

            with transaction.atomic():
                for sheet_name, df in sheets.items():
                    for _, row in df.iterrows():
                        student = Student(
                            first_name=row['Familiya'],
                            last_name=row['Ismi'],
                            middle_name=row['Otasining ismi'],
                            passport_number=row['Pasport Raqami'],
                            birth_date=row['Tug\'ilgan sanasi'],
                            otm=row['OTM'],
                            speciality=row['Mutaxassislik'],
                            study_type=row['Ta\'lim turi'],
                            edu_type=row['Ta\'lim shakli'],
                            document_number=row['Diplom raqami'],
                            registered_date=row['Qayd sanasi']
                        )
                        student.save()
                        student_ids.append(student.id)

            qr_code_titles = generate_qr_code_titles(ids=student_ids)
            pdf_bytes = generate_pdf(qr_code_titles)

            response = FileResponse(BytesIO(pdf_bytes))
            response['Content-Type'] = 'application/pdf'
            response['Content-Disposition'] = 'attachment; filename="results.pdf"'

            return response

        except Exception as e:
            messages.error(request, f"Error reading Excel file: {str(e)}")

    return render(request, "home.html")


def students_view(request, pk):
    student = Student.objects.filter(pk=pk).first()
    if student:
        return render(request, "student_detail.html", {"student": student})
    return render(request, "404.html")
