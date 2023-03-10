from datetime import datetime
from django.db import models


class CustomManager(models.Manager):
    def get_queryset(self):
        return super(CustomManager, self).get_queryset().filter(isDeleted=False, isActive=True)


class CustomModel(models.Model):
    createdAt = models.DateTimeField(db_column='createdAt', default=datetime.now)
    modifiedAt = models.DateTimeField(db_column='modifiedAt', default=datetime.now)
    isDeleted = models.BooleanField(db_column='isDeleted', default=False)
    isActive = models.BooleanField(db_column='isActive', default=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id or not self.createdAt:
            self.createdAt = datetime.now()
        self.modifiedAt = datetime.now()
        super(CustomModel, self).save(*args, **kwargs)