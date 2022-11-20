from cProfile import Profile
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, TemplateView
from .forms import UserRegisterForm, UserLoginForm, ClanForm
from django.contrib import messages
from  django.contrib.auth import login, logout
from django.urls import reverse_lazy
from .models import *

# def index(request):
#     '''Returns the home page'''
#     return render(request=request, template_name='color_loss_app/index.html')

class Index(TemplateView):
    '''Returns the home page'''
    template_name = "color_loss_app/index.html"


def login_page(request):
    '''Returns the user's login page'''
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }

    return render(request=request, template_name='color_loss_app/login.html', context=context)


def register_page(request):
    '''Returns the user registration page'''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration completed successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Registration error.')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    
    return render(request=request, template_name='color_loss_app/register.html', context=context)


def logout_page(request):
    '''Returns the user's logout page'''
    logout(request)

    return redirect('login')


def profile_page(request):
    '''Returns the user's profile page'''
    users = User.objects.all().select_related('profile')

    context = {'users': users}

    return render(request=request, template_name='color_loss_app/profile.html', context=context)


def news_page(request):
    '''Returns the news page'''
    news = Article.objects.all()

    context = {'news': news}

    return render(request=request, template_name='color_loss_app/news.html', context=context)


class GetArticle(DetailView):
    '''Returns the article page'''
    model = Article
    template_name = 'color_loss_app/article.html'
    context_object_name = 'article'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def clans_page(request):
    '''Returns the clans page'''
    clans = Clan.objects.all()

    context = {'clans': clans}

    return render(request=request, template_name='color_loss_app/clans.html', context=context)


class CreateClan(CreateView):
    template_name = 'color_loss_app/create_clan.html'
    form_class = ClanForm
    success_url = reverse_lazy('clans')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GetClan(DetailView):
    '''Returns the article page'''
    model = Clan
    template_name = 'color_loss_app/clan.html'
    context_object_name = 'clan'

    def get_context_data(self,  *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.all().select_related('profile')
        return context
