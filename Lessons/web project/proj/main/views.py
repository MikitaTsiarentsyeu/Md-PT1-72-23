from django.shortcuts import render
import datetime

# Create your views here.

def test(request):
    t = datetime.datetime.now()
    return render(request, 'test.html', {"current_time":t})