# Generated by Django 4.0.3 on 2023-08-14 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_eventsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChefsModel',
            fields=[
                ('sectionmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.sectionmodel')),
                ('name', models.CharField(max_length=50)),
                ('chefs_image', models.ImageField(upload_to='ChefsImage')),
            ],
            bases=('app.sectionmodel',),
        ),
    ]