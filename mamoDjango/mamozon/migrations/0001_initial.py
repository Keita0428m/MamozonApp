# Generated by Django 3.0.7 on 2020-06-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='thumbnails/', verbose_name='サムネイル')),
                ('name', models.CharField(max_length=150, verbose_name='名前')),
                ('price', models.IntegerField(verbose_name='価格')),
                ('description', models.TextField(verbose_name='説明')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
    ]
