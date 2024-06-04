from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Word
from .models import CustomUser
from .serializers import WordSerializer
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from rest_framework import permissions
from django.http import HttpResponse

class CustomLoginView(LoginView):
    template_name = 'words/login.html'
    success_url = reverse_lazy('main')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = CustomUserCreationForm()
    return render(request, 'words/register.html', {'form': form})

class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [permissions.AllowAny]
    
def main_view(request):
    return render(request, 'words/main.html')

def redoc_view(request):
    return render(request, 'words/redoc.html')

def about_view(request):
    return render(request, 'words/about.html')

def login_view(request):
    return render(request, 'words/login.html')

def registration_view(request):
    return render(request, 'words/registration.html')

def profile_view(request):
    return render(request, 'words/profile.html')

def users_online(request):
    connected_users = [str(user) for user in CustomUser.objects.all()]
    return HttpResponse("Currently connected: %s" % connected_users)
