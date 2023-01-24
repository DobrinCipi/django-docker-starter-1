from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
import string


def validate_no_a(value):
    for i in string.ascii_lowercase:
        if i in value:
            raise ValidationError("Caracter nepermis")
        
def validate_no_sepecial_characters(value):
    value = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    for a in value:
        raise ValidationError("Nu sunt persmise caractere speciale")
    
def validate_no_num_in_name(value):
    value = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for a in value:
        raise ValidationError("Nu sunt permise cifre")

# Create your models here.
class Student(models.Model):
    nume = models.TextField(validators=[validate_no_num_in_name, validate_no_sepecial_characters,])
    prenume = models.TextField(validators=[validate_no_num_in_name, validate_no_sepecial_characters,])
    an = models.IntegerField(default=1, db_index=True)
    telefon = models.TextField(null=True, blank=True)
    cnp = models.CharField(unique=True, null=True, blank=True, max_length=13,
                                validators=[MinLengthValidator(13), validate_no_a, validate_no_sepecial_characters,])
            