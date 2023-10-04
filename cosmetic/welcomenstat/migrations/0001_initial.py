# Generated by Django 4.1.7 on 2023-10-04 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cosmetics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('cost', models.CharField(max_length=255)),
                ('seller', models.CharField(max_length=255)),
                ('image_pic', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
