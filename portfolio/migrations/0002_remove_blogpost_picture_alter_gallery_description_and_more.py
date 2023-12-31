# Generated by Django 4.2.3 on 2023-10-04 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='picture',
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blogPost_images/')),
                ('blogPost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.blogpost')),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='images',
            field=models.ManyToManyField(blank=True, to='portfolio.blogimage'),
        ),
    ]
