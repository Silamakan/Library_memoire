from django.shortcuts import render

# Create your views here.
def register(request):

    template_name = 'app_auth/register.html'
    return render(request, template_name)