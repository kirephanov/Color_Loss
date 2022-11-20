from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_page, name='logout'),
    path('profile/', profile_page, name='profile'),
    path('news/', news_page, name='news'),
    path('news/<int:pk>/', GetArticle.as_view(), name='article'),
    path('clans/', clans_page, name='clans'),
    path('create_clan/', CreateClan.as_view(), name='create_clan'),
    path('clans/<int:pk>/', GetClan.as_view(), name='clan'),
]