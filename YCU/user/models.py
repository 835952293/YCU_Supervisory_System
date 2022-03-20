from django.db import models

# Create your models here.

class ClassInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    class_id = models.IntegerField(blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    class_type = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)
    tercher_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Class_info'


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    account_id = models.IntegerField(blank=True, null=True)
    password = models.IntegerField(blank=True, null=True)
    user_type = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'