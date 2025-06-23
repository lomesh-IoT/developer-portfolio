from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'portfolio/home.html')

def aboutMe_view(request):
    return render(request, 'portfolio/about_me.html')

def profile_view(request):
    return render(request, 'portfolio/profile.html')