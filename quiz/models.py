from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)  # 'A', 'B', 'C', or 'D'

    def __str__(self):
        return self.text

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate session with a user
    name = models.CharField(max_length=100)  # User-entered name for the session
    questions = models.ManyToManyField(Question)
    progress = models.JSONField(default=dict)  # {"1": "A", "2": "B", ...} (question_id -> selected option)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.user.username})"

