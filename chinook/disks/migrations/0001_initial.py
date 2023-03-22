# Generated by Django 4.1.7 on 2023-03-22 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('composer', models.CharField(max_length=200, null=True)),
                ('milliseconds', models.IntegerField(verbose_name='Duration (ms)')),
                ('bytes', models.IntegerField(verbose_name='Size (bytes)')),
                ('unitPrice', models.FloatField(verbose_name='Unit Price (EUR)')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disks.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disks.artist'),
        ),
    ]
