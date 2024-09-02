# Generated by Django 5.1 on 2024-09-02 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=265)),
                ('author', models.CharField(max_length=100)),
                ('pages', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('review', models.TextField()),
                ('isbn', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
