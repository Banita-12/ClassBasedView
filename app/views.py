from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from app.forms import *


#Returning string as responce by using function based view
def fbv_string(request):
    return HttpResponse('This is the string from fbv_string')

#Returning string as responce by using function based view
class CbvString(View):
    def get(self,request):
        return HttpResponse('This is the string from CbvString')
    

#Rendering html by FBV
def fbvhtml(request):
    return render(request,'fbvhtml.html')

#Rendering html by CBV
class CbvHtml(View):
    def get(self,request):
        return render(request,'CbvHtml.html')
    

#Insert data by FBV through model form
def insert_school_by_fbv(request):
    SFO=SchoolForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_school_by_fbv is done')

    return render(request,'insert_school_by_fbv.html',d)

# Insert Data By using Class Based View
class InsertSchoolByCbv(View):
    def get(self,request):
        ESFO=SchoolForm()
        d={'ESFO':ESFO}
        return render(request,'InsertSchoolByCbv.html',d)
    
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('InsertSchoolByCbv is done')


#Template view
class Cbv_Template(TemplateView):
    template_name='Cbv_Template.html'
