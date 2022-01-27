# Generated by Django 4.0.1 on 2022-01-27 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategoryMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuName', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(upload_to='images/menuItem')),
                ('unit', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.FloatField(max_length=10)),
                ('categoryMenuId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categorymenu')),
                ('foodTypeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.foodtype')),
            ],
        ),
    ]