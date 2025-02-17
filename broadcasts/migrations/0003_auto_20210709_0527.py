# Generated by Django 3.2.5 on 2021-07-09 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('broadcasts', '0002_auto_20210709_0515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Broadcast',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('on_air', models.BooleanField(default=False)),
                ('broadcast_host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='broadcasts', to=settings.AUTH_USER_MODEL)),
                ('genre', models.ManyToManyField(blank=True, to='broadcasts.Genre')),
            ],
            bases=('core.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='PictureQuality',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.timestampedmodel',),
        ),
        migrations.DeleteModel(
            name='Broadcasts',
        ),
        migrations.AddField(
            model_name='broadcast',
            name='picture_quality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='broadcasts.picturequality'),
        ),
    ]
