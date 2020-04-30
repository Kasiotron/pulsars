from django.shortcuts import render
from django.http import HttpResponse
from database.models import Pulsar

def fill(request):
    f = open("database/static/list.txt")
    lines = f.readlines()
    pulsars = []
    for line in lines:
        psrs = line.strip().split(',')
        for psr in psrs:
            if not "READ" in psr and not "search" in psr and not "J0000" in psr and psr != '':
                pulsars.append(psr)
        if "README.txt" in line:
            break
    f.close()

    # for ps in pulsars:
    #     psrs = Pulsar.object.filter(Name=ps)
    #     if len(psr) == 0:
    #         pass
    #     else:
    #         pass
    # print(len(psrs))

    return HttpResponse("Database changes <br /> {}".format(pulsars))
