# Generated by Django 4.0.3 on 2023-08-15 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0012_gallerymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=50)),
                ('city', models.CharField(max_length=200)),
                ('house_no', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField(max_length=50)),
                ('state', models.CharField(choices=[('Dhaka', 'Uttaratri'), ('uttara_sec-1', 'uttara_sec-2'), ('Mirpur-1', 'Mirpur-2'), ('Khulshi', 'Muradpur'), ('Cumilla', 'Feni')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
