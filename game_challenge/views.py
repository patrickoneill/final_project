from django.shortcuts import render, HttpResponse, redirect
from .models import Challenges

# Create your views here.
#checking it works
def working(request):
    return HttpResponse('This is where the fun happens')
    
def main_page(request):
    result = Challenges.objects.all()
    return render(request, "what_is_it.html", {'challenges': result})

def post_challenge(request):
    if request.method=="POST":
        new_challenge = Challenges()
        new_challenge.name = request.POST.get("name")
        new_challenge.save()
        return redirect(main_page)
    return render(request, "post_challenge.html")