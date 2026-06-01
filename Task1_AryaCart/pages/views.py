from django.shortcuts import render
from django.contrib import messages


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    if request.method == 'POST':
        messages.success(
            request,
            'Thank you for contacting us! We will get back to you soon.',
        )
    return render(request, 'pages/contact.html')
