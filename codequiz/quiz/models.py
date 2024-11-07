from django.db import models
from datetime import datetime

class Submission(models.Model):
    enrollment_number = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
    branch = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    datetime = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return f"{self.enrollment_number} - {self.name}"

class Results(models.Model):
    enrollment_number = models.CharField(max_length=20, primary_key=True)
    score = models.IntegerField()
    q1 = models.CharField(max_length=50)
    q2 = models.CharField(max_length=50)
    q3 = models.CharField(max_length=50)
    q4 = models.CharField(max_length=50)
    q5 = models.CharField(max_length=50)
    q6 = models.CharField(max_length=50)
    q7 = models.CharField(max_length=50)
    q8 = models.CharField(max_length=50)
    q9 = models.CharField(max_length=50)
    q10 = models.CharField(max_length=50)
    q11 = models.CharField(max_length=50)
    q12 = models.CharField(max_length=50)
    q13 = models.CharField(max_length=50)
    q14 = models.CharField(max_length=50)
    q15 = models.CharField(max_length=50)
    q16 = models.CharField(max_length=50)
    q17 = models.CharField(max_length=50)
    q18 = models.CharField(max_length=50)
    q19 = models.CharField(max_length=50)
    q20 = models.CharField(max_length=50)
    q21 = models.CharField(max_length=50)
    q22 = models.CharField(max_length=50)
    q23 = models.CharField(max_length=50)
    q24 = models.CharField(max_length=50)
    q25 = models.CharField(max_length=50)
    q26 = models.CharField(max_length=50)
    q27 = models.CharField(max_length=50)
    q28 = models.CharField(max_length=50)
    q29 = models.CharField(max_length=50)
    q30 = models.CharField(max_length=50)
    q31 = models.CharField(max_length=50)
    q32 = models.CharField(max_length=50)
    q33 = models.CharField(max_length=50)
    q34 = models.CharField(max_length=50)
    q35 = models.CharField(max_length=50)
    q36 = models.CharField(max_length=50)
    q37 = models.CharField(max_length=50)
    q38 = models.CharField(max_length=50)
    q39 = models.CharField(max_length=50)
    q40 = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.enrollment_number} - {self.score}"