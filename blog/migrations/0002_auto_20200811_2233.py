# Generated by Django 3.0.8 on 2020-08-11 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='chead0',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chead1',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chead2',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head0',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head1',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head2',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='thumbmail',
            field=models.ImageField(default='', upload_to='blog/images'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
