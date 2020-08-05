from django.db import models


class contact(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=45,null=False)
    lastname = models.CharField(max_length=45,null=False)

    class Meta:
        db_table='contactinfo'
