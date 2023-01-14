# Generated by Django 4.1.5 on 2023-01-14 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_description_alter_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image_2',
            field=models.ImageField(blank=True, upload_to='portfolio/images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image_3',
            field=models.ImageField(blank=True, upload_to='portfolio/images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image_4',
            field=models.ImageField(blank=True, upload_to='portfolio/images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image_5',
            field=models.ImageField(blank=True, upload_to='portfolio/images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image_6',
            field=models.ImageField(blank=True, upload_to='portfolio/images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image_7',
            field=models.ImageField(blank=True, upload_to='portfolio/images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image_8',
            field=models.ImageField(blank=True, upload_to='portfolio/images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image_9',
            field=models.ImageField(blank=True, upload_to='portfolio/images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=7000),
        ),
    ]
