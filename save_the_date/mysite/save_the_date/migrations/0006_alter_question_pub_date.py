# Generated by Django 4.2.4 on 2023-08-26 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('save_the_date', '0005_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='pub_date'),
        ),
    ]