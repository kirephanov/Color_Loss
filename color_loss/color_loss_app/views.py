from django.shortcuts import render

def index(request):
    return render(request=request, template_name='color_loss_app/index.html')
