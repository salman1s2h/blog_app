# Generated by Django 4.2.9 on 2024-01-18 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_birth_date_user_gender_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=191, null=True, verbose_name='Name'),
        ),
    ]
