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