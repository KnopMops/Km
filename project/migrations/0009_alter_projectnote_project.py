# Generated by Django 5.0.1 on 2024-01-03 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_alter_projectnote_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectnote',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='project.project'),
        ),
    ]
