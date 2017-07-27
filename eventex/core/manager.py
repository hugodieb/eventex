from django.db import models

class KindQueryset(models.QuerySet):
    def emails(self):
        return self.filter(Kind=self.model.EMAIL)

    def phones(self):
        return  self.filter(Kind=self.model.PHONE)


class KindContactManager(models.Manager):
    def get_queryset(self):
        return KindQueryset(self.model, using=self._db)

    def emails(self):
        return self.get_queryset().emails()

    def phones(self):
        return self.get_queryset().phones()

class PeriodManager(models.Manager):
    MIDDAY = '12:00'

    def at_morning(self):
        return self.filter(start__lt=self.MIDDAY)

    def at_afternoon(self):
        return self.filter(start__gte=self.MIDDAY)