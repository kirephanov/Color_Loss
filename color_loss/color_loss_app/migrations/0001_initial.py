# Generated by Django 4.0.6 on 2022-07-26 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clan_name', models.CharField(db_index=True, max_length=50, verbose_name='Сlan name')),
                ('clan_description', models.TextField(blank=True, max_length=250, verbose_name='Description')),
                ('clan_is_open', models.BooleanField(blank=True, verbose_name='Is open')),
            ],
            options={
                'verbose_name': 'Clan',
                'verbose_name_plural': 'Clans',
                'ordering': ['clan_name'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_lvl', models.IntegerField(blank=True, default=1, verbose_name='Player Level')),
                ('user_money', models.IntegerField(blank=True, default=0, verbose_name='Colors')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_clan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='color_loss_app.clan', verbose_name='Member of a clan')),
            ],
        ),
    ]
