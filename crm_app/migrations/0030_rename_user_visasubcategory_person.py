# Generated by Django 4.0.2 on 2023-10-12 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0029_visasubcategory_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visasubcategory',
            old_name='user',
            new_name='person',
        ),
    ]
