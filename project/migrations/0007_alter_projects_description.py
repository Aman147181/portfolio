# Generated by Django 4.1.3 on 2023-01-07 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(default='Lorem ipsum dolor, sit amet consectetur adipisicing elit. Alias, voluptas itaque nulla impedit sunt consequatur consectetur suscipit. Ad, porro ab explicabo dolorem quo, provident soluta quam quisquam error, nulla culpa.'),
        ),
    ]
