from django.db import models
from authentication.models import User
# Create your models here.

class Skill(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=20)
    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"
    def __str__(self):
        return self.name

class Vacancy(models.Model):
    STATUS  = [
        ("draft", "Черновик"),
        ("open", "Открыта"),
        ("close", "Закрыта"),
    ]
    slug = models.SlugField(max_length=50)
    text = models.CharField(max_length=2000)
    status = models.CharField(max_length=6, choices=STATUS, default = "draft")
    created = models.DateField(auto_now_add=True)# like default=datetime.date.now
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    skills = models.ManyToManyField(Skill)

    likes = models.IntegerField(default = 0)

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.slug

    @property
    def username(self):
        return self.user if self.user else None



