# Generated by Django 3.2 on 2021-04-18 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('Address_line', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('isOrganizationMember', models.BooleanField(default=False)),
                ('bloodGroup', models.CharField(blank=True, max_length=100, null=True)),
                ('dateOfBirth', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('Address_line', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('isOrganizationMember', models.BooleanField(default=True)),
                ('yearOfEstablishment', models.DateField(blank=True, null=True)),
                ('chairman', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationPosts',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('requirementInformation', models.CharField(max_length=100)),
                ('Address_line', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('MemberSelected', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.member')),
                ('postedByOrganization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.organization')),
            ],
            options={
                'ordering': ['-createdAt'],
            },
        ),
    ]
