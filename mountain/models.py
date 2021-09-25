from django.db import models
from django.urls import reverse


class Trail(models.Model):
    title = models.CharField(max_length=150, verbose_name='Hiking Trail')
    content = models.TextField(blank=True, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated Date')
    photo = models.ImageField()
    difficulty = models.ForeignKey('Difficulty', on_delete=models.PROTECT, null=True, verbose_name='Difficulty')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('trail_list', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Trail'
        verbose_name_plural = 'Trails'
        ordering = ['-created_at']


class Difficulty(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Degree of Difficulty')

    def get_absolute_url(self):
        return reverse('difficulty', kwargs={"difficulty_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Difficulty'
        verbose_name_plural = 'Difficulties'
        ordering = ['title']


# class Employee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE())
#     department = models.CharField(max_length=100)
#
# # for access to DB:
# # u = User.objects.get(username='tod36')
# # tod36_department = u.employee.department
