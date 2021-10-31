# Generated by Django 3.2.8 on 2021-10-30 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0013_auto_20210423_0321'),
    ]

    operations = [
        migrations.CreateModel(
            name='DVDBenchTrainingData',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('CPUUtilization_Average', models.IntegerField()),
                ('NetworkIn_Average', models.IntegerField()),
                ('NetworkOut_Average', models.IntegerField()),
                ('MemoryUtilization_Average', models.DecimalField(decimal_places=10, max_digits=19)),
                ('Final_Target', models.DecimalField(decimal_places=10, max_digits=19)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
