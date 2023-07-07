from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="Familiya")
    last_name = models.CharField(max_length=200, verbose_name="Ism")
    middle_name = models.CharField(max_length=200, verbose_name="Otasining Ismi")
    passport_number = models.CharField(max_length=150, verbose_name="Passport raqami")
    birth_date = models.CharField(max_length=50, verbose_name="Tug'ulgan sanasi")
    otm = models.CharField(max_length=200, verbose_name="OTM")
    speciality = models.CharField(max_length=200, verbose_name="Mutaxasisligi")
    study_type = models.CharField(max_length=100, verbose_name="Ta'lim turi")
    edu_type = models.CharField(max_length=100, verbose_name="Ta'lim shakli")
    document_number = models.CharField(max_length=100, verbose_name="Diplom raqami")
    registered_date = models.CharField(max_length=50)

    def __str__(self) -> str:
        return "{}{}".format(self.first_name, self.last_name)
