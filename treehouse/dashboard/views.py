from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django import forms

from django.views import generic
from .models import Person

from openpyxl import load_workbook




class UploadFileForm(forms.Form):
    file = forms.FileField()


class IndexView(generic.DetailView):
    model = Person
    template_name = 'polls/detail.html'


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

                if(Person.objects.filter(name=name).exists()):
                    p = Person.objects.get(name=name)
                    p.big_2 = big
                else:
                    p = Person(name=name,big=big)
                p.save()

        a_big_table = wb['AB']

        for row in a_big_table:
            name = row[1].value
            a_big = row[0].value
            if (name and name != "Little" and big!="AB"):
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