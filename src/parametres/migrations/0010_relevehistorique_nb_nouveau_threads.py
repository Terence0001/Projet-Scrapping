# Generated by Django 4.1.1 on 2022-09-29 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametres', '0009_alter_relevehistorique_date_rel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='relevehistorique',
            name='nb_nouveau_threads',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
