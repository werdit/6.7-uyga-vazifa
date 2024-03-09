from django.shortcuts import render

from django.http import HttpResponse

def page1(request):
    return HttpResponse("<h1>Page 1</h1><a href='/page2'>Keyingi sahifa</a>")

def page2(request):
    return HttpResponse("<h1>Page 2</h1><a href='/page1'>Oldingi sahifa</a><a href='/page3'>Keyingi sahifa</a>")

def page3(request):
    return HttpResponse("<h1>Page 3</h1><a href='/page2'>Oldingi sahifa</a><a href='/page4'>Keyingi sahifa</a>")

def page4(request):
    return HttpResponse("<h1>Page 4</h1><a href='/page3'>Oldingi sahifa</a><a href='/page5'>Keyingi sahifa</a>")

def page5(request):
    return HttpResponse("<h1>Page 5</h1><a href='/page4'>Oldingi sahifa</a>")
