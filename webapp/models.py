from django.db import models
from django.utils import timezone
from django.db.models import TextChoices


class StatusChoice(TextChoices):
    ACTIVE = 'active', 'Активно'
    BLOCKED = 'blocked', 'Заблокированно'


class Book(models.Model):
    email = models.EmailField(verbose_name="Почта", max_length=100, null=False, blank=False)
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=300, null=False, blank=False, verbose_name="Статус",
                              choices=StatusChoice.choices, default=StatusChoice.ACTIVE)
    is_deleted = models.BooleanField(verbose_name='Удалено', null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время и дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время и дата обновления")

    def __str__(self):
        return f"{self.author} - {self.status}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книга'


