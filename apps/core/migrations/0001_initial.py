# Generated by Django 3.1.4 on 2020-12-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewCatPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(max_length=120)),
                ('neighborhood', models.CharField(max_length=120)),
                ('text', models.TextField()),
                ('image', models.URLField(max_length=120)),
                ('sighted', models.DateTimeField()),
            ],
        ),
    ]
