# Generated by Django 4.0.2 on 2022-03-04 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_positive', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.user')),
            ],
        ),
    ]
