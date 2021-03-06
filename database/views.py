from django.shortcuts import render
from django.http import HttpResponse
from database.models import Pulsar
import psrqpy
import re
import datetime


#q = psrqpy.QueryATNF(params='P0', 'P1', 'F0', 'F1', 'F2', 'F3', 'DM', 'DM1', 'RM', 'W50', 'W10', 'S400', 'S1400', 'S2000', 'Dist', 'Age', 'Bsurf', 'Edot')

def fill2(request):
    f = open("database/static/list.txt")
    lines = f.readlines()
    pulsar_dict = {}
    for i, line in enumerate(lines):
        checked_line = re.search('/fred/oz005.search/(.*)(.*)/1284', line)
        if checked_line:
            checked_line = checked_line.string
            #print(checked_line)
            pulsar_key = checked_line.split("/")[4]
            #pulsar_key = checked_line.group(1)
            #datetime_list = checked_line.group(2).split('-')
            datetime_list = checked_line.split("/")[5]
            freq = checked_line.split("/")[6][:-2]
            #print(pulsar_key)
            #print(datetime_list)
            #print(freq)
            pulsar_dict[pulsar_key] = {
                #'date': datetime_list[0:10],
                'start_time': datetime_list[11:19],
                'start_datetime': datetime_list[0:19],
                'freq': freq,
                'end_time': datetime_list[11:19] # TODO !
                }
        if 'obs.header' in lines[i]:
            try:
                endtime = lines[i-1].split(',')[-2].split('-')[-1].split('.')[0]  # # # naprawic
            except:
                print('asd')
                print(lines[i-1].split(','))
            if endtime:
                pulsar_dict[pulsar_key]['end_time'] = endtime

    for k, v in pulsar_dict.items():
        try:
            p = Pulsar.objects.get(NAME=k)
        except:
            print("Pulsar {} not found...".format(k))

        #print(v["start_datetime"])
        print(v)
        st = datetime.datetime.strptime(v["start_datetime"], "%Y-%m-%d-%H:%M:%S")
        en_str = "{}-{}-{}-{}".format(st.year, st.month, st.day, v["end_time"])
        print(en_str)
        #en = datetime.datetime.strptime(en_str, "%Y-%m-%d-%H:%M:%S")
        #print(en-st)

        #o = Observation(start_datetime=v["start_datetime"], frequancy=v["freq"],  )
        #o.save()
        #p.observations.add(o)
        ######
    return HttpResponse("Database changes <br /> {}".format(pulsar_dict))


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
