from django.db import models


class Job(models.Model):  # Перейменувати на Job
    SRC_DOU = 'dou'
    SRC_OTHER = 'other'
    SRC_CHOICES = [
        (SRC_DOU, SRC_DOU),
        (SRC_OTHER, SRC_OTHER),
    ]
    name = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=250, choices=SRC_CHOICES, default=SRC_OTHER)
    url = models.URLField(max_length=250, unique=True)
    salary_info = models.TextField(max_length=250, null=True)  # переробити на positive integer field
    place_info = models.TextField(max_length=250, null=True)  # спробувати зробити через array field
    # years exp додати поле small integer field 0, 1
    # description - повний текст з опису вакансії
    # publish date - дата публікації вакансії date field


    def __str__(self):
        return str(self.pk)


    # зробити класс схожий вакансій,