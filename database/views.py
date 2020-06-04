from django.shortcuts import render
from django.http import HttpResponse
from database.models import Pulsar
import psrqpy

#q = psrqpy.QueryATNF(params='P0', 'P1', 'F0', 'F1', 'F2', 'F3', 'DM', 'DM1', 'RM', 'W50', 'W10', 'S400', 'S1400', 'S2000', 'Dist', 'Age', 'Bsurf', 'Edot')

def fill2(request):
    f = open("database/static/list.txt")

    return HttpResponse("Database changes <br /> {}".format(1))


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
    all = psrqpy.PSR_ALL_PARS
    atrs = Pulsar.__dict__.keys()
    attrs = []
    for at in atrs:
        if at.upper() in all:
            attrs.append(at.upper())
    q = psrqpy.QueryATNF(params=attrs, psrs=pulsars)
    cat = q.catalogue

    for ps in pulsars:
        p = Pulsar.objects.filter(NAME=ps)
        if len(p) == 0:
            psr = Pulsar(NAME=ps)
            res = cat.loc[cat["NAME"]==psr.NAME]
            for atr in attrs:
                new_vals = getattr(res, atr).values
                if len(new_vals) > 0:
                    setattr(psr, atr, new_vals[0])
            psr.save()
        elif len(p) == 1:
            # new values
            psr = p[0]
            res = cat.loc[cat["NAME"]==psr.NAME]
            for atr in attrs:
                val = getattr(psr, atr)
                if val == None:
                    new_vals = getattr(res, atr).values
                    if len(new_vals) > 0:
                        setattr(psr, atr, new_vals[0])
            psr.save()
    return HttpResponse("Database changes <br /> {}".format(1))

def view_all(request):
    pulsars = Pulsar.objects.all()
    context = {"pulsars": pulsars}
    return render(request, "database/index.html", context)
