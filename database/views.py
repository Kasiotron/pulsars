from django.shortcuts import render
from django.http import HttpResponse
from database.models import Pulsar
import psrqpy

#q = psrqpy.QueryATNF(params='P0', 'P1', 'F0', 'F1', 'F2', 'F3', 'DM', 'DM1', 'RM', 'W50', 'W10', 'S400', 'S1400', 'S2000', 'Dist', 'Age', 'Bsurf', 'Edot')

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

    # TODO psrqpy

    for ps in pulsars:
        p = Pulsar.objects.filter(Name=ps)
        if len(p) == 0:
            psr = Pulsar(Name=ps)
            psr.save()
        elif len(p) == 1:
            # new values
            psr = p[0]
            vals = psr.__dict__.keys()
            for val in vals:
                attr = getattr(psr, val)
                if attr == None:
                    #q = psrqpy.QueryATNF(params=[val], psrs=[psr.Name])
                    #print(q.table)
                    pass
            pass


    return HttpResponse("Database changes <br /> {}".format(1))
