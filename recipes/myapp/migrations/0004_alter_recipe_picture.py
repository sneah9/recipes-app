# Generated by Django 4.1.2 on 2022-11-02 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_ingredient_recipe_picture_relationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='picture',
            field=models.ImageField(default=None, upload_to='recipe'),
        ),
    ]
