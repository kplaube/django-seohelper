# Generated by Django 2.2 on 2019-12-11 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255, verbose_name='URL')),
                ('title', models.CharField(max_length=140, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name='Keywords')),
                ('robot_tags', models.CharField(choices=[('index,follow', 'Index, Follow'), ('noindex,follow', 'No index, Follow'), ('index,nofollow', 'Index, No follow'), ('noindex,nofollow', 'No index, No follow')], default='index,follow', max_length=20, verbose_name='Robots')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'ordering': ('url',),
            },
        ),
    ]
