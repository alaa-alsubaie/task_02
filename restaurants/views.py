from django.shortcuts import render

from django.http import HttpResponse

 ##def function_name(request):
  ##  return HttpResponse("<h1> Hello</h1>")

def context(request):
    context = {
        "msg": "Hello World!",
    }
    return render(request, 'homepage.html', context)
