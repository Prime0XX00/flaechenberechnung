from django.http import JsonResponse
from django.shortcuts import render


def overview(request):
    context = {}
    return render(request, "overview.html", context)
