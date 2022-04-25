from django.shortcuts import render


def form_manual(request):
    return render(request, 'pages/index.html')