# Generated by Django 3.2.6 on 2021-08-24 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Degree of Difficulty')),
            ],
            options={
                'verbose_name': 'Difficulty',
                'verbose_name_plural': 'Difficulties',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Hiking Trail')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('photo', models.ImageField(upload_to='')),
                ('views', models.IntegerField(default=0)),
                ('difficulty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mountain.difficulty', verbose_name='Difficulty')),
            ],
            options={
                'verbose_name': 'Trail',
                'verbose_name_plural': 'Trails',
                'ordering': ['-created_at'],
            },
        ),
    ]
