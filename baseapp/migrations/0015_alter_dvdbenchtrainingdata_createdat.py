# Generated by Django 3.2.8 on 2021-10-30 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0014_dvdbenchtrainingdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvdbenchtrainingdata',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
