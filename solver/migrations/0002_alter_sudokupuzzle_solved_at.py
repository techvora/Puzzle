# Generated by Django 5.0.2 on 2024-06-02 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sudokupuzzle',
            name='solved_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
