from django.shortcuts import render
from django.http import HttpResponse

def fill(request):
    f = open("database/static/list.txt")
    lines = f.readlines()
    pulsars = []
    for line in lines:
        pulsars.append(line)
        if "README.txt" in lines:
            break
    f.close()
    return HttpResponse("Database changes <br /> {}".format(pulsars))
