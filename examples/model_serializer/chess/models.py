from django.db import models


class ChessPlayer(models.Model):

    email = models.EmailField()
    birth_date = models.DateField()
    pesel = models.TextField()
    rodo_accepted = models.BooleanField()
    first_name = models.TextField(max_length=20)
    second_name = models.TextField(max_length=20, null=True)
