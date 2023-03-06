from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def appointment(request):
    return render(request, 'appointment.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def price(request):
    return render(request, 'price.html', {})


def service(request):
    return render(request, 'service.html', {})


def team(request):
    return render(request, 'team.html', {})


def testimonial(request):
    return render(request, 'testimonial.html', {})
