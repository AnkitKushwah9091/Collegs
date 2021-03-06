# Generated by Django 3.1.1 on 2020-09-21 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import photos.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photoalbummodel',
            options={'ordering': [], 'verbose_name': 'Album', 'verbose_name_plural': 'Albums'},
        ),
        migrations.AlterModelOptions(
            name='photomodel',
            options={'ordering': [], 'verbose_name': 'Photo', 'verbose_name_plural': 'Photos'},
        ),
        migrations.AlterField(
            model_name='photomodel',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=photos.models.PhotoModel.post_photo_path),
        ),
        migrations.CreateModel(
            name='LikeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_liked', models.DateTimeField(auto_now=True)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.photomodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
                'db_table': 'PHOTOS_LIKES',
                'ordering': [],
                'unique_together': {('user', 'photo')},
            },
        ),
    ]
