from django.db import models


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


class CollageInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    collage_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Collage_info'


class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    collage = models.CharField(max_length=255, blank=True, null=True)
    collage_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Teacher'


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


class DayXInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    class_id = models.IntegerField(blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    class_num = models.IntegerField(blank=True, null=True)
    lecture_id = models.IntegerField(blank=True, null=True)
    lecture_name = models.CharField(max_length=255, blank=True, null=True)
    lecture_type = models.CharField(max_length=255, blank=True, null=True)
    attend_num = models.IntegerField(blank=True, null=True)
    day_diff = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'day_x_info'


class Lecture(models.Model):
    id = models.IntegerField(primary_key=True)
    lecture_name = models.CharField(max_length=255, blank=True, null=True)
    lecture_type = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lecture'


class ScoreInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    score = models.FloatField(blank=True, null=True)
    class_id = models.IntegerField(blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)
    teacher_name = models.CharField(max_length=255, blank=True, null=True)
    collage_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'score_info'


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    college = models.CharField(max_length=255, blank=True, null=True)
    college_id = models.IntegerField(blank=True, null=True)
    class_id = models.IntegerField(blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    teacher_name = models.CharField(max_length=255, blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'