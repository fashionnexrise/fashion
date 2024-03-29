# Generated by Django 2.2.4 on 2019-08-12 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='WomensPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='', max_length=50)),
                ('cover', models.ImageField(upload_to='images/womens/')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(upload_to='images/mens/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(default='', max_length=50),
        ),
    ]
