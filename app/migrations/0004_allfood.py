# Generated by Django 4.0.3 on 2023-08-13 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_img_aboutmodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('ST', 'STARTERS'), ('SL', 'SALAD'), ('SP', 'SPECIALITY')], max_length=50)),
                ('food_image', models.ImageField(upload_to='FoodImage')),
            ],
        ),
    ]
