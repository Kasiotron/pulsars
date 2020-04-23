from django.shortcuts import render
from django.http import HttpResponse

def fill(request):
    f = open("database/static/list.txt")
    lines = f.readlines()
    pulsars = []
    for line in lines:
        psrs = line.rstrip().split(',')
        for psr in psrs:
            if not "READ" in psr and not "search" and not "J0000" in psr:
                pulsars.append(psr)
        if "README.txt" in line:
            break
    f.close()
    return HttpResponse("Database changes <br /> {}".format(pulsars))
