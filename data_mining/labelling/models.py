from django.db import models


class Label(models.Model):
    line = models.IntegerField()
    TYPES = (
        (0, 'BAD'),
        (1, 'GOOD'),
    )
    option1 = models.CharField(max_length=100, null=False)
    option2 = models.CharField(max_length=100, null=False)
    option3 = models.CharField(max_length=100, null=False)
    option4 = models.CharField(max_length=100, null=False)
    result = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    is_good = models.IntegerField(choices=TYPES, default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'label'
        default_permissions = ()
