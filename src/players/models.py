from django.db import models



DEXTERITY = {
    "R": "Right",
    "L": "Left",
    "AR": "Ambidextrous Right",
    "AL": "Ambidextrous Left",
}

class Player(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dexterity = models.CharField(
        max_length=2,
        choices=DEXTERITY,
        default="R",
    )
    golf_dexterity = models.CharField(
        max_length=2,
        choices=DEXTERITY,
        default="R",
    )

