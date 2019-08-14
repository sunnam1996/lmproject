# Generated by Django 2.2.3 on 2019-08-02 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='regis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('UserName', models.CharField(max_length=10)),
                ('FirstName', models.CharField(max_length=10)),
                ('LastName', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=10)),
                ('DateOfJoin', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
                ('MobileNumber', models.IntegerField()),
                ('Password', models.CharField(max_length=10)),
                ('ConfirmPassword', models.CharField(max_length=10)),
            ],
        ),
    ]
