from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    '''The class extends the user model'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_lvl = models.IntegerField(default=1, blank=True, verbose_name='Player Level')
    user_money = models.IntegerField(default=0, blank=True, verbose_name='Colors') # Game currency
    user_clan = models.ForeignKey('Clan', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Member of a clan')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Clan(models.Model):
    '''Class displays clans inside the game'''
    clan_name = models.CharField(max_length=50, db_index=True, verbose_name='Сlan name')
    clan_description = models.TextField(max_length=250, blank=True, verbose_name='Description')
    clan_is_open = models.BooleanField(blank=True, verbose_name='Is open')

    def __str__(self):
        return self.clan_name

    class Meta:
        verbose_name = 'Clan'
        verbose_name_plural = 'Clans'
        ordering = ['clan_name']

class Article(models.Model):
    '''The class displays articles on the website'''
    article_title = models.CharField(max_length=150, verbose_name='Article title')
    article_content = models.TextField(max_length=2500, verbose_name='Article content')
    article_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Photo')
    article_created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-article_created_at']