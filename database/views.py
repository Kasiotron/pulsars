from django.shortcuts import render
from django.http import HttpResponse
from database.models import Pulsar
import psrqpy

q = psrqpy.QueryATNF(params='P0', 'P1', 'F0', 'F1', 'F2', 'F3', 'DM', 'DM1', 'RM', 'W50', 'W10', 'S400', 'S1400', 'S2000', 'Dist', 'Age', 'Bsurf', 'Edot')

def fill(request):
    f = open("database/static/list.txt")
    lines = f.readlines()
    pulsars = []
    for line in lines:
        psrs = line.strip().split(',')
        for psr in psrs:
            if not "READ" in psr and not "search" in psr and not "J0000" in psr and psr != '':
                pulsars.append(psr.strip())
        if "README.txt" in line:
            break
    f.close()


    for ps in pulsars:
        p = Pulsar.objects.filter(Name=ps)
        if len(p) == 0:
            psr = Pulsar(Name=ps)
            psr.save()
        else:
            # new values

            #print("already added")
            pass


    return HttpResponse("Database changes <br /> {}".format(1))
