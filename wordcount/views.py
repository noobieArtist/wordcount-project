from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def count(request):
    input = request.GET['input']
    iplist = input.split(' ')
    newdict = {}
    for word in iplist:
        if word in newdict:
            newdict[word] += 1
        else:
            newdict[word] = 1
    return render(request, 'count.html', {'fulltext':input, 'newdict':newdict})
def about(request):
    return render(request, 'about.html')
