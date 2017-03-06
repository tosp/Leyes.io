from django.shortcuts import render


def home(request):
    return render(request, "base/home.html")


def base_files(request, filename):
    location = "base/" + filename
    return render(request, location, {}, content_type="text/plain")
