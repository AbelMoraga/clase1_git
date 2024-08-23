from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def intento2(request):
    return HttpResponse("<h1> el daiblo esta es la app2</h1>")

def vista2(request):
    html="""
    <h1> vista 2 app2</h2>
    """
    return HttpResponse(html)
    