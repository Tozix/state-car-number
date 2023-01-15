import uuid

from django.core.validators import RegexValidator
from django.db import models


class CarNumer(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    plate = models.CharField(
        'Гос. номер',
        unique=True,
        max_length=9,
        validators=[
            RegexValidator(
                regex='^[ABEKMHOPCTYX]\d{3}[ABEKMHOPCTYX]{2}$',
                message='Недопустимые символы в номере!'
            )
        ])

    class Meta:
        verbose_name = 'Номер машины'
        verbose_name_plural = 'Номера машин'
