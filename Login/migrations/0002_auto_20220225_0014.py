# Generated by Django 3.2.9 on 2022-02-24 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Create1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('DOB', models.DateField()),
                ('Address', models.TextField()),
                ('Phone', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Create',
        ),
    ]