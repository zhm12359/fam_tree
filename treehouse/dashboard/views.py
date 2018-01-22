from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django import forms

from django.views import generic
from .models import Person

from openpyxl import load_workbook

import json


class UploadFileForm(forms.Form):
    file = forms.FileField()


def IndexView(request):
    persons = Person.objects.all()[:]

    return render(request, 'dashboard/index.html', {'persons': persons})

def BigTreeView(request):
    persons = Person.objects.all()[:]

    return render(request, 'dashboard/BigTreeView.html', {'persons': persons})

def AssignView(request):
    persons = Person.objects.all()[:]

    data = {}
    roots = [] #those who are not bigs

    for p in persons:
        data[p.name] = p

        if not Person.objects.filter(big=p.name).exists():
            roots.append(p)


    # print(roots)
    paths = []

    for r in roots:
        temp = [r.name]

        big = r.big

        while Person.objects.filter(name=big).exists() and big!="":
            if not big:
                break
            temp.append(big)
            tp = Person.objects.get(name=big)
            big = tp.big

        paths.append(temp)

    # print("paths: " )
    # print(paths)

    print("p obj")
    print(data)


    abs = []

    for path in paths:
        temp = []
        for p in path:
            if data[p].assistant_big:
                temp.append( p + "->" + data[p].assistant_big )
            if data[p].assistant_big_2:
                temp.append( p + "->" + data[p].assistant_big_2 )
        abs.append(temp)

    result = []
    for i in range(0, len(paths)):
        result.append( [paths[i], abs[i]] )

    return render(request, 'dashboard/assign.html', {'persons': persons, 'person_obj': data, 'paths': result })

def ImportView(request):
    if request.method == 'POST':
        new_persons = request.FILES['myfile']

        print("here!\n\n\n")
        print(new_persons)
        print(type(new_persons))

        wb = load_workbook(new_persons)

        print(wb)

        big_table = wb['Big']

        for row in big_table.rows:
            name = row[1].value
            big = row[0].value
            if(name and name!="Little"):

                if not Person.objects.filter(name=big).exists():
                    b = Person(name=big)
                    b.save()

                if(Person.objects.filter(name=name).exists()):
                    p = Person.objects.get(name=name)
                    if not p.big:
                        p.big = big
                    else:
                        p.big_2 = big
                else:
                    p = Person(name=name,big=big)
                p.save()

        a_big_table = wb['AB']

        for row in a_big_table:
            name = row[1].value
            a_big = row[0].value
            if (name and name != "Little" and big!="AB"):


                if not Person.objects.filter(name=a_big).exists():
                    b = Person(name=a_big)
                    b.save()

                if (Person.objects.filter(name=name).exists()):
                    p = Person.objects.get(name=name)
                    print(p)
                    if(len(p.assistant_big)<=1):
                        p.assistant_big = a_big
                    else:
                        p.assistant_big_2 = a_big
                else:
                    p = Person(name=name, assistant_big = a_big)
                    print(p)
                p.save()


        return redirect('index')

    return render(request, 'dashboard/import.html')